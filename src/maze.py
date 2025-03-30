import random

from cell import Cell
from graphics import Point


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            rows = []
            for j in range(self._num_rows):
                rows.append(Cell(self._win))
            self._cells.append(rows)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        p1 = Point(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y)
        p2 = Point(p1.x + self._cell_size_x, p1.y + self._cell_size_y)
        cell.draw(p1, p2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False

        i = len(self._cells) - 1
        j = len(self._cells[i]) - 1
        self._cells[i][j].has_bottom_wall = False

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell._visited = True
        while True:
            to_visit = []

            # check left cell
            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append(("L", i - 1, j))

            # check right cell
            index = len(self._cells) - 1
            if i < index and not self._cells[i + 1][j]._visited:
                to_visit.append(("R", i + 1, j))

            # check top cell
            if j > 0 and not self._cells[i][j - 1]._visited:
                to_visit.append(("T", i, j - 1))

            # check bottom cell
            index = len(self._cells[i]) - 1
            if j < index and not self._cells[i][j + 1]._visited:
                to_visit.append(("B", i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break

            index = random.randint(0, len(to_visit) - 1)
            next_cell = to_visit[index]

            i = next_cell[1]
            j = next_cell[2]

            if next_cell[0] == "L":
                cell.has_left_wall = False
                self._cells[i][j].has_right_wall = False
            elif next_cell[0] == "R":
                cell.has_right_wall = False
                self._cells[i][j].has_left_wall = False
            elif next_cell[0] == "T":
                cell.has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            elif next_cell[0] == "B":
                cell.has_bottom_wall = False
                self._cells[i][j].has_top_wall = False

            self._break_walls_r(i, j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
