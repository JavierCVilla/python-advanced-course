try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
master = tk.Tk()

w = tk.Canvas(master, width=600, height=400, bg='black')
w.pack()

x,y = w.winfo_height() / 2, w.winfo_width() / 2
vx, vy = 80.0, 150.0

# Particle size
particle_height = 60
particle_width = 60
particle = w.create_oval(x,y, particle_height, particle_width, outline='yellow')

def update(dt):
    global x,y, vx, vy
    oldx, oldy = x,y
    x += vx*dt
    y += vy*dt

    if x + particle_width > w.winfo_width():
        x = w.winfo_width() - particle_width
        vx = - vx

    if x < 0:
        x = 0
        vx = - vx

    if y + particle_height > w.winfo_height():
        y = w.winfo_height() - particle_height
        vy = - vy

    if y < 0:
        y = 0
        vy = - vy

    w.move(particle, x-oldx, y-oldy)
    w.update()
    w.after(17, update, 1/60.0)

update(0)

tk.mainloop()
