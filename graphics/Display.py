class Display(object):

    def __init__(self):
        self._elements = []

    def add(self, elem):
        self._elements.append(elem)

    def update(self, dt):
        for e in self._elements:
            e.move(dt)
            e.bounce(self.bounding_box())

    def bounding_box():
        return

    def go():
        pass

    def draw_circle():
        pass

    def draw_square():
        pass
