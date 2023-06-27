CREATE DATABASE posto

CREATE TABLE combustivel(
combustivel_id INT PRIMARY KEY IDENTITY NOT NULL,
nome_combustivel VARCHAR(40) NOT NULL,
estoque FLOAT UNIQUE NOT NULL,
preco_venda FLOAT NOT NULL,
preco_compra FLOAT NOT NULL,
fornecedor_id INT NOT NULL,
);

ALTER TABLE combustivel
	ADD CONSTRAINT fk_fornecedor FOREIGN KEY (fornecedor_id) REFERENCES fornecedor (fornecedor_id);

CREATE TABLE fornecedor (
fornecedor_id INT PRIMARY KEY IDENTITY NOT NULL,
nome_fornecedor VARCHAR(45) NOT NULL,
CNPJ varchar(45) NOT NULL
);

CREATE TABLE funcionario(
funcionario_id INT PRIMARY KEY IDENTITY NOT NULL,
nome_funcionario VARCHAR(75) NOT NULL,
CPF VARCHAR(45) NOT NULL,
);

CREATE TABLE bomba(
bomba_id INT PRIMARY KEY IDENTITY NOT NULL,
combustivel_id INT NOT NULL,
);

ALTER TABLE bomba
	ADD CONSTRAINT fk_combustivel FOREIGN KEY (combustivel_id) REFERENCES combustivel (combustivel_id);

CREATE TABLE abertura_bomba(
abertura_bomba_id INT PRIMARY KEY IDENTITY NOT NULL,
bomba_id INT NOT NULL,
funcionario_id INT NOT NULL,
valor_venda FLOAT NOT NULL,
);

ALTER TABLE abertura_bomba
	ADD CONSTRAINT fk_bomba FOREIGN KEY (bomba_id) REFERENCES bomba (bomba_id);

ALTER TABLE abertura_bomba
	ADD CONSTRAINT fk_funcionario FOREIGN KEY (funcionario_id) REFERENCES funcionario (funcionario_id);

CREATE TABLE venda(
venda_id INT PRIMARY KEY IDENTITY NOT NULL,
bomba_id INT NOT NULL,
combustivel_id INT NOT NULL,
quantidade_venda FLOAT NOT NULL,
estoque FLOAT,
);

ALTER TABLE venda
	ADD CONSTRAINT fk_estoque_1 FOREIGN KEY (estoque) REFERENCES combustivel (estoque);

ALTER TABLE venda
	ADD CONSTRAINT fk_bomba_1 FOREIGN KEY (bomba_id) REFERENCES bomba (bomba_id);

ALTER TABLE venda
	ADD CONSTRAINT fk_combustivel_1 FOREIGN KEY (combustivel_id) REFERENCES combustivel (combustivel_id);

CREATE TABLE abastecimento(
abastecimento_id INT PRIMARY KEY IDENTITY NOT NULL,
combustivel_id INT NOT NULL,
quantidade_abastecimento FLOAT NOT NULL,
estoque FLOAT,
);

ALTER TABLE abastecimento
	ADD CONSTRAINT fk_estoque_2 FOREIGN KEY (estoque) REFERENCES combustivel (estoque);

ALTER TABLE abastecimento
	ADD CONSTRAINT fk_combustivel_2 FOREIGN KEY (combustivel_id) REFERENCES combustivel (combustivel_id);



DROP TABLE combustivel;
DROP TABLE fornecedor;
DROP TABLE bomba;
DROP TABLE abertura_bomba;
DROP TABLE abastecimento;
DROP TABLE venda;
DROP TABLE funcionario;
