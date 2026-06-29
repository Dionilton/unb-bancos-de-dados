CREATE TABLE usuario (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  dt_nascimento DATE NOT NULL,
  email VARCHAR(255) NOT NULL,
  senha_hash VARCHAR(255) NOT NULL,
  foto_documento MEDIUMBLOB NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE categoria (
  id INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE acao (
  id INT NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE catalogo (
  id INT NOT NULL AUTO_INCREMENT,
  usuario_id INT NOT NULL,
  categoria_id INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  disponibilidade TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE troca (
  id INT NOT NULL AUTO_INCREMENT,
  livro_a INT NOT NULL,
  livro_b INT NOT NULL,
  dt_troca DATE NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE doacao (
  id INT NOT NULL AUTO_INCREMENT,
  livro INT NOT NULL,
  usuario_a INT NOT NULL,
  usuario_b INT NOT NULL,
  dt_doacao DATE NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE emprestimo (
  id INT NOT NULL AUTO_INCREMENT,
  livro INT NOT NULL,
  usuario_a INT NOT NULL,
  usuario_b INT NOT NULL,
  dt_emprestimo DATE NOT NULL,
  dt_devolucao DATE NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE aluno (
  id_usuario INT NOT NULL,
  matricula INT NOT NULL,
  curso INT NOT NULL,
  PRIMARY KEY (id_usuario)
) ENGINE=InnoDB;

CREATE TABLE professor (
  id_usuario INT NOT NULL,
  departamento INT NOT NULL,
  PRIMARY KEY (id_usuario)
) ENGINE=InnoDB;

CREATE TABLE servidor (
  id_usuario INT NOT NULL,
  setor INT NOT NULL,
  PRIMARY KEY (id_usuario)
) ENGINE=InnoDB;

CREATE TABLE terceirizado (
  id_usuario INT NOT NULL,
  empresa INT NOT NULL,
  matricula_empresa INT NOT NULL,
  PRIMARY KEY (id_usuario)
) ENGINE=InnoDB;

CREATE TABLE historico_catalogo (
  ts_acao TIMESTAMP NOT NULL,
  livro INT NOT NULL,
  acao INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  id_livro INT NOT NULL,
  nome_proprietario VARCHAR(100) NOT NULL,
  id_proprietario INT NOT NULL,
  categoria VARCHAR(45) NOT NULL,
  disponiblidade TINYINT NOT NULL,
  PRIMARY KEY (ts_acao, livro, acao)
) ENGINE=InnoDB;

CREATE TABLE curso (
  id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE departamento (
  id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE setor (
  id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE empresa (
  id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

ALTER TABLE catalogo
ADD CONSTRAINT fk_catalogo_usuario
FOREIGN KEY (usuario_id) REFERENCES usuario(id);

ALTER TABLE catalogo
ADD CONSTRAINT fk_catalogo_categoria
FOREIGN KEY (categoria_id) REFERENCES categoria(id);

ALTER TABLE troca
ADD CONSTRAINT fk_troca_livro_a
FOREIGN KEY (livro_a) REFERENCES catalogo(id);

ALTER TABLE troca
ADD CONSTRAINT fk_troca_livro_b
FOREIGN KEY (livro_b) REFERENCES catalogo(id);

ALTER TABLE doacao
ADD CONSTRAINT fk_doacao_livro
FOREIGN KEY (livro) REFERENCES catalogo(id);

ALTER TABLE doacao
ADD CONSTRAINT fk_doacao_usuario_a
FOREIGN KEY (usuario_a) REFERENCES usuario(id);

ALTER TABLE doacao
ADD CONSTRAINT fk_doacao_usuario_b
FOREIGN KEY (usuario_b) REFERENCES usuario(id);

ALTER TABLE emprestimo
ADD CONSTRAINT fk_emprestimo_livro
FOREIGN KEY (livro) REFERENCES catalogo(id);

ALTER TABLE emprestimo
ADD CONSTRAINT fk_emprestimo_usuario_a
FOREIGN KEY (usuario_a) REFERENCES usuario(id);

ALTER TABLE emprestimo
ADD CONSTRAINT fk_emprestimo_usuario_b
FOREIGN KEY (usuario_b) REFERENCES usuario(id);

ALTER TABLE aluno
ADD CONSTRAINT fk_aluno_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(id);

ALTER TABLE aluno
ADD CONSTRAINT fk_aluno_curso
FOREIGN KEY (curso) REFERENCES curso(id);

ALTER TABLE professor
ADD CONSTRAINT fk_professor_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(id);

ALTER TABLE professor
ADD CONSTRAINT fk_professor_departamento
FOREIGN KEY (departamento) REFERENCES departamento(id);

ALTER TABLE servidor
ADD CONSTRAINT fk_servidor_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(id);

ALTER TABLE servidor
ADD CONSTRAINT fk_servidor_setor
FOREIGN KEY (setor) REFERENCES setor(id);

ALTER TABLE terceirizado
ADD CONSTRAINT fk_terceirizado_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(id);

ALTER TABLE terceirizado
ADD CONSTRAINT fk_terceirizado_empresa
FOREIGN KEY (empresa) REFERENCES empresa(id);

ALTER TABLE historico_catalogo
ADD CONSTRAINT fk_historico_acao
FOREIGN KEY (acao) REFERENCES acao(id);
