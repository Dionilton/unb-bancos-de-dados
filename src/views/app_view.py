import customtkinter as ctk
from src.views.login_cadastro_view import LoginCadastroView
from src.views.login_view import LoginView

class AppView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Comunitário de Livros da UnB")
        self.geometry("800x600")

        self.current_frame = None

        self.show_tela_login_cadastro()

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_tela_login_cadastro(self):
        self.show_frame(LoginCadastroView)

    def show_login(self):
        self.show_frame(LoginView)