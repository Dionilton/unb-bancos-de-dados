from database.connection import get_connection
from src.models.livro import Livro

class CatalogoDAO:
    def listar(self) -> list[Livro]:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute("""
            SELECT * from view_catalogo
        """)

        registros = cursor.fetchall()

        livros = []

        for livro in registros:
            livros.append(
                Livro(
                    catId=livro["catId"],
                    userId=livro["userId"],
                    nome=livro["nome"],
                    titulo=livro["titulo"],
                    descricao=livro["descricao"],
                    disponibilidade=livro["disponibilidade"]
                )
            )

        cursor.close()
        conn.close()
        
        return livros