from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv_bind.kv"))

class MyContainer(BoxLayout):
    pass

class KvBindApp(App):
    def build(self):
        return MyContainer()

if __name__ == "__main__":
    KvBindApp().run()
