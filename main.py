from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import random

# Fundo da janela
Window.clearcolor = (0/255, 0/255, 80/255, 1)

# Lista de filmes
filmes = {
    "Ação": [
        ("John Wick", 2014, "https://img.elo7.com.br/product/zoom/265E425/big-poster-filme-john-wick-lo02-tamanho-90x60-cm-poster-cinema.jpg?_gl=1*1h13t2j*_gcl_au*MTMzMzY3ODQ0Ny4xNzU2NDAyODE1*_ga*OTk3NjQ4MTA0LjE3NTY0MDI4MTU.*_ga_22YVRK2WCW*czE3NTY0MDI4MTUkbzEkZzAkdDE3NTY0MDI4MTUkajYwJGwwJGgxODE5Nzk0OTIw"),
        ("Mad Max: Estrada da Fúria", 2015, "https://img.elo7.com.br/product/zoom/265F0ED/big-poster-filme-mad-max-estrada-da-furia-lo08-tam-90x60-cm-poster-cinema.jpg?_gl=1*e4h89f*_gcl_au*MTMzMzY3ODQ0Ny4xNzU2NDAyODE1*_ga*OTk3NjQ4MTA0LjE3NTY0MDI4MTU.*_ga_22YVRK2WCW*czE3NTY0MDI4MTUkbzEkZzEkdDE3NTY0MDMzOTkkajYwJGwwJGgxODE5Nzk0OTIw"),
        ("Vingadores: Ultimato", 2019, "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SL1500_.jpg"),
        ("Gladiador", 2000, "https://i.pinimg.com/1200x/50/fb/ef/50fbef1358104b1cda975d39dc8682d3.jpg"),
        ("O Protetor", 2014, "https://i.pinimg.com/736x/97/b1/14/97b1148de4b77b94cc79d59bfaf53204.jpg"),
        ("Missão Impossível: Efeito Fallout", 2018, "https://i.pinimg.com/736x/91/8a/6c/918a6c97b1a19a64bc3625f8a47472a8.jpg")
    ],
    "Comédia": [
        ("As Branquelas", 2004, "https://i.pinimg.com/736x/e4/71/2a/e4712ae58795ab898ba239df75db673a.jpg"),
        ("Se Beber, Não Case!", 2009, "https://i.pinimg.com/1200x/74/a7/a3/74a7a37667410cffdb7c037099039ace.jpg"),
        ("Superbad", 2007, "https://i.pinimg.com/1200x/a4/86/50/a486504e8854d00e7fcb84506308a189.jpg"),
        ("Gente Grande", 2010, "https://i.pinimg.com/736x/b1/4b/95/b14b95148f0d1555f0d6c328c23145f5.jpg"),
        ("O Máskara", 1994, "https://i.pinimg.com/1200x/e0/96/2e/e0962e226ff8c59d465358773a2cdcb5.jpg"),
        ("Todo Poderoso", 2003, "https://i.pinimg.com/1200x/5c/66/b6/5c66b62386aa7af3e932ba14b1669268.jpg")
    ],
    "Terror": [
        ("Invocação do Mal", 2013, "https://i.pinimg.com/736x/ca/c1/0a/cac10a09d92b5331c0a9c410a8f4b84c.jpg"),
        ("It: A Coisa", 2017, "https://i.pinimg.com/736x/54/64/26/546426f0faec37276e05caf059c6454b.jpg"),
        ("O Exorcista", 1973, "https://i.pinimg.com/736x/5e/4d/05/5e4d05f5fc4674e8169e0eed7abafd75.jpg"),
        ("A Freira", 2018, "https://i.pinimg.com/736x/cc/a6/ab/cca6ab8b37a4d4e0adfb3ff79fca2041.jpg"),
        ("Atividade Paranormal", 2007, "https://i.pinimg.com/736x/d2/c0/db/d2c0db66a87cc7884c84705fd0426870.jpg"),
        ("Corra!", 2017, "https://i.pinimg.com/736x/e1/f9/a0/e1f9a0e21bfa396063294ec275813401.jpg")
    ],
    "Romance": [
        ("Titanic", 1997, "https://i.pinimg.com/736x/ea/3a/ae/ea3aaeb6fec6c6213df3ab1472c7e5a2.jpg"),
        ("Diário de uma Paixão", 2004, "https://i.pinimg.com/736x/91/8b/88/918b88576de32abf6e791aee60be5fb5.jpg"),
        ("Orgulho e Preconceito", 2005, "https://i.pinimg.com/736x/bc/97/53/bc975396bb79a72e32d317bd097cea3b.jpg"),
        ("A Culpa é das Estrelas", 2014, "https://i.pinimg.com/736x/48/a0/13/48a013635baeb19667f4399eb036563e.jpg"),
        ("Romeu + Julieta", 1996, "https://i.pinimg.com/736x/a7/42/4e/a7424e8f5efd561981b648e126cf228a.jpg"),
        ("Ghost: Do Outro Lado da Vida", 1990, "https://i.pinimg.com/736x/a7/19/85/a7198569b15d7213031fd442058d7144.jpg")
    ],
    "Animação": [
        ("Toy Story", 1995, "https://i.pinimg.com/736x/8e/bd/48/8ebd48f66f760c1066bb7f82204d8866.jpg"),
        ("Shrek", 2001, "https://i.pinimg.com/736x/82/58/d5/8258d5d80e06df3581b603530e17e7de.jpg"),
        ("Procurando Nemo", 2003, "https://i.pinimg.com/736x/59/19/a6/5919a697bff3873f28f73992c95e5e5f.jpg"),
        ("Up: Altas Aventuras", 2009, "https://i.pinimg.com/736x/70/26/3b/70263b8092e00cddc2e4cedfe8287715.jpg"),
        ("Gato de Botas 2", 2022, "https://i.pinimg.com/736x/7c/77/70/7c7770e094d990f806763c791a076fdf.jpg"),
        ("Como Treinar o Seu Dragão", 2010, "https://i.pinimg.com/736x/22/20/4a/22204a9fe4ff0cbaca524b802a63a3b2.jpg")
    ],
    "Ficção Científica": [
        ("Interestelar", 2014, "https://i.pinimg.com/736x/3f/09/dd/3f09ddcc1d3c3740f6a74e63d57fba61.jpg"),
        ("Matrix", 1999, "https://i.pinimg.com/736x/ed/45/16/ed4516338fa5df348c13a2a7ce1e7998.jpg"),
        ("A Origem", 2010, "https://i.pinimg.com/736x/13/bf/49/13bf49eff74f4773005df65d83c82240.jpg"),
        ("Blade Runner 2049", 2017, "https://i.pinimg.com/736x/4b/1c/ab/4b1cab19aed05183b61c11e399b53833.jpg"),
        ("Guardiões da Galáxia", 2014, "https://i.pinimg.com/736x/d8/49/e1/d849e1330681c2b7d8b9ecbbf0b17dd9.jpg"),
        ("Avatar", 2009, "https://i.pinimg.com/736x/d2/71/4a/d2714af5f61ec69b65db6959718f0543.jpg"),
        ("De Volta para o Futuro", 1985, "https://i.pinimg.com/736x/ba/6f/f2/ba6ff2005256ae1405e4a8cc14b98f07.jpg")
    ],
    "Fantasia": [
    # Harry Potter
    ("Harry Potter e a Pedra Filosofal", 2001, "https://i.pinimg.com/1200x/fa/8c/80/fa8c80b1695d091d62efef11ef07d9de.jpg"),
    ("Harry Potter e a Câmara Secreta", 2002, "https://i.pinimg.com/736x/cd/5e/28/cd5e286a0af2cf3a2a82a04d37bfd575.jpg"),
    ("Harry Potter e o Prisioneiro de Azkaban", 2004, "https://i.pinimg.com/736x/59/20/81/592081af4aa6d9d6c5300d0c4c1770ed.jpg"),
    ("Harry Potter e o Cálice de Fogo", 2005, "https://i.pinimg.com/1200x/6a/fd/36/6afd36e8edb795f4eba7acc7f02fe690.jpg"),
    ("Harry Potter e a Ordem da Fênix", 2007, "https://i.pinimg.com/736x/ca/5b/f2/ca5bf27ff2ef306faf1bb217c65df3b1.jpg"),
    ("Harry Potter e o Enigma do Príncipe", 2009, "https://i.pinimg.com/1200x/2f/bb/34/2fbb34efd8790e9f9a5e01e8ae2834e1.jpg"),
    ("Harry Potter e as Relíquias da Morte Parte 1", 2010, "https://i.pinimg.com/736x/4d/ab/cf/4dabcf824a00ebb9093127d1179a794c.jpg"),
    ("Harry Potter e as Relíquias da Morte Parte 2", 2011, "https://i.pinimg.com/736x/ae/ce/1a/aece1aeba20d092d0ddb8d85ec97b2af.jpg"),

    # Animais Fantásticos
    ("Animais Fantásticos e Onde Habitam", 2016, "https://i.pinimg.com/1200x/3e/e6/0f/3ee60f6b4ec7abda77a10aa41ca7b0b1.jpg"),
    ("Animais Fantásticos: Os Crimes de Grindelwald", 2018, "https://i.pinimg.com/1200x/1a/a4/7e/1aa47e20e51842960ab7d5d152152e1c.jpg"),
    ("Animais Fantásticos: Os Segredos de Dumbledore", 2022, "https://i.pinimg.com/1200x/9b/36/5e/9b365e927b4d10196b7fd515297e39b8.jpg"),

    # O Senhor dos Anéis
    ("O Senhor dos Anéis: A Sociedade do Anel", 2001, "https://i.pinimg.com/736x/c7/89/fd/c789fd292e75beeb861ee4059317f46a.jpg"),
    ("O Senhor dos Anéis: As Duas Torres", 2002, "https://i.pinimg.com/1200x/fe/98/28/fe9828d616848f7c4be388ce65718314.jpg"),
    ("O Senhor dos Anéis: O Retorno do Rei", 2003, "https://i.pinimg.com/736x/bf/87/2e/bf872ee6ee5ae7f31e209731e3c7cda5.jpg"),

    # O Hobbit
    ("O Hobbit: Uma Jornada Inesperada", 2012, "https://i.pinimg.com/736x/35/d9/62/35d96228dd077cba12fe9c65cbf12fa3.jpg"),
    ("O Hobbit: A Desolação de Smaug", 2013, "https://i.pinimg.com/736x/fa/46/3d/fa463db3e8b1f24799b8f5fd6a30e9a0.jpg"),
    ("O Hobbit: A Batalha dos Cinco Exércitos", 2014, "https://i.pinimg.com/1200x/d1/c1/c4/d1c1c4e7d78675223cc8654da731044e.jpg")
    ]

}

# --- Tela 1: Login ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        with layout.canvas.before:
            Color(0.1, 0.1, 0.3, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        layout.bind(size=lambda inst, val: setattr(self.rect, "size", val))
        layout.bind(pos=lambda inst, val: setattr(self.rect, "pos", val))

        layout.add_widget(Label(text="Bem-vindo ao App de Filmes", font_size=32, color=(1,1,0,1)))
        self.input_name = TextInput(hint_text="Digite seu nome", font_size=22, multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.input_name)

        btn_continue = Button(text="Continuar", size_hint_y=None, height=50, background_color=(0.2,0.7,0.3,1))
        btn_continue.bind(on_press=self.go_to_suggestion)
        layout.add_widget(btn_continue)
        self.add_widget(layout)

    def go_to_suggestion(self, instance):
        nome = self.input_name.text.strip()
        if nome:
            self.manager.get_screen("suggestion").user_name = nome
            self.manager.current = "suggestion"

# --- Tela 2: Sugestão ---
class SuggestionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_name = ""
        self.favoritos = []

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        with layout.canvas.before:
            Color(0.05, 0.05, 0.2, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        layout.bind(size=lambda inst, val: setattr(self.rect, "size", val))
        layout.bind(pos=lambda inst, val: setattr(self.rect, "pos", val))

        self.label_welcome = Label(text="", font_size=26, color=(1,1,0,1))
        layout.add_widget(self.label_welcome)

        self.spinner = Spinner(text="Selecione um gênero", values=list(filmes.keys()), size_hint_y=None, height=50)
        layout.add_widget(self.spinner)

        btn_sugerir = Button(text="Sugerir Filme", size_hint_y=None, height=50, background_color=(0.8,0.6,0.2,1))
        btn_sugerir.bind(on_press=self.sugerir_filme)
        layout.add_widget(btn_sugerir)

        self.label_filme = Label(text="", font_size=20, color=(1,1,1,1))
        layout.add_widget(self.label_filme)

        self.img_filme = AsyncImage(source="", allow_stretch=True, keep_ratio=True)
        layout.add_widget(self.img_filme)

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        # Botão para adicionar aos favoritos sem sair da tela
        btn_add_fav = Button(text="Adicionar aos Favoritos", background_color=(0.2,0.5,0.8,1))
        btn_add_fav.bind(on_press=self.adicionar_favoritos)
        # Botão para ver favoritos
        btn_ver_fav = Button(text="Ver Favoritos", background_color=(0.5,0.7,0.2,1))
        btn_ver_fav.bind(on_press=lambda x: setattr(self.manager, "current", "favoritos"))
        # Botão voltar para login
        btn_voltar = Button(text="Voltar", background_color=(0.8,0.2,0.2,1))
        btn_voltar.bind(on_press=lambda x: setattr(self.manager, "current", "login"))

        btn_layout.add_widget(btn_add_fav)
        btn_layout.add_widget(btn_ver_fav)
        btn_layout.add_widget(btn_voltar)
        layout.add_widget(btn_layout)
        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.label_welcome.text = f"Olá, {self.user_name}! Escolha um gênero:"

    def sugerir_filme(self, instance):
        genero = self.spinner.text
        if genero not in filmes:
            self.label_filme.text = "Escolha um gênero válido!"
            return
        filme, ano, img = random.choice(filmes[genero])
        self.label_filme.text = f"{filme} ({ano}) - {genero}"
        self.img_filme.source = img
        # guarda temporariamente o último filme sugerido
        self.ultimo_filme = (filme, ano, genero, img)

    def adicionar_favoritos(self, instance):
        if hasattr(self, "ultimo_filme"):
            if self.ultimo_filme not in self.favoritos:
                self.favoritos.append(self.ultimo_filme)
            # Atualiza a tela de favoritos
            self.manager.get_screen("favoritos").favoritos = self.favoritos

# --- Tela 3: Favoritos ---
class FavoritosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.favoritos = []

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        with layout.canvas.before:
            Color(0.1,0.1,0.2,1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        layout.bind(size=lambda inst, val: setattr(self.rect, "size", val))
        layout.bind(pos=lambda inst, val: setattr(self.rect, "pos", val))

        layout.add_widget(Label(text="Meus Filmes Favoritos", font_size=26, color=(1,1,0,1)))

        self.scroll = ScrollView()
        self.grid = GridLayout(cols=2, size_hint_y=None, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        btn_voltar = Button(text="Voltar", size_hint_y=None, height=50, background_color=(0.8,0.2,0.2,1))
        btn_voltar.bind(on_press=lambda x: setattr(self.manager, "current", "suggestion"))
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.grid.clear_widgets()
        for filme, ano, genero, img in self.favoritos:
            box = BoxLayout(orientation="vertical", size_hint_y=None, height=250, spacing=5)
            capa = AsyncImage(source=img, allow_stretch=True, keep_ratio=True)
            titulo = Label(text=f"{filme} ({ano})", font_size=16, color=(1,1,1,1), size_hint_y=None, height=30)
            box.add_widget(capa)
            box.add_widget(titulo)
            self.grid.add_widget(box)

# --- App ---
class FilmeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SuggestionScreen(name="suggestion"))
        sm.add_widget(FavoritosScreen(name="favoritos"))
        return sm

if __name__=="__main__":
    FilmeApp().run()
