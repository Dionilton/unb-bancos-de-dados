import customtkinter as ctk
from src.controllers.catalogo_controller import CatalogoController

class AreaLogadaView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.catalogo_controller = CatalogoController()

        self.btn_cadastro_livro = ctk.CTkButton(
            self,
            text='Cadastrar Livro',
            #command=self.navegar_para_cadastro_livro
        )
        self.btn_cadastro_livro.pack(pady=25)

        self.btn_consulta_catalogo = ctk.CTkButton(
            self,
            text='Atualizar Catalogo',
            #command=self.navegar_para_cadastro
        )
        self.btn_consulta_catalogo.pack(pady=25)

        self.lista_clientes = ctk.CTkFrame(self)
        self.lista_clientes.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.carregar_catalogo()

    def buscar_livros(self):
        return self.catalogo_controller.listar()

    def carregar_catalogo(self):
        livros = self.buscar_livros()

        for livro in livros:
            

            item = ctk.CTkFrame(
                self.lista_clientes
            )

            item.pack(
                fill="x",
                pady=5
            )

            id = ctk.CTkLabel(
                item,
                text=livro.catId
            )
            id.pack(
                side="left",
                padx=10
            )

            nome = ctk.CTkLabel(
                item,
                text=livro.nome
            )
            nome.pack(
                side="left",
                padx=10
            )

            titulo = ctk.CTkLabel(
                item,
                text=livro.titulo
            )
            titulo.pack(
                side="left",
                padx=10
            )

            descicao = ctk.CTkLabel(
                item,
                text=livro.descricao
            )
            descicao.pack(
                side="left",
                padx=10
            )

            disponibilidade = ctk.CTkLabel(
                item,
                text='disponível' if livro.disponibilidade == 1 else 'indisponível'
            )
            disponibilidade.pack(
                side="left",
                padx=10
            )

            btn = ctk.CTkButton(
                item,
                text="Obter Livro" if livro.userId != self.master.usuario_logado else 'Meu Livro',
                fg_color= "#b9394a" if livro.userId == self.master.usuario_logado else "#1b8529",
                width=120,
                command= self.doacao,
                state = 'disable' if livro.userId == self.master.usuario_logado else 'normal'
            )
            btn.pack(side="right", padx=10)

    def doacao(self):
        print(self.master.usuario_logado)

