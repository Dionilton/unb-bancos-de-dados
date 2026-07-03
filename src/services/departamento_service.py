from src.dao.departamento_dao import DepartamentoDAO


class DepartamentoService:
    def __init__(self):
        self.departamento_dao = DepartamentoDAO()

    def listar(self):
        return self.departamento_dao.listar()