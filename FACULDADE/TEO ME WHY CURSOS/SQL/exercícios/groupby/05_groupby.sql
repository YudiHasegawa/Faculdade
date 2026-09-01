-- Qual o valor médio de pontos positivos por dia?

SELECT  sum(QtdePontos) AS TotalPontos,
        count(DISTINCT substr(DtCriacao, 1, 10)) AS Dias,
        count(substr(Dtcriacao, 1, 10)) AS DiasRepetidos,
        sum(QtdePontos) / count(DISTINCT substr(Dtcriacao, 1, 10)) AS Média
FROM transacoes
WHERE QtdePontos > 0