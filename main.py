from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.running = False
        self.canvas.pack(fill=BOTH, expand=True)
        self.__root.protocol("WM_Delete_Window", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
        

def main():
    
    win = Window(800, 600)
    win.wait_for_close()