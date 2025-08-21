from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BoasVindasApp(App):
    def build(self):
        # Layout principal (vertical)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Título fixo no topo
        self.titulo = Label(
            text="👋 App de Boas-Vindas",
            font_size=28,
            bold=True,
            size_hint=(1, 0.2),
            halign="center",
            valign="middle"
        )
        self.titulo.bind(size=self.titulo.setter("text_size"))
        layout.add_widget(self.titulo)

        # Campo de texto para digitar o nome
        self.entrada = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2),
            font_size=20
        )
        layout.add_widget(self.entrada)

        # Botão de enviar
        self.botao = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.1, 0.5, 0.8, 1),  # azul
            font_size=22
        )
        self.botao.bind(on_press=self.mostrar_mensagem)
        layout.add_widget(self.botao)

        # Label para mostrar a mensagem
        self.mensagem = Label(
            text="",
            font_size=22,
            size_hint=(1, 0.4),
            halign="center",
            valign="middle"
        )
        self.mensagem.bind(size=self.mensagem.setter("text_size"))
        layout.add_widget(self.mensagem)

        return layout

    def mostrar_mensagem(self, instance):
        nome = self.entrada.text.strip()

        if nome:
            self.mensagem.text = f"Bem-vindo(a), {nome}!"
        else:
            self.mensagem.text = "Por favor, digite seu nome."


if __name__ == "__main__":
    BoasVindasApp().run()
