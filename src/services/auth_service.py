from src.dao.usuario_dao import UsuarioDAO
import bcrypt

class AuthService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def authenticate(self, email, senha):
        usuario = self.usuario_dao.find_by_email(email)

        if not usuario:
            return False
        
        return bcrypt.checkpw(
            senha.encode("utf-8"),
            usuario.senha_hash.encode("utf-8")
        )