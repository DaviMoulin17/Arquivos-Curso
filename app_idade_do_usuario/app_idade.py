from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)

class MainWidget(BoxLayout):
    mensagem = StringProperty("Digite seus dados acima")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mensagens = []

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
            mensagem = f"Olá, {nome}! Você é menor de idade."
        elif idade < 60:
            mensagem = f"Olá, {nome}! Você é maior de idade."
        else:
            mensagem = f"Olá, {nome}! Você é idoso e merece muito respeito."
            
        # Atualizar mensagem atual
        self.mensagem = mensagem
        
        # Adicionar ao histórico com nome e idade
        historico_item = f"{nome} ({idade} anos): {mensagem.split('!')[1].strip()}"
        self.mensagens.append(historico_item)
        
        # Limitar o histórico aos 5 últimos registros
        if len(self.mensagens) > 5:
            self.mensagens = self.mensagens[-5:]
            
        # Atualizar o histórico
        self.ids.label_historico.text = "\n".join(self.mensagens)
        
        # Limpar os campos
        self.ids.campo_nome.text = ""
        self.ids.campo_idade.text = ""
        
class IdadeApp(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    IdadeApp().run()
