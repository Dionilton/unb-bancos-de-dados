from src.dao.empresa_dao import EmpresaDAO


class EmpresaService:
    def __init__(self):
        self.empresa_dao = EmpresaDAO()

    def listar(self):
        return self.empresa_dao.listar()