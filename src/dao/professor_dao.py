from database.connection import get_connection
from src.models.professor import Professor

class ProfessorDAO:
    def insert(self, professor: Professor) -> int:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO professor
            (id_usuario, departamento)
            VALUES(%s, %s)
        """
        
        valores = (
            professor.id_usuario,
            professor.departamento
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return professor.id_usuario