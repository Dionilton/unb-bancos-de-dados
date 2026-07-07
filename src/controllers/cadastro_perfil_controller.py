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
            case 'Servidor':
                self.cadastro_perfil_service.cadastrarServidor(kwargs["setor"], kwargs["email"])
            case 'Terceirizado':
                 self.cadastro_perfil_service.cadastrarEmpresa(kwargs["empresa"], kwargs['matricula_empresa'], kwargs["email"])
