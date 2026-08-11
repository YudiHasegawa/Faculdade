SELECT  avg(qtdePontos) AS média1,

        round(avg(qtdePontos), 2) AS média2,

        sum(qtdePontos) / count(qtdePontos) AS média3,

        1. * sum(qtdePontos) / count(qtdePontos) AS média4,

        min(qtdePontos) AS Menor,
        max(qtdePontos) AS Maior,

        sum(flTwitch),
        sum(flEmail)
FROM clientes