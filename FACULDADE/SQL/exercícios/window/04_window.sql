-- Saldo de pontos acumulado de cada usuário
WITH tb_cliente AS (
    SELECT  DISTINCT IdCliente,
            substr(DtCriacao, 1,10) AS DtDia,
            sum(QtdePontos) AS TotalPontos
    FROM transacoes
    GROUP BY 1, 2
),

tb_saldopontos AS (
    SELECT  *,
            sum(TotalPontos) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS SaldoPontos
    FROM tb_cliente
)

SELECT * FROM tb_saldopontos