from src.dao.catalogo_dao import CatalogoDAO

class CatalogoController:
    def __init__(self):
         self.catalogo_dao = CatalogoDAO()

    def listar(self):
        return self.catalogo_dao.listar()