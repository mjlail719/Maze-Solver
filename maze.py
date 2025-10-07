from graphics import Line, Point, Window
import time


class Maze():
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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                c = Cell(window=self.__win)
                column.append(c)
            self.__cells.append(column)
        if self.__win:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self.__draw_cell(i, j)
        
    def __draw_cell(self, i, j):
        cell_x1 = self.x1 + (self.cell_size_x * i)
        cell_y1 = self.y1 + (self.cell_size_y * j)
        cell_x2 = self.cell_size_x + cell_x1
        cell_y2 = self.cell_size_y + cell_y1
        if self.__win:
            self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
            self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        

class Cell():
    def __init__(self, window=None):
        self.__win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self_center_x = self.get_center_x()
        self_center_y = self.get_center_y()
        to_center_x = to_cell.get_center_x()
        to_center_y = to_cell.get_center_y()
        self.__win.draw_line(Line(Point(self_center_x, self_center_y), Point(to_center_x, to_center_y)), fill_color)

    def get_center_x(self):
        return (self.__x1 + self.__x2) / 2
    
    def get_center_y(self):
        return (self.__y1 + self.__y2) / 2
        