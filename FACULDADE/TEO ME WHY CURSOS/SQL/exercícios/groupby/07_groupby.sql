-- Qual o produto mais transacionado?
SELECT  IdProduto,
        count(IdTransacao) AS QtdeTransacao,
        sum(QtdeProduto) AS QtdeProduto
FROM transacao_produto

GROUP BY IdProduto

ORDER BY sum(QtdeProduto) DESC