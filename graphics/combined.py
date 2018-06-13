implemetation = raw_input("Choose an implementation tkinter [tk] or pyglet [pyg]: ")

if "tk" in implemetation:
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
else:
    import pyglet
    from math import sin, cos, pi, sqrt
    twopi = 2*pi

    window = pyglet.window.Window(600,400)
    fps_display = pyglet.clock.ClockDisplay()

    x,y = window.width / 2, window.height / 2
    vx, vy = 80.0, 150.0
    radius = 30

    @window.event
    def on_draw():
        window.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield x + radius * cos(angle)
                yield y + radius * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        fps_display.draw()


    def update(dt):
        global x,y, vx, vy
        x += vx*dt
        y += vy*dt

        if x + radius > window.width:
            x = window.width - radius
            vx = - vx

        if x - radius < 0:
            x =  radius
            vx = - vx

        if y + radius > window.height:
            y = window.height - radius
            vy = - vy

        if y - radius < 0:
            y = radius
            vy = - vy

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()