-- Qual o dia da semana mais ativo de cada usuário?
WITH tb_dia_cliente AS (
    SELECT  DISTINCT IdCliente,
            strftime('%w', substr(DtCriacao, 1,10)) AS DtDia,
            count(*) AS QtdeInteracoes
    FROM transacoes

    GROUP BY 1, 2
    ORDER BY 1, 3 DESC
),

tb_rn AS (
    SELECT  *,   
            row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeInteracoes DESC, DtDia) AS rn
    FROM tb_dia_cliente
)

SELECT * FROM tb_rn
WHERE rn = 1