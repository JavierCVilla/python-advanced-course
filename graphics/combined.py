from sys import argv
from Particle import Particle

if "tk" in argv:
    from TkinterDisplay import TkinterDisplay as Display
else:
    from PygletDisplay import PygletDisplay as Display

display = Display()

x,y = display.height() / 2, display.width() / 2
vx, vy = 80.0, 150.0
radius = 60

particle = Particle(radius, (x, y),(vx, vy))
display.add(particle)
display.go()
