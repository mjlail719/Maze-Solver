import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_entrance_and_exit(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_reset_visited(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        all_reset = True
        for i in range(len(m1._Maze__cells)):
            for j in range(len(m1._Maze__cells[0])):
                if m1._Maze__cells[i][j].visited != False:
                    all_reset = False

        self.assertEqual(all_reset, True)

if __name__ == "__main__":
    unittest.main()