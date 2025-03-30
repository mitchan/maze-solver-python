from cell import Cell
from graphics import Point
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
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

    def _create_cells(self):
        for i in range(self._num_cols):
            rows = []
            for j in range(self._num_rows):
                rows.append(Cell(self._win))
            self._cells.append(rows)

        self._break_entrance_and_exit()

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
