from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Ellipse, Line, Rectangle
from random import random


class MeuPaintWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_width = 2
        self.current_shape = 'Linha'
        self.start_pos = None

    def on_touch_down(self, touch):
        color = (random(), random(), random())
        touch.ud['color'] = color
        touch.ud['start'] = (touch.x, touch.y)

        with self.canvas:
            Color(*color)
            if self.current_shape == 'Linha':
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
            elif self.current_shape == 'Elipse':
                d = 30
                touch.ud['ellipse'] = Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            elif self.current_shape == 'Retângulo':
                touch.ud['rect'] = Rectangle(pos=(touch.x, touch.y), size=(1, 1))

    def on_touch_move(self, touch):
        if self.current_shape == 'Linha' and 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
        elif self.current_shape == 'Retângulo' and 'rect' in touch.ud:
            x0, y0 = touch.ud['start']
            x1, y1 = touch.x, touch.y
            x = min(x0, x1)
            y = min(y0, y1)
            w = abs(x1 - x0)
            h = abs(y1 - y0)
            touch.ud['rect'].pos = (x, y)
            touch.ud['rect'].size = (w, h)

    def clear_canvas(self, instance):
        self.canvas.clear()

    def set_line_width(self, instance, value):
        self.line_width = value

    def set_shape(self, spinner, text):
        self.current_shape = text


class MeuPaintApp(App):
    def build(self):
        layout = FloatLayout()
        paint_widget = MeuPaintWidget()

        # Botão de limpar
        clear_btn = Button(text='Limpar', size_hint=(0.15, 0.08), pos_hint={'x': 0.8, 'top': 1})
        clear_btn.bind(on_release=paint_widget.clear_canvas)

        # Slider de espessura
        slider = Slider(min=1, max=10, value=2, size_hint=(0.3, 0.05), pos_hint={'x': 0.05, 'top': 1})
        slider.bind(value=paint_widget.set_line_width)

        # Spinner de forma
        shape_spinner = Spinner(
            text='Linha',
            values=['Linha', 'Retângulo', 'Elipse'],
            size_hint=(0.2, 0.08),
            pos_hint={'x': 0.5, 'top': 1}
        )
        shape_spinner.bind(text=paint_widget.set_shape)

        layout.add_widget(paint_widget)
        layout.add_widget(clear_btn)
        layout.add_widget(slider)
        layout.add_widget(shape_spinner)

        return layout


if __name__ == '__main__':
    MeuPaintApp().run()
