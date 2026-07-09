from dataclasses import dataclass

@dataclass
class Livro:
    catId: int
    userId: int
    nome: str
    titulo: str
    descricao: str
    disponibilidade: int