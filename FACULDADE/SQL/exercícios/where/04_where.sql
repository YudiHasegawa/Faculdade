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