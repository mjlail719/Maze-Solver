from graphics import Window, Line, Point
from maze import Cell, Maze

def main():
    win = Window(800, 600)
    maze = Maze(10,10,11,15,50,50,win)
    maze.solve()
    win.wait_for_close()
    


if __name__ == "__main__":
    main()