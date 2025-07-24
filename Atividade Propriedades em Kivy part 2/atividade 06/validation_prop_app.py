from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("validation_prop.kv")

class ValidatedInputWidget(BoxLayout):
    validated_text = StringProperty("Texto válido")
    last_valid = "Texto válido"

    def validate_input(self, new_text):
        # Validação: mínimo 5 caracteres e sem números
        if len(new_text) >= 5 and not any(char.isdigit() for char in new_text):
            self.validated_text = new_text
            self.last_valid = new_text
        else:
            # Volta para o último texto válido
            self.ids.input_field.text = self.last_valid
            self.validated_text = self.last_valid

class ValidationApp(App):
    def build(self):
        return ValidatedInputWidget()

if __name__ == "__main__":
    ValidationApp().run()
