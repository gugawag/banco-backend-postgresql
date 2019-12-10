-- Tabelas simples apenas para fins didaticos
CREATE TABLE TB_CONTA
(
    id     SERIAL PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    saldo  INTEGER     NOT NULL DEFAULT 0
);