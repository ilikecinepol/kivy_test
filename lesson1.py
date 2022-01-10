from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 640)
Config.set('graphics', 'height', 480)


class MyApp(App):

    def build(self):
        self.counter = 0
        s = Scatter()
        fl = FloatLayout(size=(300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(text='Кнопка',
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=[.34, .73, .14, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(640 / 2 - 160, 480 / 2 - 480 / 8)))

        return s

    def btn_press(self, instance):
        # print('Кнопка нажата')
        instance.text = str(self.counter + 1)
        self.counter += 1


if __name__ == '__main__':
    MyApp().run()
