from Display import Display
from Vector import Vector

class Particle:

    def __init__(self, r, pos, velocity):
        self.r = r
        self.pos = Vector(*pos)
        self.velocity = Vector(*velocity)

    @property
    def x(self):
        return self.pos.x
    @property
    def y(self):
        return self.pos.y

    @x.setter
    def x(self, new):
        self.pos.x = new

    @y.setter
    def y(self, new):
        self.pos.y = new

    @property
    def vx(self):
        return self.velocity.x
    @property
    def vy(self):
        return self.velocity.y

    @vx.setter
    def vx(self, new):
        self.velocity.x = new

    @vy.setter
    def vy(self, new):
        self.velocity.y = new

    def move(self, dt):
        self.pos.x = self.pos.x + dt * self.velocity.x
        self.pos.y = self.pos.y + dt * self.velocity.y

    def bounce(self, limits):
        xmin, xmax, ymin, ymax = limits

        # right
        if self.pos.x + self.r > xmax:
            self.pos.x = xmax - self.r - (self.pos.x - xmax + self.r)
            self.velocity.x = - self.velocity.x

        # left
        if self.pos.x - self.r < xmin:
            self.pos.x += (xmin - (self.pos.x - self.r))*2
            self.velocity.x = - self.velocity.x

        # top
        if self.pos.y + self.r > ymax:
            self.pos.y = ymax - self.r - (self.pos.y - ymax + self.r)
            self.velocity.y = - self.velocity.y

        # bottom
        if self.pos.y - self.r < ymin:
            self.pos.y += (ymin - (self.pos.y - self.r))*2
            self.velocity.y = - self.velocity.y

    def draw(self, display):
        display.draw_circle(self.pos.x, self.pos.y, self.r)
