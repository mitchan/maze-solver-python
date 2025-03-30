from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, p1, p2):
        if self._win is None:
            return

        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y

        line = Line(Point(p1.x, p1.y), Point(p1.x, p2.y))
        self._win.draw_line(line, "black" if self.has_left_wall else "white")

        line = Line(Point(p2.x, p1.y), Point(p2.x, p2.y))
        self._win.draw_line(line, "black" if self.has_right_wall else "white")

        line = Line(Point(p1.x, p1.y), Point(p2.x, p1.y))
        self._win.draw_line(line, "black" if self.has_top_wall else "white")

        line = Line(Point(p1.x, p2.y), Point(p2.x, p2.y))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "white")

    def get_center_point(self):
        return Point((self._x2 + self._x1) // 2, (self._y2 + self._y1) // 2)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        p1 = self.get_center_point()
        p2 = to_cell.get_center_point()
        print(p1.x, p1.y)
        line = Line(p1, p2)
        self._win.draw_line(line, "grey" if undo else "red")
