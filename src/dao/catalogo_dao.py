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
    
    def cadastrar(self, idUser, titulo):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO catalogo
            (usuario_id, categoria_id, titulo, disponibilidade)
            VALUES(%s, %s, %s, %s)
        """

        valores = (
            idUser,
            1,
            titulo,
            1
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    def atualizar_proprietario(self, id_livro, novo_usuario):

        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE catalogo
            SET usuario_id = %s
            WHERE id = %s
        """

        cursor.execute(sql, (novo_usuario, id_livro))


        conn.commit()

        cursor.close()
        conn.close()