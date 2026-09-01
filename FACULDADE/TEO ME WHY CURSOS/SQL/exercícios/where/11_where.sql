-- Lista de produtos que são "chapéu"

SELECT  IdProduto,
        DescCategoriaProduto
FROM produtos
WHERE DescCategoriaProduto = 'chapeu';
