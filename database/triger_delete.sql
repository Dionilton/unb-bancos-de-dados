CREATE TRIGGER trg_catalogo_delete
AFTER DELETE
ON catalogo
FOR EACH ROW
BEGIN

    CALL registrar_historico(
        OLD.id,
        3,
        OLD.titulo,
        OLD.usuario_id,
        OLD.categoria_id,
        OLD.disponibilidade
    );

END