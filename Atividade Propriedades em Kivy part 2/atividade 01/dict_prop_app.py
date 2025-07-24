from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty
from kivy.lang import Builder

# Carrega o layout visual
Builder.load_file('dict_prop.kv')

class UserProfileWidget(BoxLayout):
    # Propriedade do tipo dicionário
    user_data = DictProperty({
        'name': 'João',
        'age': 30,
        'city': 'São Paulo'
    })

    def update_age(self):
        # Incrementa a idade
        self.user_data['age'] += 1
        print(f"Nova idade: {self.user_data['age']}")  # Debug: para verificar no terminal
        # Força o Kivy a atualizar os bindings
        self.user_data = self.user_data.copy()

class DictPropApp(App):
    def build(self):
        return UserProfileWidget()

if __name__ == '__main__':
    DictPropApp().run()
