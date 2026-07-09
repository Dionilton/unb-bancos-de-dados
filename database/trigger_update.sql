CREATE TRIGGER trg_catalogo_update
AFTER UPDATE
ON catalogo
FOR EACH ROW
BEGIN

    CALL registrar_historico(
        NEW.id,
        2,
        NEW.titulo,
        NEW.usuario_id,
        NEW.categoria_id,
        NEW.disponibilidade
    );

END