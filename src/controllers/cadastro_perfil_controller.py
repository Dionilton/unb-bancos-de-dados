from src.services.cadastro_perfil_service import CadastroPerfilService

class CadastroPerfilController:
    def __init__(self):
        self.cadastro_perfil_service = CadastroPerfilService()

    def cadastrar(self, **kwargs):

        match kwargs["perfil"]:
            case 'Aluno':
                self.cadastro_perfil_service.cadastarAluno(kwargs["matricula"], kwargs["curso"], kwargs["email"])
        
            case 'Professor':
                self.cadastro_perfil_service.cadastarProfessor(kwargs["departamento"], kwargs["email"])
