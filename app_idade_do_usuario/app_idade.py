from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MainWidget(BoxLayout):
    mensagem = StringProperty("Digite seus dados acima")

    def verificar_idade(self):
        nome = self.ids.campo_nome.text.strip()
        idade_texto = self.ids.campo_idade.text.strip()

        # Verificação básica
        if not nome or not idade_texto:
            self.mensagem = "⚠️ Preencha todos os campos!"
            return

        # Tentando converter a idade
        try:
            idade = int(idade_texto)
        except ValueError:
            self.mensagem = "⚠️ Digite apenas números na idade!"
            return

        # Condição de maioridade
        if idade < 18:
            self.mensagem = f"Olá, {nome}! Você é menor de idade."
        else:
            self.mensagem = f"Olá, {nome}! Você é maior de idade."

class IdadeApp(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    IdadeApp().run()
