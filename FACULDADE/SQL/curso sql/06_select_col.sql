SELECT  idCliente, 
        qtdePontos, 
        qtdePontos + 10 AS qtdePontosplus10,
        qtdePontos * 2  qtdePontosDouble,
-- AS não é obrigatório mas é melhor para organização
        datetime(DtCriacao)
FROM clientes;

SELECT  DtCriacao,
        date(DtCriacao),
        datetime(DtCriacao)
FROM clientes;

SELECT  DtCriacao,
        substr(DtCriacao,1, 10) AS DtCriacao2,
        substr(DtCriacao,1, 19) AS DtTmpCriacao,
        datetime(substr(DtCriacao,1, 19)) AS DtTmpCriacao2,
        strftime('%w', datetime(substr(DtCriacao,1, 19))) AS DiaDaSemana
FROM clientes;