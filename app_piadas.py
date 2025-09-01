import requests
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button

class JokeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        
        # Label para mostrar a piada
        self.joke_label = Label(
            text="Clique no botão para ver uma piada!",
            halign="center",
            valign="middle",
            font_size=20
        )
        self.joke_label.bind(size=self.joke_label.setter('text_size'))
        
        # Botão para carregar nova piada
        self.button = Button(
            text="Nova Piada",
            size_hint=(1, 0.2),
            font_size=18
        )
        self.button.bind(on_press=self.get_joke)
        
        self.layout.add_widget(self.joke_label)
        self.layout.add_widget(self.button)
        
        return self.layout
    
    def get_joke(self, instance):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                joke = response.json()
                setup = joke.get("setup", "")
                punchline = joke.get("punchline", "")
                self.joke_label.text = f"{setup}\n\n{punchline}"
            else:
                self.joke_label.text = "Erro ao carregar piada "
        except Exception as e:
            self.joke_label.text = f"Erro: {e}"
            
if __name__ == "__main__":
    JokeApp().run()
