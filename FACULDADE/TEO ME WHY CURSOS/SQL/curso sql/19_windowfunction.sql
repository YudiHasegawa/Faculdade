with tb_sumario_dias AS (
    SELECT  substr(DtCriacao, 1, 10) AS DtDia,
            count(IdTransacao) AS QtdeTransacao
    FROM transacoes

    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    GROUP BY 1
)

SELECT  *,
        sum(QtdeTransacao) OVER (ORDER BY DtDia) AS QtdeTransacaoAcum
FROM tb_sumario_dias