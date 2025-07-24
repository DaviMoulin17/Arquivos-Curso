from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "input_prop.kv"))

class InputPropWidget(BoxLayout):
    pass

class InputPropApp(App):
    def build(self):
        return InputPropWidget()

if __name__ == "__main__":
    InputPropApp().run()
