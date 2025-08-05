import threading
import time
import random
import json
import os
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy_garden.graph import MeshLinePlot

KV_FILE = "ai_control.kv"


class AIControlPanel(BoxLayout):
    status_text = StringProperty("IA: Offline")
    threat_level = NumericProperty(0)
    ia_ativa = BooleanProperty(False)
    log_entries = ListProperty([])

    graph = None
    plot = None
    history = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Som de alerta (comente se não tiver o arquivo alerta.wav)
        self.sound_alert = SoundLoader.load("alerta.wav")

        # Inicializar gráfico depois da interface carregar
        Clock.schedule_once(self.init_graph, 1)

        self.history = []

        self.load_state()

        # Atualização passiva do nível de ameaça a cada 5 segundos
        Clock.schedule_interval(self.increase_threat_passive, 5)

        # Thread para eventos aleatórios
        self.stop_thread = False
        self.thread = threading.Thread(target=self.random_events_thread, daemon=True)
        self.thread.start()

    def init_graph(self, dt):
        self.graph = self.ids.threat_graph
        self.plot = MeshLinePlot(color=[0, 1, 1, 1])
        self.graph.add_plot(self.plot)
        self.update_graph()

    def toggle_ia(self):
        self.ia_ativa = not self.ia_ativa
        if self.ia_ativa:
            self.status_text = "IA: Online, aguardando comando..."
            self.add_log("IA ligada.")
        else:
            self.status_text = "IA: Offline"
            self.threat_level = 0
            self.add_log("IA desligada.")
            self.stop_animation()
        self.save_state()

    def execute_command(self, cmd):
        cmd = cmd.strip().lower()
        if not self.ia_ativa:
            self.status_text = "IA: Offline. Ligue a IA para enviar comandos."
            return
        if not cmd:
            self.status_text = "IA: Por favor, digite um comando."
            return

        resposta = ""
        if cmd == "capturar robô":
            resposta = "IA: Robô localizado e sendo rastreado."
            self.change_threat(15)
        elif cmd == "injetar_virus":
            resposta = "IA: Vírus injetado nos sistemas inimigos."
            self.change_threat(20)
        elif cmd == "desligar_sistemas":
            resposta = "IA: Todos os sistemas externos desligados."
            self.change_threat(-10)
        elif cmd == "acessar_dados":
            resposta = "IA: Acesso aos dados autorizado."
        elif cmd == "analisar":
            resposta = "IA: Sondas de diagnóstico lançadas."
            self.change_threat(5)
        elif cmd == "desconectar":
            self.toggle_ia()
            resposta = "IA: Desconectando do sistema."
        else:
            resposta = f"IA: Comando '{cmd}' não reconhecido."

        self.status_text = resposta
        self.add_log(f"Comando: {cmd}")
        self.add_log(f"Resposta: {resposta}")

        self.save_state()

    def add_log(self, msg):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.log_entries.append(f"{timestamp} {msg}")
        # Limitar o log para 100 entradas
        if len(self.log_entries) > 100:
            self.log_entries = self.log_entries[-100:]

    def increase_threat_passive(self, dt):
        if self.ia_ativa and self.threat_level < 100:
            self.change_threat(1)

    def change_threat(self, amount):
        new_level = self.threat_level + amount
        if new_level < 0:
            new_level = 0
        elif new_level > 100:
            new_level = 100
        self.threat_level = new_level
        self.add_log(f"Nível de ameaça ajustado para {self.threat_level}%")
        self.update_graph()
        self.check_threat()

    def check_threat(self):
        if self.threat_level >= 80:
            self.status_text = "IA: ALERTA! Nível de ameaça crítico!"
            self.animate_alert()
            if self.sound_alert:
                self.sound_alert.play()
        else:
            self.stop_animation()

    def animate_alert(self):
        if hasattr(self.ids, "threat_bar"):
            anim = Animation(background_color=(1, 0, 0, 1), duration=0.5) + Animation(background_color=(0.1, 0.1, 0.1, 1), duration=0.5)
            anim.repeat = True
            anim.start(self.ids.threat_bar)

    def stop_animation(self):
        if hasattr(self.ids, "threat_bar"):
            Animation.cancel_all(self.ids.threat_bar)
            self.ids.threat_bar.background_color = (0.1, 0.1, 0.1, 1)

    def update_graph(self):
        self.history.append(self.threat_level)
        if len(self.history) > 50:
            self.history.pop(0)
        if self.plot:
            self.plot.points = list(enumerate(self.history))

    def save_state(self):
        data = {
            "status_text": self.status_text,
            "threat_level": self.threat_level,
            "ia_ativa": self.ia_ativa,
            "log_entries": self.log_entries,
            "history": self.history
        }
        try:
            with open("ia_state.json", "w") as f:
                json.dump(data, f)
        except Exception as e:
            self.add_log(f"Erro ao salvar estado: {e}")

    def load_state(self):
        if os.path.exists("ia_state.json"):
            try:
                with open("ia_state.json", "r") as f:
                    data = json.load(f)
                    self.status_text = data.get("status_text", self.status_text)
                    self.threat_level = data.get("threat_level", self.threat_level)
                    self.ia_ativa = data.get("ia_ativa", self.ia_ativa)
                    self.log_entries = data.get("log_entries", [])
                    self.history = data.get("history", [])
            except Exception as e:
                print("Erro ao carregar estado:", e)

    def random_events_thread(self):
        while not self.stop_thread:
            if self.ia_ativa:
                # 10% chance de evento inesperado a cada 10 segundos
                if random.random() < 0.1:
                    self.add_random_event()
            time.sleep(10)

    @mainthread
    def add_random_event(self):
        eventos = [
            ("Pico súbito de ameaça detectado!", 15),
            ("Sistemas de defesa ativados, ameaças mitigadas.", -10),
            ("Nova vulnerabilidade detectada.", 10),
            ("Ataque externo em progresso!", 20),
            ("Análise completa, ameaça estabilizada.", -5)
        ]
        evento, delta = random.choice(eventos)
        self.add_log(f"Evento: {evento}")
        self.change_threat(delta)

    def on_stop(self):
        self.stop_thread = True


class AIControlApp(App):
    def build(self):
        Builder.load_file(KV_FILE)
        return AIControlPanel()

    def on_stop(self):
        # Para a thread ao fechar app
        self.root.stop_thread = True


if __name__ == "__main__":
    AIControlApp().run()
