from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import random
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

Window.clearcolor = (0/255, 0/255, 80/255, 1)

class FilmeApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Título
        self.lbl_titulo = Label(
            text="App de Sugestão de Filme",
            font_size=30,
            color=(1, 1, 0, 1),
            size_hint_y=None,
            halign="center",
            valign="middle"
        )
        self.lbl_titulo.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        layout.add_widget(self.lbl_titulo)

        # Entrada de nome e seleção de gênero
        self.txt_nome = TextInput(
            hint_text="Digite seu nome",
            font_size=20,
            size_hint_y=None,
            height=50,
            multiline=False
        )
        layout.add_widget(self.txt_nome)

        self.spinner_genero = Spinner(
            text="Selecione um gênero",
            values=("Ação", "Comédia", "Terror", "Romance", "Animação", "Ficção Científica"),
            font_size=18,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.spinner_genero)

        # Botões
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_sugerir = Button(text="Sugerir Filme", background_color=(0.678, 0.847, 0.902, 1))
        btn_sugerir.bind(on_release=self.sugerir_filme)
        btn_limpar = Button(text="Limpar", background_color=(1.0, 0.341, 0.2, 1))
        btn_limpar.bind(on_release=self.limpar)
        btn_layout.add_widget(btn_sugerir)
        btn_layout.add_widget(btn_limpar)
        layout.add_widget(btn_layout)

        # Mensagem
        self.lbl_mensagem = Label(
            text="Digite seu nome, escolha um gênero e clique em Sugerir Filme",
            font_size=18,
            color=(1, 1, 0, 1),
            size_hint_y=None,
            height=40,
            halign="center",
            valign="middle"
        )
        self.lbl_mensagem.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        layout.add_widget(self.lbl_mensagem)

        # Imagem do filme
        self.img_filme = AsyncImage(source="", allow_stretch=True, keep_ratio=True)
        layout.add_widget(self.img_filme)

        # Histórico
        self.scroll = ScrollView(size_hint=(1, 0.3))
        self.layout_historico = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.layout_historico.bind(minimum_height=self.layout_historico.setter("height"))
        self.scroll.add_widget(self.layout_historico)
        layout.add_widget(Label(text="Histórico:", font_size=20, size_hint_y=None, height=30))
        layout.add_widget(self.scroll)

        return layout

    def sugerir_filme(self, instance):
        nome = self.txt_nome.text.strip()
        genero = self.spinner_genero.text

        filmes = filmes = {
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
    ]
}


        if not nome:
            self.lbl_mensagem.text="Por favor, digite seu nome."
            return
        if genero not in filmes:
            self.lbl_mensagem.text="Selecione um gênero válido."
            return

        filme, ano, img = random.choice(filmes[genero])
        self.lbl_mensagem.text = f"Olá, {nome}! Sua sugestão de filme de {genero} é: {filme} ({ano})"
        self.img_filme.source = img
        

        # Histórico
        item_hist = Label(
            text=f"{filme} ({ano}) - {genero}",
            font_size=16,
            size_hint_y=None,
            height=30,
            halign="left",
            valign="middle"
        )
        item_hist.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        self.layout_historico.add_widget(item_hist)

    def limpar(self, instance):
        self.txt_nome.text=""
        self.spinner_genero.text="Selecione um gênero"
        self.lbl_mensagem.text="Digite seu nome, escolha um gênero e clique em Sugerir Filme"
        self.img_filme.source=""
        self.layout_historico.clear_widgets()


if __name__=="__main__":
    FilmeApp().run()
