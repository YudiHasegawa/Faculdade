DROP TABLE IF EXISTS projeto_final;

CREATE TABLE IF NOT EXISTS projeto_final AS

WITH tb_transacoes AS (
    SELECT  IdTransacao,
            IdCliente,
            QtdePontos,
            datetime(substr(DtCriacao, 1,19)) AS DtCriacao,
            julianday('2025-08-30') - julianday(substr(DtCriacao, 1 ,10)) AS diffDate,
            CAST(strftime('%H', substr(DtCriacao, 1,19)) AS INTEGER) AS DtHora
    FROM transacoes
    WHERE DtCriacao < '2025-08-30'
),

tb_cliente AS (
    SELECT  IdCliente,
            datetime(substr(DtCriacao, 1,19)) AS DtCriacao,
            CAST(julianday('2025-08-30') - julianday(substr(DtCriacao, 1 ,10)) AS INTEGER) AS IdadeBase
    FROM clientes
),

tb_sumario_transacoes AS (
    SELECT  IdCliente,
            count(IdTransacao) AS QtdeTransacoesVida,
            count(CASE WHEN diffDate <= 56 THEN IdTransacao END) AS QtdeTransacoes56,
            count(CASE WHEN diffDate <= 28 THEN IdTransacao END) AS QtdeTransacoes28,
            count(CASE WHEN diffDate <= 14 THEN IdTransacao END) AS QtdeTransacoes14,
            count(CASE WHEN diffDate <= 7 THEN IdTransacao END) AS QtdeTransacoes7,
            sum(QtdePontos) AS SaldoPontos,
            sum(CASE WHEN QtdePontos > 0 THEN QtdePontos ELSE 0 END) AS PontosPosVida,
            sum(CASE WHEN QTdePontos > 0 AND diffDate <= 56 THEN QtdePontos ELSE 0 END) AS QtdePontos56,
            sum(CASE WHEN QTdePontos > 0 AND diffDate <= 28 THEN QtdePontos ELSE 0 END) AS QtdePontos28,
            sum(CASE WHEN QTdePontos > 0 AND diffDate <= 14 THEN QtdePontos ELSE 0 END) AS QtdePontos14,
            sum(CASE WHEN QTdePontos > 0 AND diffDate <= 7  THEN QtdePontos ELSE 0 END) AS QtdePontos7,
            sum(CASE WHEN QtdePontos < 0 THEN QtdePontos ELSE 0 END) AS PontosNegVida,
            sum(CASE WHEN QtdePontos < 0 AND diffDate <= 56 THEN QtdePontos ELSE 0 END) AS QtdePontosNeg56,
            sum(CASE WHEN QtdePontos < 0 AND diffDate <= 28 THEN QtdePontos ELSE 0 END) AS QtdePontosNeg28,
            sum(CASE WHEN QtdePontos < 0 AND diffDate <= 14 THEN QtdePontos ELSE 0 END) AS QtdePontosNeg14,
            sum(CASE WHEN QtdePontos < 0 AND diffDate <= 7  THEN QtdePontos ELSE 0 END) AS QtdePontosNeg7,
            CAST(min(diffdate) AS INTEGER) AS DiasUltimaInteracao
            
    FROM tb_transacoes

    GROUP BY 1
    ORDER BY 2 DESC
),

tb_transacao_produto AS (
    SELECT  t1.IdCliente,
            t1.IdTransacao,
            t3.DescNomeProduto,
            julianday('2025-08-30') - julianday(substr(DtCriacao, 1 ,10)) AS diffDate

    FROM tb_transacoes AS t1

    LEFT JOIN transacao_produto AS t2
    ON t1.IdTransacao = t2.IdTransacao

    LEFT JOIN produtos AS t3
    ON t2.IdProduto = t3.IdProduto
),

tb_cliente_produto AS (
    SELECT  IdCliente,
            DescNomeProduto,
            count(IdTransacao) AS QtdeTransVida,
            count(CASE WHEN diffDate <= 56 THEN IdTransacao END) AS QtdeTrans56,
            count(CASE WHEN diffDate <= 28 THEN IdTransacao END) AS QtdeTrans28,
            count(CASE WHEN diffDate <= 14 THEN IdTransacao END) AS QtdeTrans14,
            count(CASE WHEN diffDate <= 7  THEN IdTransacao END) AS QtdeTrans7

    FROM tb_transacao_produto 

    GROUP BY 1, 2
),

tb_cliente_produto_rn AS (
SELECT  *,
        row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTransvida DESC) AS rnvida,
        row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTrans56 DESC) AS rn56,
        row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTrans28 DESC) AS rn28,
        row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTrans14 DESC) AS rn14,
        row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTrans7 DESC) AS rn7
FROM tb_cliente_produto
),

tb_interacoes_dia AS (
    SELECT  IdCliente,
            count(IdTransacao) AS QtdeInteracoes,
            strftime('%w', substr(DtCriacao, 1,10)) AS DtDia
    FROM tb_transacoes

    WHERE diffDate <= 28

    GROUP BY 1, 3
),

tb_rn_dia AS (
    SELECT  *,
            row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeInteracoes DESC) AS RnDia
    FROM tb_interacoes_dia
),

tb_join AS (
    SELECT  t1.*,
            t2.IdadeBase,
            t3.DescNomeProduto AS ProdutoVida,
            t4.DescNomeProduto AS Produto56,
            t5.DescNomeProduto AS Produto28,
            t6.DescNomeProduto AS Produto14,
            t7.DescNomeProduto AS Produto7,
            COALESCE(t8.DtDia, -1) AS DtDia,
            COALESCE(t9.Periodo, 'Sem Informação') AS PeriodoMaisTransacao28
    FROM tb_sumario_transacoes AS t1

    LEFT JOIN tb_cliente AS t2
    ON t1.IdCliente = t2.IdCliente
    
    LEFT JOIN tb_cliente_produto_rn AS t3
    ON t1.IdCliente = t3.IdCliente
    AND t3.rnvida = 1

    LEFT JOIN tb_cliente_produto_rn AS t4
    ON t1.IdCliente = t4.IdCliente
    AND t4.rn56 = 1

    LEFT JOIN tb_cliente_produto_rn AS t5
    ON t1.IdCliente = t5.IdCliente
    AND t5.rn28 = 1

    LEFT JOIN tb_cliente_produto_rn AS t6
    ON t1.IdCliente = t6.IdCliente
    AND t6.rn14 = 1

    LEFT JOIN tb_cliente_produto_rn AS t7
    ON t1.IdCliente = t7.IdCliente
    AND t7.rn7 = 1

    LEFT JOIN tb_rn_dia AS t8
    ON t1.IdCliente = t8.IdCliente
    AND t8.RnDia = 1

    LEFT JOIN tb_rn_periodo AS t9
    ON t1.IdCliente = t9.IdCliente
    AND t9.rnperiodo = 1
),

tb_cliente_periodo AS (
    SELECT  IdCliente,
            CASE 
                WHEN DtHora BETWEEN 7 AND 12 THEN 'Manhã'
                WHEN DtHora BETWEEN 13 AND 18 THEN 'Tarde'
                WHEN DtHora BETWEEN 19 AND 23 THEN 'Noite'
                ELSE 'Madrugada'
            END AS Periodo,
            COUNT(IdTransacao) AS QtdeTransacoes
    FROM tb_transacoes

    WHERE diffDate <= 28

    GROUP BY 1, 2
),

tb_rn_periodo AS (
    SELECT  *,
            row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTransacoes DESC) AS rnperiodo
    FROM tb_cliente_periodo
)

SELECT  '2025-08-30' AS DtRef,
        *,
        100. * QtdeTransacoes28 / QtdeTransacoesVida AS Engajamento28Vida
FROM tb_join
;