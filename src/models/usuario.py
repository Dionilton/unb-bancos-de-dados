from dataclasses import dataclass
from datetime import date

@dataclass
class Usuario:
    nome: str
    dt_nascimento: date
    email: str
    senha_hash: str
    foto_documento: bytes
    id: int | None = None