from database.connection import get_connection
from src.models.usuario import Usuario

class UsuarioDAO:
    
    def find_by_email(self, email: str) -> Usuario | None:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuario where email = %s",
            (email,)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado is None:
            return None
        
        return Usuario(
            id=resultado["id"],
            nome=resultado["nome"],
            dt_nascimento=resultado["dt_nascimento"],
            email=resultado["email"],
            senha_hash=resultado["senha_hash"],
            foto_documento=resultado["foto_documento"]
        )
    
    def insert(self, usuario: Usuario) -> int:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO usuario
            (nome, dt_nascimento, email, senha_hash, foto_documento)
            VALUES(%s, %s, %s, %s, %s)
        """

        valores = (
            usuario.nome,
            usuario.dt_nascimento,
            usuario.email,
            usuario.senha_hash,
            usuario.foto_documento
        )

        cursor.execute(sql, valores)
        conn.commit()

        id_gerado = cursor.lastrowid

        cursor.close()
        conn.close()

        return id_gerado