SELECT *
FROM clientes 
ORDER BY qtdePontos DESC
LIMIT 10;

SELECT  idCliente,
        DtCriacao,
        qtdePontos,
        flTwitch,
        flEmail
FROM clientes
WHERE flTwitch = 1
AND flEmail = 1
ORDER BY DtCriacao ASC, qtdePontos DESC
LIMIT 10;