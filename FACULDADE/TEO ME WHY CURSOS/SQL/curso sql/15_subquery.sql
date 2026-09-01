-- Lista de transações com o produto “Resgatar Ponei”

SELECT *
FROM transacao_produto AS T1

WHERE t1.IdProduto IN (
    SELECT Idproduto
    FROM produtos
    WHERE DescNomeProduto = 'Resgatar Ponei'
)