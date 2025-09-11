import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

KV_FILE = "filmes.kv"

class CadastroScreen(Screen):
    def limpar_campos(self):
        self.ids.titulo_input.text = ""
        self.ids.genero_spinner.text = "Selecione o gênero"
        self.ids.ano_input.text = ""

class ListagemScreen(Screen):
    def on_pre_enter(self):
        self.populate_list()

    def populate_list(self):
        app = App.get_running_app()
        container = self.ids.lista_container
        container.clear_widgets()

        filmes = app.listar_filmes()
        if not filmes:
            container.add_widget(Label(text="Nenhum filme cadastrado.", size_hint_y=None, height=dp(40), halign="center", valign="middle", text_size=(self.width, None)))
            return

        for fid, titulo, genero, ano in filmes:
            row = BoxLayout(size_hint_y=None, height=dp(44), spacing=6)

            # Label centralizada
            lbl = Label(
                text=f"{titulo} ({ano}) — {genero}",
                size_hint_x=1,
                halign="center",
                valign="middle"
            )
            lbl.text_size = (lbl.width, None)
            row.add_widget(lbl)

            btn_edit = Button(text="Editar", size_hint_x=None, width=dp(90))
            btn_edit.bind(on_release=lambda btn, film_id=fid: app.abrir_edicao(film_id))
            row.add_widget(btn_edit)

            btn_del = Button(text="Excluir", size_hint_x=None, width=dp(90))
            btn_del.bind(on_release=lambda btn, film_id=fid: app.deletar_filme(film_id))
            row.add_widget(btn_del)

            container.add_widget(row)

class EdicaoScreen(Screen):
    def preencher_campos(self, film):
        self.ids.edit_titulo.text = film[1]
        self.ids.edit_genero.text = film[2]
        self.ids.edit_ano.text = str(film[3])

class FilmesApp(App):
    editing_id = None

    def build(self):
        self.conn = sqlite3.connect("banco_de_dados.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()
        return Builder.load_file(KV_FILE)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    # --- CRUD ---
    def adicionar_filme(self, titulo, genero, ano):
        if not titulo.strip() or not genero.strip() or not str(ano).strip():
            return
        try:
            ano_int = int(ano)
        except ValueError:
            return

        self.cursor.execute(
            "INSERT INTO filmes (titulo, genero, ano) VALUES (?, ?, ?)",
            (titulo.strip(), genero.strip(), ano_int)
        )
        self.conn.commit()

        self.root.get_screen('cadastro').limpar_campos()
        self.root.current = 'listagem'
        self.root.get_screen('listagem').populate_list()

    def listar_filmes(self):
        self.cursor.execute("SELECT id, titulo, genero, ano FROM filmes ORDER BY ano, titulo")
        return self.cursor.fetchall()

    def abrir_edicao(self, film_id):
        self.editing_id = film_id
        self.cursor.execute("SELECT id, titulo, genero, ano FROM filmes WHERE id = ?", (film_id,))
        film = self.cursor.fetchone()
        if film:
            self.root.get_screen('edicao').preencher_campos(film)
            self.root.current = 'edicao'

    def editar_filme(self, titulo, genero, ano):
        if self.editing_id is None:
            return
        try:
            ano_int = int(ano)
        except ValueError:
            return

        self.cursor.execute(
            "UPDATE filmes SET titulo = ?, genero = ?, ano = ? WHERE id = ?",
            (titulo.strip(), genero.strip(), ano_int, self.editing_id)
        )
        self.conn.commit()

        self.editing_id = None
        self.root.current = 'listagem'
        self.root.get_screen('listagem').populate_list()

    def deletar_filme(self, film_id):
        self.cursor.execute("DELETE FROM filmes WHERE id = ?", (film_id,))
        self.conn.commit()
        self.root.get_screen('listagem').populate_list()

    def on_stop(self):
        try:
            self.conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    FilmesApp().run()
