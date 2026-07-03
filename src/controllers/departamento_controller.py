from src.services.departamento_service import DepartamentoService

class DepartamentoController:
    def __init__(self):
        self.service = DepartamentoService()

    def listar(self):
        return self.service.listar()