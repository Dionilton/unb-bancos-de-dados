from database.connection import get_connection
from src.models.departamento import Departamento

class DepartamentoDAO:
    def listar(self) -> list[Departamento]:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, nome
            FROM departamento
            ORDER BY nome
        """)

        departamentos = [
            Departamento(
                id=row["id"],
                nome=row["nome"]
            )
            for row in cursor.fetchall()
        ]

        cursor.close()
        conn.close()

        return departamentos