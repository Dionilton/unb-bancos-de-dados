import customtkinter as ctk
from src.controllers.auth_controller import AuthController

class LoginView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.auth_controller = AuthController()

        self.label_user = ctk.CTkLabel(self, text="Usuário")
        self.label_user.pack()

        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.pack()

        self.label_pass = ctk.CTkLabel(self, text="Senha")
        self.label_pass.pack()

        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.pack()

        self.btn_login = ctk.CTkButton(
            self,
            text="Entrar",
            command=self.login
        )
        self.btn_login.pack()

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack()

    def login(self):
        email = self.entry_user.get()
        senha = self.entry_pass.get()

        result = self.auth_controller.login(email, senha)

        if result:
            self.label_msg.configure(text="Login OK")
        else:
            self.label_msg.configure(text="Erro no login")