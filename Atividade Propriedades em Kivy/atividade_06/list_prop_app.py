from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "list_prop.kv"))

class ListaItensWidget(BoxLayout):
    lista_de_compras = ListProperty(['Leite', 'Pão', 'Ovos'])

    def adicionar_item(self, item):
        item = item.strip()
        if item:
            self.lista_de_compras.append(item)

class ListPropApp(App):
    def build(self):
        return ListaItensWidget()

if __name__ == "__main__":
    ListPropApp().run()
