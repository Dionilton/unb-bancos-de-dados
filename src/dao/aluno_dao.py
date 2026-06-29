from database.connection import get_connection
from src.models.aluno import Aluno

class AlunoDAO:
    def insert(self, aluno: Aluno) -> int:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO aluno
            (id_usuario, matricula, curso)
            VALUES(%s, %s, %s)
        """

        valores = (
            aluno.id_usuario,
            aluno.matricula,
            aluno.curso
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return aluno.id_usuario