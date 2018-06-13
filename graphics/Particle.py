from Display import Display

class Particle:

    def __init__(self, r, pos, velocity):
        self.r = r
        self.x, self.y = pos
        self.vx, self.vy = velocity

    def move(self, dt):
        self.x = self.x + dt * self.vx
        self.y = self.y + dt * self.vy

    def bounce(self, limits):
        xmin, xmax, ymin, ymax = limits
        if self.x + self.r > xmax:
            self.x = xmax - self.r - (self.x - xmax + self.r)
            self.vx = - self.vx

        # left far (completely out)
        if self.x + self.r < xmin:
            self.x = xmin + self.r + (xmin - self.x + self.r)
            self.vx = - self.vx

        # left near
        if self.x - self.r < xmin:
            self.x += (xmin - (self.x - self.r))*2
            self.vx = - self.vx

        # top
        if self.y + self.r > ymax:
            self.y = ymax - self.r - (self.y - ymax + self.r)
            self.vy = - self.vy

        # bottom
        if self.y - self.r < ymin:
            self.y += (ymin - (self.y - self.r))*2
            self.vy = - self.vy

    def draw(self, display):
        display.draw_circle(self.x, self.y, self.r)
