-- Quais clientes mais perderam pontos por Lover?
SELECT  count(t1.IdTransacao) AS TotalTransacao,
        t1.IdCliente,
        sum(t2.vlProduto * t2.QtdeProduto) AS PontosTotal,
        t3.DescCategoriaProduto
FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

LEFT JOIN produtos AS t3
ON t2.IdProduto = t3.IdProduto

WHERE t3.DescCategoriaProduto = 'lovers'

GROUP BY 2

ORDER BY 3