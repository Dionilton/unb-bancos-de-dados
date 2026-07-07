from database.connection import get_connection
from src.models.servidor import Servidor

class ServidorDAO:
    def insert(self, servidor: Servidor) -> int:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO servidor
            (id_usuario, setor)
            VALUES(%s, %s)
        """
        
        valores = (
            servidor.id_usuario,
            servidor.setor
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return servidor.id_usuario