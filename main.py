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
        canvas.pack()
class Cell:
    def __init__(self, _x1: int, _x2: int, _y1:int, _y2:int, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall =has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = win 
        
    def draw(self, canvas: Canvas):
        
        if self.has_left_wall:
            canvas.create_line(self._x1, self._)
        if self.has_top_wall:
            canvas.create_line()
        if self.has_bottom_wall:
            canvas.create_line()
        if self.has_right_wall:
            canvas.create_line()
        
        
        
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.running = False
        self.canvas.pack(fill=BOTH, expand=True)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)

def main():
    
    win = Window(800, 600)
    pt1 = Point(100, 100)
    pt2 = Point(400,400)
    line = Line(pt1, pt2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()