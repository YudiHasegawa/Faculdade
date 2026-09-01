-- Quantos clientes tem Twitch?

SELECT  count(DISTINCT idCliente),
        flTwitch
FROM clientes

GROUP BY flTwitch