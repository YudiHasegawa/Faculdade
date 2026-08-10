-- Selecione todos os clientes com email cadastrado
SELECT idCliente, flEmail
FROM clientes
WHERE flEmail = 1;

-- Selecione todas as transações de 50 pontos (exatos)
SELECT IdCliente, IdTransacao, QtdePontos
FROM transacoes
WHERE qtdePontos = 50;

-- Selecione todos clientes com mais de 500 pontos
SELECT idCliente, qtdePontos
FROM clientes
WHERE qtdePontos > 500;

-- Selecione produtos que contêm 'churn' no nome

-- Jeito noob loser porco podre iniciante
SELECT *
FROM produtos

WHERE DescNomeProduto = 'Churn_10pp'
OR DescNomeProduto = 'Churn_2pp'
OR DescNomeProduto = 'Churn_5pp';

-- Jeito aura + ego
SELECT *
FROM produtos

WHERE DescNomeProduto IN ('Churn_10pp', 'Churn_2pp', 'Churn_5pp');

-- Jeito hacker aura + ego 67 pro max 3000
SELECT *
FROM produtos

WHERE DescNomeProduto LIKE 'Churn%';

-- Jeito hacker aura + ego 67 pro max 3000 DELUXE FINAL 2.0
SELECT *
FROM produtos

WHERE DescCategoriaProduto LIKE 'churn_model';