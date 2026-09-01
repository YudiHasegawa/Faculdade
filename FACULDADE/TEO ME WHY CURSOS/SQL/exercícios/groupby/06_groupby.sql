-- Qual dia da semana quem mais pedidos em 2025?
SELECT  strftime('%w', substr(Dtcriacao, 1 ,10)) AS DiaSemana,
        count(DISTINCT IdTransacao) AS QtdeTransacao,
        count(IdTransacao) AS QtdeTransacao2,
        count(*) AS QtdeTransacao3
FROM transacoes
WHERE substr(Dtcriacao, 1, 4) = '2025'

GROUP BY 1

ORDER BY 2 DESC