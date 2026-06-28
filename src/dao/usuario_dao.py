from database.connection import get_connection

class UsuarioDAO:
    
    def find_by_email(self, email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuario where email = %s",
            (email,)
        )

        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        return usuario