CREATE TRIGGER trg_catalogo_insert
AFTER INSERT
ON catalogo
FOR EACH ROW
BEGIN

    CALL registrar_historico(
        NEW.id,
        1,
        NEW.titulo,
        NEW.usuario_id,
        NEW.categoria_id,
        NEW.disponibilidade
    );

END