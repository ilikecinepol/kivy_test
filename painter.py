from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class Painterwiget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 0, 1)
            rad = 40
            Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

class Paintapp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=8)
        main_layout.add_widget(Painterwiget)
        main_layout.add_widget(gl)
        b1 = Button(text='Reset')
        b2 = Button(text='Save')
        gl.add_widget(b1)
        gl.add_widget(b2)
        return main_layout()


if __name__ == '__main__':
    Paintapp().run()
