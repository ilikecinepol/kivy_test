from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class My_app(App):
    def build(self):
        '''bl = BoxLayout(orientation='horizontal', spacing=100)
        bl.add_widget(Button(text='Кнопка 1'))
        bl.add_widget(Button(text='Кнопка 2'))
        bl.add_widget(Button(text='Кнопка 3'))'''
        # return bl

        gl = GridLayout(cols=3)
        for i in range(30):
            gl.add_widget(Button(text=f'Кнопка {i}'))

        return gl


if __name__ == '__main__':
    My_app().run()
