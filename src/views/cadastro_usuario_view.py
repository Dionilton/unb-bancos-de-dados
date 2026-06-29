import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import filedialog
from PIL import Image
from src.controllers.cadastro_usuario_controller import CadastroUsuarioController
from src.controllers.cadastro_perfil_controller import CadastroPerfilController
from src.controllers.curso_controller import CursoController

class CadastroUsuarioView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.cadastro_usuario_controller = CadastroUsuarioController()
        self.cadastro_perfil_controller = CadastroPerfilController()

        self.curso_controller = CursoController()
        self.lista_cursos = self.curso_controller.listar()

        self.cursos_por_nome = {
            curso.nome: curso.id
            for curso in self.lista_cursos
        }


        
        self.label_perfil = ctk.CTkLabel(self, text="Selecione seu perfil:")
        self.label_perfil.pack(fill="both")
        
        self.perfil = ctk.CTkComboBox(
            self,
            values=["Aluno", "Professor", "Servidor", "Terceirizado"]
        )
        self.perfil.pack(fill="both")


        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(fill="both")
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.pack(fill="both")

        self.label_dt_nascimento = ctk.CTkLabel(self, text="Data de nascimento (selecione)")
        self.label_dt_nascimento.pack(fill="both")
        self.data = DateEntry(
            self,
            date_pattern="dd/MM/yyyy",
            width=15
        )
        self.data.pack(fill="both")

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(fill="both")
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.pack(fill="both")

        self.label_pass = ctk.CTkLabel(self, text="Senha:")
        self.label_pass.pack(fill="both")
        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.pack(fill="both")

        self.caminho_imagem = None

        self.label_imagem_documento = ctk.CTkLabel(self, text="Documento de Identificação:")
        self.label_imagem_documento.pack(fill="both")

        self.btnSelecionaImagem = ctk.CTkButton(
            self,
            text="Selecione uma imagem",
            command=self.selecionar_imagem
        )
        self.btnSelecionaImagem.pack(fill="both")

        

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
            self.label_imagem.pack(fill="both")

            imagem = ctk.CTkImage(
                light_image=Image.open(arquivo),
                dark_image=Image.open(arquivo),
                size=(200, 200)
            )

            self.label_imagem.configure(image=imagem, text="")
            self.label_imagem.image = imagem

            self.btnCadastrar = ctk.CTkButton(
                self,
                text="CONFIRMAR DADOS",
                fg_color="#E68E0A",
                command=self.cadastrar
            )
            self.btnCadastrar.pack(fill="both")

            self.label_retorno = ctk.CTkLabel(self, text="")

    def cadastrar(self):
        retorno = self.cadastro_usuario_controller.cadastrar(
            self.entry_nome.get(),
            self.data.get_date(),
            self.entry_email.get(),
            self.entry_pass.get(),
            self.foto
        )
        if retorno != "usuário cadastrado com sucesso":
            self.label_retorno.pack(fill="both")
            self.label_retorno.configure(text=retorno)

        selecao = self.perfil.get()
        if retorno == "usuário cadastrado com sucesso":
            self.label_retorno.pack_forget()

            self.entry_nome.configure(state="disabled")
            self.entry_email.configure(state="disabled")
            self.label_dt_nascimento.configure(state="disabled")
            self.label_pass.configure(state="disabled")
            self.btnSelecionaImagem.configure(state="disabled")
            self.btnCadastrar.configure(state="disabled")
            self.perfil.configure(state="disabled")    

            self.completarCadastro = ctk.CTkLabel(self, text="Dados conmfirmados, complete seu cadastro")
            self.completarCadastro.pack(fill="both")

            match selecao:
                case "Aluno":
                    self.label_matricula = ctk.CTkLabel(self, text="Matrícula:")
                    self.label_matricula.pack(fill="both")
                    self.entry_matricula = ctk.CTkEntry(self)
                    self.entry_matricula.pack(fill="both")

                    self.label_cursos = ctk.CTkLabel(self, text="Curso:")
                    self.label_cursos.pack()
                    self.cursosSelecionado = ctk.CTkComboBox(
                        self,
                        values=[curso.nome for curso in self.lista_cursos]
                    )
                    self.cursosSelecionado.pack(fill="both")

                    self.btnFinalizar = ctk.CTkButton(
                        self,
                        text = "FINALIZAR CADASTRO",
                        command = lambda: self.finalizar_cadastro(matricula = int(self.entry_matricula.get()), curso = self.cursos_por_nome[self.cursosSelecionado.get()], email = self.entry_email.get())
                    )
                    self.btnFinalizar.pack(fill="both")
                case "Professor":
                    print("show campos professor")
                case "Servidor":
                    print("show campos servidor")
                case "Terceirizado":
                    print("show campos terceirizado")

            
    def navegar_para_login(self):
        self.master.show_login()

    def finalizar_cadastro(self, **kwargs):
        self.cadastro_perfil_controller.cadastrar(**kwargs)
        self.label_Fim = ctk.CTkLabel(self, text="Cadastro finalizado com sucesso")
        self.label_Fim.pack(fill="both")

        self.btnFinalizar.configure(state="disabled")

        self.btnLogin = ctk.CTkButton(
            self,
            text="FAZER LOGIN",
            fg_color="#4009C0",
            command=self.navegar_para_login
        )
        self.btnLogin.pack(fill="both")

