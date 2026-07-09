import customtkinter as ctk
from src.controllers.catalogo_controller import CatalogoController
from src.controllers.doacao_controller import DoacaoController

class AreaLogadaView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.catalogo_controller = CatalogoController()
        self.doacao_controller = DoacaoController()

        self.label_titulo = ctk.CTkLabel(self, text="Insira o título do livro:")
        self.label_titulo.pack(fill="both")
        self.entry_titulo = ctk.CTkEntry(self)
        self.entry_titulo.pack(fill="both")

        self.label_categoria = ctk.CTkLabel(self, text="Categoria:")
        self.label_categoria.pack()
        self.categoriaSelecionado = ctk.CTkComboBox(
            self,
            values=['doação', 'emprestimo', 'troca']
        )
        self.categoriaSelecionado.pack(fill="both")

        self.btn_cadastro_livro = ctk.CTkButton(
            self,
            text='Cadastrar Livro',
            command=lambda: self.cadastrar_livro(idUser = self.master.usuario_logado, titulo=self.entry_titulo.get())
        )
        self.btn_cadastro_livro.pack(pady=25)

        self.label_retorno_cadastro = ctk.CTkLabel(self, text="")
        self.label_retorno_cadastro.pack(fill="both")

        self.btn_consulta_catalogo = ctk.CTkButton(
            self,
            text='Atualizar Catalogo',
            command=self.atualizar_catalogo
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
                text="Obter Livro" if livro.userId != self.master.usuario_logado else "Meu Livro",
                fg_color="#b9394a" if livro.userId == self.master.usuario_logado else "#1b8529",
                width=120,
                command=lambda l=livro: self.doacao(
                    livro=l.catId,
                    usuario_a=l.userId,
                    usuario_b=self.master.usuario_logado
                ),
                state="disabled" if livro.userId == self.master.usuario_logado else "normal"
            )
            btn.pack(side="right", padx=10)

    def doacao(self, livro, usuario_a, usuario_b):
        self.doacao_controller.insert(livro, usuario_a, usuario_b)

    def cadastrar_livro(self, idUser, titulo):
        self.catalogo_controller.cadastrar_livro(idUser, titulo)
        self.label_retorno_cadastro.configure(text="livro cadastrado com sucesso")

    def atualizar_catalogo(self):
        for widget in self.lista_clientes.winfo_children():
            widget.destroy()

        self.carregar_catalogo()

