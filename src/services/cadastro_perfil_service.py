from src.dao.usuario_dao import UsuarioDAO
from src.dao.aluno_dao import AlunoDAO
from src.models.aluno import Aluno

class CadastroPerfilService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()
        self.aluno_dao = AlunoDAO()

    def cadastarAluno(self, matricula, curso, email):
        usuario = self.usuario_dao.find_by_email(email)
        if usuario:
            aluno = Aluno(
                id_usuario = usuario.id,
                matricula = matricula,
                curso = curso
            )
            
            self.aluno_dao.insert(aluno)