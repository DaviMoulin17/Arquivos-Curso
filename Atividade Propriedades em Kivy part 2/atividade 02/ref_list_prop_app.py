from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.lang import Builder

# Carrega o conteúdo do arquivo KV externo
Builder.load_file("ref_list_prop.kv")

# Classe principal que representa o ponto móvel
class MovableDot(Widget):
    # Coordenada X inicial
    pos_x = NumericProperty(100)
    # Coordenada Y inicial
    pos_y = NumericProperty(100)

    # Agrupa pos_x e pos_y em uma única propriedade (como uma tupla)
    dot_pos = ReferenceListProperty(pos_x, pos_y)

    # Métodos que alteram as posições
    def move_left(self):
        self.pos_x -= 10  # Move 10 pixels para a esquerda

    def move_right(self):
        self.pos_x += 10  # Move 10 pixels para a direita

    def move_up(self):
        self.pos_y += 10  # Move 10 pixels para cima

    def move_down(self):
        self.pos_y -= 10  # Move 10 pixels para baixo

# Classe do App
class ReferenceListApp(App):
    def build(self):
        # Retorna o widget principal
        return MovableDot()

# Executa o app
if __name__ == '__main__':
    ReferenceListApp().run()
