from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ListProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "paint_prop.kv"))

class MyPaintWidget(Widget):
    current_draw_color = ListProperty([1, 0, 0, 1])  # Vermelho

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.current_draw_color)
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

    def set_draw_color(self, color_list):
        self.current_draw_color = color_list

class PaintApp(BoxLayout):
    pass

class MyPaintApp(App):
    def build(self):
        return PaintApp()

if __name__ == "__main__":
    MyPaintApp().run()
