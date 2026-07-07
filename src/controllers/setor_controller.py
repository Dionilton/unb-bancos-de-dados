from src.services.setor_service import SetorService

class SetorController:
    def __init__(self):
        self.service = SetorService()

    def listar(self):
        return self.service.listar()
    