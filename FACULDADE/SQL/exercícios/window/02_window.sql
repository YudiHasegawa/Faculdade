-- Quantidade de usuários cadastrados (absoluto e acumulado) ao longo do tempo?
WITH tb_sumario_dias AS (
    SELECT  substr(DtCriacao, 1,10) AS DtDia,
            count(DISTINCT idCliente) AS QtdeCliente
    FROM clientes

    GROUP BY 1
    ORDER BY 1
),

tb_acum AS (
SELECT  *,
        sum(QtdeCliente) OVER (ORDER BY DtDia) as QtdeClienteAcum
FROM tb_sumario_dias
)

SELECT * FROM tb_acum
ORDER BY DtDia