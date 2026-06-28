import customtkinter as ctk
#from src.controllers.login_castro_controller import LoginCadastroController

class LoginCadastroView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        #self.login_castro_controller = LoginCadastroController()


        self.btn_login = ctk.CTkButton(
            self,
            text='FAZER LOGIN',
            command=self.navegar_para_login
        )
        self.btn_login.pack(pady=25)

        self.btn_cadastro = ctk.CTkButton(
            self,
            text='FAZER CADASTRO',
            command=self.navegar_para_cadastro
        )
        self.btn_cadastro.pack(pady=25)

    def navegar_para_login(self):
        self.master.show_login()
        
    def navegar_para_cadastro(self):
        self.master.show_cadastro_usuario()