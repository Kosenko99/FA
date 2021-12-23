import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.graphics import Rectangle, Color
from kivy.graphics import *

class MyApp(App):
    def build(self):
        r = GridLayout(cols = 1, row_force_default = True,row_default_height = 70)
        l1 = Label(text="Об академии", font_size=22, halign="center")
        r.add_widget(l1)
        l2 = Label(text="Приложение было создано специально для организации Spain Football Academy из Новосибирска."
                        "В приложении пользователь может ознакомиться с расписанием тренировок и данными тренеров."
                        "Автором приложения является студент СГУГиТ обучающийся в группе БИ-33 - Косенко Евгений Валерьевич.",
                   halign="center", font_size=15, text_size = (700,200))
        r.add_widget(l2)
        return r

if __name__ == "__main__":
    MyApp().run()