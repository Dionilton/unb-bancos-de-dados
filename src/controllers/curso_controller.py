from src.services.curso_service import CursoService


class CursoController:
    def __init__(self):
        self.service = CursoService()

    def listar(self):
        return self.service.listar()