from src.services.empresa_service import EmpresaService

class EmpresaController:
    def __init__(self):
        self.service = EmpresaService()

    def listar(self):
        return self.service.listar()
    