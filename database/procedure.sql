CREATE PROCEDURE registrar_historico(
    IN p_livro INT,
    IN p_acao INT,
    IN p_titulo VARCHAR(255),
    IN p_usuario_id INT,
    IN p_categoria_id INT,
    IN p_disponibilidade TINYINT
)
BEGIN

    INSERT INTO historico_catalogo (
        ts_acao,
        livro,
        acao,
        titulo,
        id_livro,
        nome_proprietario,
        id_proprietario,
        categoria,
        disponiblidade
    )
    SELECT
        NOW(),
        p_livro,
        p_acao,
        p_titulo,
        p_livro,
        u.nome,
        u.id,
        c.descricao,
        p_disponibilidade
    FROM usuario u
    JOIN categoria c
        ON c.id = p_categoria_id
    WHERE u.id = p_usuario_id;

END