from dataclasses import dataclass

@dataclass
class Livro:
    id: int
    nome: str
    titulo: str
    descricao: str
    disponibilidade: int