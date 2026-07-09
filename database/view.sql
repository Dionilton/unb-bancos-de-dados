CREATE VIEW view_catalogo AS
SELECT
    c.id AS catId,
    u.id AS userId,
    u.nome AS nome,
    c.titulo AS titulo,
    cat.descricao AS descricao,
    c.disponibilidade AS disponibilidade
FROM catalogo c
INNER JOIN usuario u
    ON c.usuario_id = u.id
INNER JOIN categoria cat
    ON c.categoria_id = cat.id;