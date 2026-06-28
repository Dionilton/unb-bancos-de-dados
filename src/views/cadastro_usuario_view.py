import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import filedialog
from PIL import Image
from src.controllers.cadastro_usuario_controller import CadastroUsuarioController

class CadastroUsuarioView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.cadastro_usuario_controller = CadastroUsuarioController()
        

        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.pack()

        self.label_dt_nascimento = ctk.CTkLabel(self, text="Data de nascimento (selecione)")
        self.label_dt_nascimento.pack()
        self.data = DateEntry(
            self,
            date_pattern="dd/MM/yyyy",
            width=15
        )
        self.data.pack(pady=5)

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack()
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.pack()

        self.label_pass = ctk.CTkLabel(self, text="Senha:")
        self.label_pass.pack()
        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.pack()

        self.caminho_imagem = None

        self.label_imagem_documento = ctk.CTkLabel(self, text="Documento de Identificação:")
        self.label_imagem_documento.pack()

        self.btnSelecionaImagem = ctk.CTkButton(
            self,
            text="Selecione uma imagem",
            command=self.selecionar_imagem
        )
        self.btnSelecionaImagem.pack()
        

    def selecionar_imagem(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.gif"),
                ("Todos os arquivos", "*.*")
            ]
        )

        with open(arquivo, "rb") as f:
            self.foto = f.read()

        if arquivo:
            self.caminho_imagem = arquivo
            print("Imagem selecionada: ", arquivo)

            self.label_imagem = ctk.CTkLabel(self, text="")
            self.label_imagem.pack(pady=20)

            imagem = ctk.CTkImage(
                light_image=Image.open(arquivo),
                dark_image=Image.open(arquivo),
                size=(300, 300)
            )

            self.label_imagem.configure(image=imagem, text="")
            self.label_imagem.image = imagem

            self.btnCadastrar = ctk.CTkButton(
                self,
                text="CADASTRAR",
                fg_color="#E68E0A",
                command=self.cadastrar
            )
            self.btnCadastrar.pack(pady=50)

            self.label_retorno = ctk.CTkLabel(self, text="")
            self.label_retorno.pack()

    def cadastrar(self):
        retorno = self.cadastro_usuario_controller.cadastrar(
            self.entry_nome.get(),
            self.data.get_date(),
            self.entry_email.get(),
            self.entry_pass.get(),
            self.foto
        )
        self.label_retorno.configure(text=retorno)

        if retorno == "usuário cadastrado com sucesso":
            self.btnLogin = ctk.CTkButton(
                self,
                text="FAZER LOGIN",
                fg_color="#4009C0",
                command=self.navegar_para_login
            )
            self.btnLogin.pack(pady=14)
    def navegar_para_login(self):
        self.master.show_login()
        

