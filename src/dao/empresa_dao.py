from database.connection import get_connection
from src.models.empresa import Empresa

class EmpresaDAO:
    def listar(self) -> list[Empresa]:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, nome
            FROM empresa
            ORDER BY nome
        """)

        empresas = [
            Empresa(
                id=row["id"],
                nome=row["nome"]
            )
            for row in cursor.fetchall()
        ]

        cursor.close()
        conn.close()

        return empresas