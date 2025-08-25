from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Definindo tamanho da janela
Window.size = (400, 600)

class ListaTarefasApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título do aplicativo
        self.titulo = Label(text='Minha Lista de Tarefas', font_size=24, size_hint=(1, 0.1))
        self.layout.add_widget(self.titulo)
        
        # TextInput para inserir tarefas
        self.entrada = TextInput(hint_text='Digite sua tarefa aqui', multiline=False, size_hint=(1, 0.1))
        self.layout.add_widget(self.entrada)
        
        # Botão Adicionar
        self.botao_adicionar = Button(text='Adicionar', size_hint=(1, 0.1), background_color=(0.2, 0.6, 0.9, 1))
        self.botao_adicionar.bind(on_press=self.adicionar_tarefa)
        self.layout.add_widget(self.botao_adicionar)
        
        # Botão Limpar lista (desafio extra)
        self.botao_limpar = Button(text='Limpar Lista', size_hint=(1, 0.1), background_color=(0.9, 0.3, 0.3, 1))
        self.botao_limpar.bind(on_press=self.limpar_lista)
        self.layout.add_widget(self.botao_limpar)
        
        # Área de exibição das tarefas
        self.tarefas_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        self.layout.add_widget(self.tarefas_layout)
        
        return self.layout
    
    def adicionar_tarefa(self, instance):
        tarefa_texto = self.entrada.text.strip()
        if tarefa_texto:  # Verifica se não está vazio
            nova_tarefa = Label(text=f'• {tarefa_texto}', font_size=18, size_hint_y=None, height=30)
            self.tarefas_layout.add_widget(nova_tarefa)
            self.entrada.text = ''  # Limpa o TextInput
        else:
            self.entrada.text = ''
            self.entrada.hint_text = 'Insira uma tarefa válida'
    
    def limpar_lista(self, instance):
        self.tarefas_layout.clear_widgets()

# Executa o aplicativo
if __name__ == '__main__':
    ListaTarefasApp().run()
