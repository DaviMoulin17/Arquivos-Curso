from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty

class MyCustomWidget(BoxLayout):
    message = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)
        self.log_label = Label(text="Aguardando mensagem...", color=(0,0,0,1))
        self.input_msg = TextInput(multiline=False, hint_text="Digite uma nova mensagem",
                                   foreground_color=(0,0,0,1), background_color=(1,1,1,1))
        self.btn = Button(text="Atualizar Mensagem")
        self.btn.bind(on_release=self.update_message)

        self.add_widget(self.log_label)
        self.add_widget(self.input_msg)
        self.add_widget(self.btn)

    def update_message(self, *args):
        self.message = self.input_msg.text
        self.log_label.text = "Nova mensagem: " + self.message

class TestApp(App):
    def build(self):
        return MyCustomWidget()

if __name__ == "__main__":
    TestApp().run()
