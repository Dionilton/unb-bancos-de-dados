from src.services.cadastro_perfil_service import CadastroPerfilService

class CadastroPerfilController:
    def __init__(self):
        self.cadastro_perfil_service = CadastroPerfilService()

    def cadastrar(self, **kwargs):
        if kwargs["matricula"] != None:
            self.cadastro_perfil_service.cadastarAluno(kwargs["matricula"], kwargs["curso"], kwargs["email"])
