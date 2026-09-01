-- Qual o produto com mais pontos transacionados?
SELECT  IdProduto,
        sum(vlProduto * QtdeProduto) AS TotalPontos,
        sum(QtdeProduto) AS QtdeVenda,
        count(IdTransacao) AS QtdeTransacao
FROM transacao_produto

GROUP BY 1

ORDER BY 2 DESC