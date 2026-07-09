from src.dao.doacao_dao import DoacaoDAO
from src.dao.catalogo_dao import CatalogoDAO

class DoacaoController:
    def __init__(self):
        self.doacao_dao = DoacaoDAO()
        self.catalogo_dao =  CatalogoDAO()

    def insert(self, livro, usuario_a, usuario_b):
        self.doacao_dao.cadastrar(livro, usuario_a, usuario_b)
        self.catalogo_dao.atualizar_proprietario(livro, usuario_b)