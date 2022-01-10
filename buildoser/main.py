from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 420)
Config.set('graphics', 'height', 640)


class Calculator(App):
    def build(self):
        self.result = '0'
        main_layout = GridLayout(rows=2)
        label_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=[1.0, 0.2])
        keyboard_layout = (GridLayout(cols=4, size_hint=[1.0, 0.8], padding=10))
        main_layout.add_widget(label_layout)
        main_layout.add_widget(keyboard_layout)
        self.text_layout = Label(text=self.result, font_size=50, text_size=(420 - 50, 640 * .2 - 50), halign='right')
        label_layout.add_widget(self.text_layout)

        keyboard_layout.add_widget(Button(text='(', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text=')', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='C', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='/', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))

        keyboard_layout.add_widget(Button(text='7', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='8', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='9', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='X', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))

        keyboard_layout.add_widget(Button(text='4', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='5', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='6', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.73, .97, .24, 1], on_press=self.calculate))
        keyboard_layout.add_widget(Button(text='-', font_size=40, size_hint=(None, None), size=(100, 100),
                                          background_color=[.90, .22, .62, 1], on_press=self.calculate))

        fl1 = GridLayout(cols=1, size_hint=(None, None), size=(100, 200))
        fl2 = GridLayout(cols=1, size_hint=(None, None), size=(100, 200))
        fl3 = GridLayout(cols=1, size_hint=(None, None), size=(100, 200))
        fl4 = AnchorLayout(size_hint=(None, None), size=(100, 200))
        keyboard_layout.add_widget(fl1)
        keyboard_layout.add_widget(fl2)
        keyboard_layout.add_widget(fl3)
        keyboard_layout.add_widget(fl4)

        fl1.add_widget(Button(text='1', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        fl2.add_widget(Button(text='2', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        fl3.add_widget(Button(text='3', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        fl4.add_widget(Button(text='+', font_size=40, size_hint=(None, None), size=(100, 200),
                              background_color=[.90, .22, .62, 1], on_press=self.calculate))

        fl1.add_widget(Button(text='.', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        fl2.add_widget(Button(text='0', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        fl3.add_widget(Button(text='=', font_size=40, size_hint=(None, None), size=(100, 100),
                              background_color=[.73, .97, .24, 1], on_press=self.calculate))
        # keyboard_layout.add_widget(Button(text='+', font_size=40))

        return main_layout

    def calculate(self, instance):

        if self.result == '0':
            self.result = ''

        if instance.text == '=':
            self.result = str(eval(self.result))
        elif instance.text == 'C':
            self.result = '0'
        elif instance.text == 'X':
            self.result += '*'

        if instance.text != '=' and instance.text != 'C' and instance.text != 'X':
            self.result += str(instance.text)

        print(instance.text)
        self.text_layout.text = self.result

if __name__ == '__main__':
    Calculator().run()
