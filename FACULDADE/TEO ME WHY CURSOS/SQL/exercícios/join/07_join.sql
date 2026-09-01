SELECT  t1.IdCliente,
        julianday('now') - julianday(substr(t1.Dtcriacao, 1,10)) AS IdadeBase,
        count(t2.IdTransacao) AS QtdeTransacoes
FROM clientes AS t1

LEFT JOIN transacoes AS t2
ON t1.IdCliente = t2.IdCliente

GROUP BY 1, 2