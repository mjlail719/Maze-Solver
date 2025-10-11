from graphics import Line, Point, Window
import time
import random


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
        seed=None,
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
        self.__break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        self.__solve_r(0,0)

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

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_indexes = [] 
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_indexes.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_indexes.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_indexes.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_indexes.append((i, j + 1))

            if len(next_indexes) == 0:
                self.__draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(next_indexes))
            next_index = next_indexes[direction_index]

            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            self.__break_walls_r(next_index[0], next_index[1])

    def __solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if self.__cells[i][j] == self.__cells[-1][-1]:
            return True
        
        next_indexes = []
        correct_path = False
        # left
        if i > 0 and not self.__cells[i - 1][j].visited and not self.__cells[i][j].has_left_wall:
            next_indexes.append((i - 1, j))
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            correct_path = self.__solve_r(i - 1, j)
            if correct_path:
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)
        # right
        if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited and not self.__cells[i][j].has_right_wall:
            next_indexes.append((i + 1, j))
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            correct_path = self.__solve_r(i + 1, j)
            if correct_path:
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)
        # up
        if j > 0 and not self.__cells[i][j - 1].visited and not self.__cells[i][j].has_top_wall:
            next_indexes.append((i, j - 1))
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            correct_path = self.__solve_r(i, j - 1)
            if correct_path:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)
        # down
        if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited and not self.__cells[i][j].has_bottom_wall:
            next_indexes.append((i, j + 1))
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            correct_path = self.__solve_r(i, j + 1)
            if correct_path:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)
        return False

    def __reset_cells_visited(self):
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__cells[i][j].visited = False

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
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black" if self.has_left_wall else "white")
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black" if self.has_top_wall else "white")
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black" if self.has_right_wall else "white")
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black" if self.has_bottom_wall else "white")

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
        