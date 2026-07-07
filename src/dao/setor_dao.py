from database.connection import get_connection
from src.models.setor import Setor

class SetorDAO:
    def listar(self) -> list[Setor]:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, nome
            FROM setor
            ORDER BY nome
        """)

        setores = [
            Setor(
                id=row["id"],
                nome=row["nome"]
            )
            for row in cursor.fetchall()
        ]

        cursor.close()
        conn.close()

        return setores