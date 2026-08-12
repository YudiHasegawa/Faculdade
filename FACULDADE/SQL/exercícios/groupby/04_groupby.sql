-- Quantos produtos são de rpg?

SELECT  count(DescCategoriaProduto)
FROM produtos
WHERE DescCategoriaProduto = 'rpg';

SELECT  DescCategoriaProduto,
        count(*)
FROM produtos
GROUP BY DescCategoriaProduto
ORDER BY count(*) DESC;