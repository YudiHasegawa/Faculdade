SELECT  SUM(QtdePontos) AS QtdePontos,

        SUM(CASE
            WHEN QtdePontos > 0 THEN QtdePontos
        END) AS PontosPositivos,

        SUM(CASE 
            WHEN QtdePontos < 0 THEN QtdePontos
        END) AS PontosNegativos,
        COUNT(CASE 
            WHEN QtdePontos < 0 THEN QtdePontos
        END) AS TransacoesNegativas
FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'