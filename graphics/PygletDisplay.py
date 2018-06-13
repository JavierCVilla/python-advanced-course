import pyglet

from math import sin, cos, pi, sqrt
twopi = 2*pi

from Display import Display

class PygletDisplay(Display):

    def __init__(self):
        super(PygletDisplay, self).__init__()
        self.window = pyglet.window.Window(600,400)
        self.fps_display = pyglet.clock.ClockDisplay()

        @self.window.event
        def on_draw():
            self.window.clear()
            #display.draw_circle(particle.x, particle.y, radius)
            for e in self._elements:
                e.draw(self)
            self.fps_display.draw()

    def width(self):
        return self.window.width

    def height(self):
        return self.window.height

    def refresh(self):
        self.window.update()

    def bounding_box(self):
        box = (0, self.width(), 0, self.height())
        return box

    def draw_circle(self, x, y, radius):
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

    def schedule(self, action, time):
        pyglet.clock.schedule_interval(action, time)

    def go(self):
        self.schedule(self.update, 1/60.0)
        pyglet.app.run()
