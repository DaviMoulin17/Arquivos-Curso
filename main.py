from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random

# cor de fundo
Window.clearcolor = (0.9, 0.9, 0.9, 1)

class FilmeApp(App):
    def build(self):
        # layout principal
        layout = BoxLayout(orientation="vertical", spacing=20, padding=30)

        # título
        self.lbl_titulo = Label(
            text="App de Sugestão de Filme",
            font_size=28,
            color=(0, 0, 0, 1)
        )

        # campo de texto
        self.txt_nome = TextInput(
            hint_text="Digite seu nome",
            font_size=20,
            size_hint_y=None,
            height=50,
            multiline=False
        )

        # botão
        btn_sugerir = Button(
            text="Sugerir Filme",
            font_size=22,
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_sugerir.bind(on_release=self.sugerir_filme)

        # label de mensagem
        self.lbl_mensagem = Label(
            text="Digite seu nome e clique em Sugerir Filme",
            font_size=20,
            color=(0, 0, 0, 1),
            halign="center"
        )

        # adicionar ao layout
        layout.add_widget(self.lbl_titulo)
        layout.add_widget(self.txt_nome)
        layout.add_widget(btn_sugerir)
        layout.add_widget(self.lbl_mensagem)

        return layout

    def sugerir_filme(self, instance):
        nome = self.txt_nome.text.strip()

        filmes = [
            ("Vingadores: Era de Ultron", 2015),
            ("John Wick", 2014),
            ("As Branquelas", 2004),
            ("Superbad: É Hoje", 2007),
            ("Invocação do Mal", 2013),
            ("It: A coisa", 2018),
            ("Clube da Luta", 1999),
            ("Ilha do Medo", 2010),
            ("Titanic", 1997),
            ("Querido John", 2010),
            ("Interestelar", 2014),
            ("Star Wars: Os Últimos Jedi", 2017),
            ("Harry Potter e a Pedra Filosofal", 2001),
            ("O Senhor dos Anéis: A Sociedade do Anel", 2001),
            ("Forrest Gump", 1994),
            ("O Menino do Pijama Listrado", 2008),
            ("Toy Story", 1995),
            ("Shrek", 2001)
        ]

        if not nome:
            self.lbl_mensagem.text = "Por favor, digite seu nome."
        else:
            filme, ano = random.choice(filmes)
            self.lbl_mensagem.text = f"Olá, {nome}! Sua sugestão de filme é: {filme} ({ano})."


if __name__ == "__main__":
    FilmeApp().run()
