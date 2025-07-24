from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.event import EventDispatcher

class GlobalState(EventDispatcher):
    current_status = StringProperty("Nenhum status definido")

class StatusDisplayWidget(BoxLayout):
    global_state_obj = ObjectProperty()

class StatusChangerWidget(BoxLayout):
    global_state_obj = ObjectProperty()

    def change_status(self):
        self.global_state_obj.current_status = self.ids.input_status.text

class EventCommApp(App):
    def build(self):
        self.global_state = GlobalState()
        root = BoxLayout(orientation='vertical')
        from kivy.lang import Builder
        Builder.load_file('event_comm.kv')

        self.status_display = StatusDisplayWidget(global_state_obj=self.global_state)
        self.status_changer = StatusChangerWidget(global_state_obj=self.global_state)

        root.add_widget(self.status_display)
        root.add_widget(self.status_changer)

        return root

if __name__ == '__main__':
    EventCommApp().run()
