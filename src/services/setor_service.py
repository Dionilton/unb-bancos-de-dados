from src.dao.setor_dao import SetorDAO


class SetorService:
    def __init__(self):
        self.setor_dao = SetorDAO()

    def listar(self):
        return self.setor_dao.listar()