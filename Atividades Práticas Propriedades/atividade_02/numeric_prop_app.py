from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
import os

# Carregar o arquivo .kv manualmente
Builder.load_file(os.path.join(os.path.dirname(__file__), "numeric_prop.kv"))

class Contador(BoxLayout):
    conta = NumericProperty(0)

    def aumentar(self):
        self.conta += 1

class NumericPropApp(App):
    def build(self):
        return Contador()

if __name__ == "__main__":
    NumericPropApp().run()
