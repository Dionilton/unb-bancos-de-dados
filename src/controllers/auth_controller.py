from src.services.auth_service import AuthService

class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def login(self, email, senha):
        if not email or not senha:
            return False
        return self.auth_service.authenticate(email, senha)