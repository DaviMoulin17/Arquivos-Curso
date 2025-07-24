from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty

class StatusWidget(BoxLayout):
    status_message = StringProperty("Offline")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Label que mostrará o status
        self.label = Label(text=self.status_message, font_size=32)
        self.add_widget(self.label)

        # Botão para mudar o status
        self.button = Button(text="Mudar Status", font_size=24)
        self.button.bind(on_release=self.mudar_status)
        self.add_widget(self.button)

        # Vincula a mudança da propriedade ao método update_label_text
        self.bind(status_message=self.update_label_text)

    def update_label_text(self, instance, value):
        self.label.text = value

    def mudar_status(self, instance):
        if self.status_message == "Offline":
            self.status_message = "Online"
        else:
            self.status_message = "Offline"

class BindStringApp(App):
    def build(self):
        return StatusWidget()

if __name__ == "__main__":
    BindStringApp().run()
