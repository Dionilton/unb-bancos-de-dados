from database.connection import get_connection


class DoacaoDAO:
    def cadastrar(self, livro, usuario_a, usuario_b):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO doacao
            (livro, usuario_a, usuario_b, dt_doacao)
            VALUES(%s, %s, %s, NOW())
        """

        valores = (
            livro,
            usuario_a,
            usuario_b
        )

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        