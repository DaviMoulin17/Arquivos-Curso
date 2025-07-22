from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.lang import Builder
import os

# Carregando o arquivo .kv manualmente com caminho absoluto relativo ao .py
Builder.load_file(os.path.join(os.path.dirname(__file__), "bool_prop.kv"))

class ToggleStateWidget(BoxLayout):
    is_active = BooleanProperty(False)

    def on_toggle_state(self, instance, state):
        self.is_active = (state == 'down')

class BoolPropApp(App):
    def build(self):
        return ToggleStateWidget()

if __name__ == "__main__":
    BoolPropApp().run()
