from dataclasses import dataclass

@dataclass
class Catalogo:
    id: int
    usuario_id: int
    categoria_id: int
    titulo: str
    disponibilidade: int