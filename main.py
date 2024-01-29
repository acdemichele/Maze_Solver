from tkinter import Tk, BOTH, Canvas



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Line:
    def __init__(self, pt1: Point, pt2: Point):
        self.pt1 = pt1
        self.pt2 = pt2
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
class Cell:
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None     
        self._y1 = None
        self._y2 = None
        self._win = win 
        
    def draw(self, x1, y1, x2, y2):
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        
        
        
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.__running = False
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
            
    def close(self):
        self.__running = False
    
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

def main():
    
    win = Window(800, 600)
    pt1 = Point(100, 100)
    pt2 = Point(400,400)
    line = Line(pt1, pt2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()