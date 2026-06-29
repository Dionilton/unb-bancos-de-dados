from database.connection import get_connection
from src.models.curso import Curso

class CursoDAO:
    def listar(self) -> list[Curso]:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, nome
            FROM curso
            ORDER BY nome  
        """)

        cursos = [
            Curso(
                id=row["id"],
                nome=row["nome"]
            )
            for row in cursor.fetchall()
        ]

        cursor.close()
        conn.close()

        return cursos