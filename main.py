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