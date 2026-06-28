from src.dao.usuario_dao import UsuarioDAO
import bcrypt

class CadastroUsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def cadastrar(self, usuario):
        existeUsuario = self.usuario_dao.find_by_email(usuario.email)
        if existeUsuario != None:
            return "email já cadastrado"
        
        senha = usuario.senha_hash
        senha_hash = bcrypt.hashpw(
            senha.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        usuario.senha_hash = senha_hash

        self.usuario_dao.insert(usuario)
        return "usuário cadastrado com sucesso"