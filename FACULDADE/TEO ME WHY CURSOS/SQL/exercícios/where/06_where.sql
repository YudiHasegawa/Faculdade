-- Lista de  pedidos reanlizados no fim de semana
SELECT  IdTransacao,
        IdCliente,
        strftime('%w', datetime(substr(DtCriacao, 1, 19))) AS FimdeSemana
FROM transacoes
WHERE strftime('%w', datetime(substr(DtCriacao, 1, 19))) IN ('6','0');