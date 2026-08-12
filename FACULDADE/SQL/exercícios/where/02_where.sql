-- Selecione todas as transações de 50 pontos (exatos)
SELECT IdCliente, IdTransacao, QtdePontos
FROM transacoes
WHERE qtdePontos = 50;