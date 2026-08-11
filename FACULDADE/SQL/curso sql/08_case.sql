/*
Intervalos
De 0 a 500          -> Noob
De 501 a 1000       -> Amateur
De 1001 a 5000      -> Pro
De 5001 a 10000     -> Hacker
+10001              -> Herobrine
*/

SELECT  idCliente,
        qtdePontos,
        CASE
            WHEN qtdePontos <= 500 THEN 'Noob'
            WHEN qtdePontos <= 1000 THEN 'Amateur'
            WHEN qtdePontos <= 5000 THEN 'Pro'
            WHEN qtdePontos <= 10000 THEN 'Hacker'
            ELSE 'Herobrine'
        END AS Nível,

        CASE
            WHEN qtdePontos <= 1000 THEN '1'
            ELSE 0
        END AS Ruim,
        CASE
            WHEN qtdePontos > 1000 THEN '1'
            ELSE 0
        END AS Bom
FROM clientes
WHERE qtdePontos > 1000
ORDER BY qtdePontos DESC