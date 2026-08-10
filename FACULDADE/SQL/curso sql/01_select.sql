SELECT 'Olá Mundo'
        'Fodasse';

SELECT 20 + 30 * 2;

SELECT  IdCliente, 
        QtdePontos, 
        DtCriacao,
        DtAtualizacao
FROM clientes
WHERE QtdePontos > 50
LIMIT 10;

SELECT *
FROM clientes;