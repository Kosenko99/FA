import sqlite3
from sqlite3 import sqlite_version
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.graphics import Rectangle, Color
from kivy.graphics import *

class MyApp(App):
    def build(self):
        r = GridLayout(cols=3, row_force_default=True, row_default_height=70)
        l1 = Label(text="ФИО", font_size=22, halign="center")
        r.add_widget(l1)
        l2 = Label(text="Возраст", font_size=22, halign="center")
        r.add_widget(l2)
        l3 = Label(text="Категория", font_size=22, halign="center")
        r.add_widget(l3)
        conn = sqlite3.connect(r'coach.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM trener;")
        records = cur.fetchall()
        for row in records:
            fio = str(row[0])
            vozrast = str(row[1])
            ktegoru = str(row[2])
            l1 = Label(text=fio, font_size=22, halign="center")
            r.add_widget(l1)
            l2 = Label(text=vozrast, font_size=22, halign="center")
            r.add_widget(l2)
            l3 = Label(text=ktegoru, font_size=22, halign="center")
            r.add_widget(l3)

        return r

if __name__ == "__main__":
    MyApp().run()