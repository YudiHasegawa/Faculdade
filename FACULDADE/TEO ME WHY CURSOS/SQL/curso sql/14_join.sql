SELECT *
FROM transacao_produto

LEFT JOIN produtos
ON transacao_produto.IdProduto = produtos.IdProduto

LIMIT 10;

SELECT *
FROM transacao_produto AS t1

LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

WHERE t2.IdProduto IS NULL

LIMIT 10;

SELECT  t1.*,
        t2.DescNomeProduto
FROM transacao_produto AS t1

LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

LIMIT 10;