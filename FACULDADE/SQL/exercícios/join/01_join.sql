-- Qual categoria tem mais produtos vendidos

SELECT  t2.DescCategoriaProduto AS Categoria,
        count(t1.IdTransacao) AS QtdeTransacao
FROM transacao_produto AS t1

LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

GROUP BY 1

ORDER BY 2 DESC;

SELECT  t2.DescCategoriaProduto AS Categoria,
        count(t1.IdTransacao) AS QtdeTransacao
FROM produtos AS t2

LEFT JOIN transacao_produto AS t1
ON t1.IdProduto = t2.IdProduto

GROUP BY 1

ORDER BY 2 DESC;