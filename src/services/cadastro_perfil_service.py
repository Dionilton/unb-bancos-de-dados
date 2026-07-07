from src.dao.usuario_dao import UsuarioDAO
from src.dao.aluno_dao import AlunoDAO
from src.dao.professor_dao import ProfessorDAO
from src.dao.servidor_dao import ServidorDAO
from src.dao.terceirizado_dao import TerceirizadoDAO
from src.models.aluno import Aluno
from src.models.professor import Professor
from src.models.servidor import Servidor
from src.models.terceirizado import Terceirizado

class CadastroPerfilService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()
        self.aluno_dao = AlunoDAO()
        self.professor_dao = ProfessorDAO()
        self.servidor_dao = ServidorDAO()
        self.terceirizado_dao = TerceirizadoDAO()

    def cadastarAluno(self, matricula, curso, email):
        usuario = self.usuario_dao.find_by_email(email)
        if usuario:
            aluno = Aluno(
                id_usuario = usuario.id,
                matricula = matricula,
                curso = curso
            )
            
            self.aluno_dao.insert(aluno)
    
    def cadastarProfessor(self, departamento, email):
        usuario = self.usuario_dao.find_by_email(email)
        if usuario:
            professor = Professor(
                id_usuario = usuario.id,
                departamento = departamento
            )

            self.professor_dao.insert(professor)

    def cadastrarServidor(self, setor, email):
        usuario = self.usuario_dao.find_by_email(email)
        if usuario:
            servidor = Servidor(
                id_usuario = usuario.id,
                setor = setor
            )

            self.servidor_dao.insert(servidor)

    def cadastrarEmpresa(self, empresa, matricula_empresa, email):
        usuario = self.usuario_dao.find_by_email(email)
        if usuario:
            terceirizado = Terceirizado(
                id_usuario = usuario.id,
                empresa = empresa,
                matricula_empresa = matricula_empresa
            )

            self.terceirizado_dao.insert(terceirizado)