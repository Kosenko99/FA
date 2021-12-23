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
        r = GridLayout(cols=4, row_force_default=True, row_default_height=70)
        ll1 = Label(text="")
        r.add_widget(ll1)
        ll2 = Label(text="ВТОРНИК", font_size=22, halign="center")
        r.add_widget(ll2)
        ll3 = Label(text="")
        r.add_widget(ll3)
        ll4 = Label(text="")
        r.add_widget(ll4)
        l1 = Label(text="Группа", font_size=22, halign="center")
        r.add_widget(l1)
        l2 = Label(text="Время", font_size=22, halign="center")
        r.add_widget(l2)
        l3 = Label(text="Адресс", font_size=22, halign="center")
        r.add_widget(l3)
        l4 = Label(text="Тренер", font_size=22, halign="center")
        r.add_widget(l4)
        conn = sqlite3.connect(r'rsp.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Vtornik;")
        records = cur.fetchall()
        for row in records:
            gruppa = str(row[0])
            vremya = str(row[1])
            adress = str(row[2])
            trener = str(row[3])
            l1 = Label(text=gruppa, font_size=22, halign="center")
            r.add_widget(l1)
            l2 = Label(text=vremya, font_size=22, halign="center")
            r.add_widget(l2)
            l3 = Label(text=adress, font_size=22, halign="center")
            r.add_widget(l3)
            l4 = Label(text=trener, font_size=22, halign="center")
            r.add_widget(l4)

        return r

if __name__ == "__main__":
    MyApp().run()