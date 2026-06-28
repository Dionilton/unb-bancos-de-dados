from src.services.cadastro_usuario_service import CadastroUsuarioService
from src.models.usuario import Usuario
from datetime import date

class CadastroUsuarioController:
    def __init__(self):
        self.cadastro_usuario_service = CadastroUsuarioService()

    def cadastrar(self, nome, dt_nascimento, email, senha, ft_documento):
        if not nome or not dt_nascimento or not email or not senha or not ft_documento:
            return "preencha todos os dados"
        
        usuario = Usuario(
            nome = nome,
            dt_nascimento = dt_nascimento,
            email = email,
            senha_hash = senha,
            foto_documento = ft_documento
        )

        return self.cadastro_usuario_service.cadastrar(usuario)