import kivy
import random
import subprocess
import sys

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

red = [1, 0, 0, 1]

class HFloatLayoutExample(App):

    def build(self):
        layout = GridLayout(cols = 1)
        img = Image(source='sfa.png', size_hint=(.6, .4),pos=(360, 200))
        layout.add_widget(img)
        btn = Button(text="Расписание", background_color=red, size_hint=(.5, .20),pos=(10, 400))
        btn.bind(on_press=self.on_press_btn)
        btn2 = Button(text="Тренеры", background_color=red, size_hint=(.5, .20),pos=(10, 250))
        btn2.bind(on_press=self.on_press_btn2)
        btn3 = Button(text="Об академии", background_color=red, size_hint=(.5, .20),pos=(10, 100))
        btn3.bind(on_press=self.on_press_btn3)

        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)


        return layout

    def on_press_btn(self, instance):
        subprocess.call('python setting.py', shell=True)

    def on_press_btn2(self, instance):
        subprocess.call('python coach.py', shell=True)

    def on_press_btn3(self, instance):
        subprocess.call('python about.py', shell=True)


if __name__ == "__main__":
    app = HFloatLayoutExample()
    app.run()