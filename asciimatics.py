# It is a funny way to have your terminal coloured :D with this funny library
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
  effects = [
      Cycle(
          screen,
          FigletText("We4theRep0rt", font='big'),
          int(screen.height / 2 - 8)),
      Cycle(
          screen,
          FigletText("The best has yet to come", font='small'),
          int(screen.height / 2 + 3)),
      Stars(screen, 600)
    ]
  
  screen.play([Scene(effects, 500)])

Screen.wrapper(demo)
