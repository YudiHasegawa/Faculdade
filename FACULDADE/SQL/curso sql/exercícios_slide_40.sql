-- Lista de transações com apenas 1 ponto
SELECT  IdTransacao,
        QtdePontos
FROM transacoes
WHERE QtdePontos = 1;

-- Lista de  pedidos reanlizados no fim de semana
SELECT  IdTransacao,
        IdCliente,
        strftime('%w', datetime(substr(DtCriacao, 1, 19))) AS FimdeSemana
FROM transacoes
WHERE strftime('%w', datetime(substr(DtCriacao, 1, 19))) IN ('6','0');

-- Lista de clientes com 0 (zero) pontos
SELECT  idCliente,
        qtdePontos
FROM clientes
WHERE qtdePontos = 0;

-- Lista de clientes com 100 a 200 pontos (inclusive ambos)
SELECT  idCliente,
        qtdePontos
FROM clientes
WHERE qtdePontos >= 100 AND qtdePontos <= 200;

-- Lista de produtos com nome que começa com "Venda de"
SELECT  IdProduto,
        DescNomeProduto
FROM produtos
WHERE DescNomeProduto LIKE 'Venda de%';

-- Lista de produtos com nome que termina com "Lover"
SELECT  IdProduto,
        DescNomeProduto
FROM produtos
WHERE DescNomeProduto LIKE '%Lover';

-- Lista de produtos que são "chapéu"

SELECT  IdProduto,
        DescCategoriaProduto
FROM produtos
WHERE DescCategoriaProduto = 'chapeu';

-- Lista de transações com o produto "Resgatar Ponei"

SELECT  IdTransacao,
        IdProduto
FROM transacao_produto
WHERE IdProduto = 15;