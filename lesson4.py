from kivy.app import App
from kivy.uix.widget import Widget

from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class Painterwiget(Widget):
    def __init__(self, **kwargs):
        super(Painterwiget, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0, 1)
            self.line = Line(points=(), width=10, joint='miter')

    def on_touch_down(self, touch):
        self.line.points += (touch.x, touch.y)

class Paintapp(App):
    def build(self):
        return Painterwiget()


if __name__ == '__main__':
    Paintapp().run()
