-- Quem iniciou o curso no primeiro dia, 
-- em média assistiu quantas aulas?

-- quem particou da 1a aula
WITH tb_prim_dia AS (
    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(Dtcriacao, 1 ,10) = '2025-08-25'
),

-- quem particou  do curso inteiro
tb_dias_curso AS (
    SELECT  DISTINCT IdCliente,
            substr(DtCriacao, 1,10) AS presentedia
    FROM transacoes
    WHERE Dtcriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    ORDER BY IdCliente, presentedia
),

-- contando quantas vezes quem partipou do primeiro dia, voltou
tb_cliente_dias AS (
    SELECT  t1.IdCliente,
            count(presentedia) AS QtdeDias
    FROM tb_prim_dia AS t1

    LEFT JOIN tb_dias_curso as t2
    ON t1.IdCliente = t2.Idcliente

    GROUP BY 1

    ORDER BY 2 DESC
)

-- calcula a média
SELECT  avg(QtdeDias),
        max(QtdeDias),
        min(QtdeDias)
FROM tb_cliente_dias