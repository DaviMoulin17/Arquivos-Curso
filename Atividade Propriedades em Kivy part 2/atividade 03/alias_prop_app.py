from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, AliasProperty
from kivy.lang import Builder

class CalculatorWidget(BoxLayout):
    num1 = NumericProperty(10)
    num2 = NumericProperty(5)

    def _get_sum_result(self):
        return self.num1 + self.num2

    sum_result = AliasProperty(_get_sum_result, None, bind=('num1', 'num2'))

class AliasPropApp(App):
    def build(self):
        Builder.load_file("alias_prop.kv")
        return CalculatorWidget()

if __name__ == "__main__":
    AliasPropApp().run()
