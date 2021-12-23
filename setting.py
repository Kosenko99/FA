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
        layout = GridLayout(cols = 2)
        btn = Button(text="Понедельник", background_color=red, size_hint=(.5, .20),pos=(10, 400))
        btn.bind(on_press=self.on_press_btn)
        btn2 = Button(text="Вторник", background_color=red, size_hint=(.5, .20),pos=(10, 250))
        btn2.bind(on_press=self.on_press_btn2)
        btn3 = Button(text="Среда", background_color=red, size_hint=(.5, .20),pos=(10, 100))
        btn3.bind(on_press=self.on_press_btn3)
        btn4 = Button(text="Четверг", background_color=red, size_hint=(.5, .20),pos=(10, 400))
        btn4.bind(on_press=self.on_press_btn4)
        btn5 = Button(text="Пятница", background_color=red, size_hint=(.5, .20),pos=(10, 250))
        btn5.bind(on_press=self.on_press_btn5)
        btn6 = Button(text="Суббота", background_color=red, size_hint=(.5, .20),pos=(10, 100))
        btn6.bind(on_press=self.on_press_btn6)

        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)

        return layout

    def on_press_btn(self, instance):
        subprocess.call('python pon.py', shell=True)

    def on_press_btn2(self, instance):
        subprocess.call('python vtor.py', shell=True)

    def on_press_btn3(self, instance):
        subprocess.call('python sred.py', shell=True)

    def on_press_btn4(self, instance):
        subprocess.call('python chetv.py', shell=True)

    def on_press_btn5(self, instance):
        subprocess.call('python pyatn.py', shell=True)

    def on_press_btn6(self, instance):
        subprocess.call('python subb.py', shell=True)


if __name__ == "__main__":
    app = HFloatLayoutExample()
    app.run()