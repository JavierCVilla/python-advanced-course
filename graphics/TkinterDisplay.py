from Display import Display

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class TkinterDisplay(Display):
    def __init__(self):
        super(TkinterDisplay, self).__init__()
        self.master = tk.Tk()
        self.window = tk.Canvas(self.master, width=600, height=400, bg='black')
        self.window.pack()

    def go(self):
        self.update(0)
        tk.mainloop()

    def width(self):
        return self.window.winfo_width()

    def height(self):
        return self.window.winfo_height()

    def bounding_box(self):
        box = (0, self.width(), 0, self.height())
        return box

    def move(self, draw, dx, dy):
        self.window.move(draw, dx, dy)

    def refresh(self):
        self.window.delete(tk.ALL)
        self.window.update()

    def draw_circle(self, x, y, radius):
        r = radius
        return self.window.create_oval(x-r,y-r, x+r, y+r, outline='yellow')

    def update(self, dt):
        super(TkinterDisplay, self).update(dt)
        self.refresh()
        for e in self._elements:
            e.draw(self)
        self.schedule(self.update, 1/60.0)

    def schedule(self, action, time):
        self.window.after(17, action, time)
