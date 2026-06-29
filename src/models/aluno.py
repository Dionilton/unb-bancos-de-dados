from dataclasses import dataclass

@dataclass
class Aluno:
    id_usuario: int
    matricula: int
    curso: str