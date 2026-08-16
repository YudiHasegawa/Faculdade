DROP TABLE IF EXISTS relatorio_diario;

CREATE TABLE IF NOT EXISTS relatorio_diario AS

WITH tb_sumario_dias AS (
    SELECT  substr(DtCriacao, 1, 10) AS DtDia,
            count(IdTransacao) AS QtdeTransacao
    FROM transacoes

    GROUP BY 1
    ORDER BY 1
),

tb_acum AS (
    SELECT  *,
            sum(QtdeTransacao) OVER (ORDER BY DtDia) AS QtdeTransacaoAcum
    FROM tb_sumario_dias
)

SELECT * FROM tb_acum
;

SELECT * FROM relatorio_diario;