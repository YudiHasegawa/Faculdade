-- Como foi a curva de Churn do Curso de SQL?

WITH tb_clientes_d1 AS (
    SELECT  DISTINCT Idcliente
    FROM transacoes

    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-26'
),

tb_join AS (
    SELECT  substr(t2.DtCriacao, 1, 10) AS DtDia,
            count(DISTINCT T1.IdCliente) AS QtdeCliente,
            100. * count(DISTINCT T1.IdCliente) / (select count(*) from tb_clientes_d1) AS pctRetenção,
            100 - 100. * count(DISTINCT T1.IdCliente) / (select count(*) from tb_clientes_d1) AS pctChurn
    FROM tb_clientes_d1 AS t1

    LEFT JOIN transacoes AS t2
    ON t1.IdCliente = t2.IdCliente

    WHERE t2.DtCriacao >= '2025-08-25'
    AND t2.DtCriacao < '2025-08-30'

    GROUP BY 1
)

SELECT * FROM tb_join