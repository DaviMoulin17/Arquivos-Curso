from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "custom_prop.kv"))

class PlayerInfo(BoxLayout):
    player_name = StringProperty("Jogador 1")
    player_score = NumericProperty(0)
    is_online = BooleanProperty(False)
    
    def incrementar_pontuacao(self):
        self.player_score += 1

class CustomPropApp(App):
    def build(self):
        return PlayerInfo()

if __name__ == "__main__":
    CustomPropApp().run()
