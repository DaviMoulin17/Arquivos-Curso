from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock

class PainelControle(BoxLayout):
    status = StringProperty("IA Desligada")
    ameaca = NumericProperty(0)
    ia_ativa = BooleanProperty(False)

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa
        if self.ia_ativa:
            self.status = "IA Ativada ✅"
            Clock.schedule_interval(self.aumentar_ameaca, 1)
        else:
            self.status = "IA Desligada ❌"
            self.ameaca = 0
            Clock.unschedule(self.aumentar_ameaca)

    def aumentar_ameaca(self, dt):
        if self.ameaca < 100:
            self.ameaca += 5
        else:
            self.status = "⚠️ Ameaça Máxima!"
            Clock.unschedule(self.aumentar_ameaca)

    def enviar_comando(self):
        comando = self.ids.campo_comando.text.strip()
        if not comando:
            self.status = "Digite um comando válido."
            return
        
        if self.ia_ativa:
            self.status = f"Comando executado: {comando}"
        else:
            self.status = "Erro: IA está desligada."
        
        self.ids.campo_comando.text = ""

class PainelIAApp(App):
    def build(self):
        return PainelControle()

if __name__ == "__main__":
    PainelIAApp().run()
