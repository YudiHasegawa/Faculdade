with tb_cliente_dia AS (
    SELECT  IdCliente,
            substr(DtCriacao, 1,10) AS DtDia,
            count(DISTINCT IdTransacao) AS QtdeTransacao
    FROM transacoes

    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    GROUP BY 1, 2
),

tb_lag AS (
    SELECT  *,
            sum(QtdeTransacao) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS QtAcum,
            lag(QtdeTransacao) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS lagTransacao
    FROM tb_cliente_dia
)

SELECT  *,
        100. *QtdeTransacao  / lagTransacao	 AS pct
FROM tb_lag