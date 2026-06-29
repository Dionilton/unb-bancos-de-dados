from src.dao.curso_dao import CursoDAO


class CursoService:
    def __init__(self):
        self.curso_dao = CursoDAO()

    def listar(self):
        return self.curso_dao.listar()