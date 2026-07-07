from database.connection import get_connection
from src.models.terceirizado import Terceirizado

class TerceirizadoDAO:
    def insert(self, terceirizado: Terceirizado) -> int:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO terceirizado
            (id_usuario, empresa, matricula_empresa)
            VALUES(%s, %s, %s)
        """
        
        valores = (
            terceirizado.id_usuario,
            terceirizado.empresa,
            terceirizado.matricula_empresa
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return terceirizado.id_usuario