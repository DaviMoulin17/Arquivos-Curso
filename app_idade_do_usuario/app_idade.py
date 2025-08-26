from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)
class MainWidget(BoxLayout):
    mensagem = StringProperty("Digite seus dados acima")

    def verificar_idade(self):
        nome = self.ids.campo_nome.text.strip()
        idade_texto = self.ids.campo_idade.text.strip()

        # Verificação básica
        if not nome or not idade_texto:
            self.mensagem = "Preencha todos os campos!"
            return

        # Tentando converter a idade
        try:
            idade = int(idade_texto)
        except ValueError:
            self.mensagem = "Digite apenas números na idade!"
            return
        
        # Validação de idade
        if idade < 0 or idade > 120:
            self.mensagem = "Idade inválida!"
            return

        # Condição de maioridade
        if idade < 18:
            self.mensagem = f"Olá, {nome}! Você é menor de idade."
        elif idade < 60:
            self.mensagem = f"Olá, {nome}! Você é maior de idade."
        else:
            self.mensagem = f"Olá, {nome}! Você é idoso e merece muito respeito."
            
        # Historico
        if not hasattr(self, "mensagens"):
            self.mensagens = []
            
        self.mensagens.append(self.mensagem)
        self.ids.label_resultado.text = "\n".join(self.mensagens)
        
class IdadeApp(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    IdadeApp().run()
