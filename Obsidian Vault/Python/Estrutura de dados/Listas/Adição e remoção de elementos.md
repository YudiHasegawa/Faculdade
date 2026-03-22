Adição de elementos -  para adicionar novos elementos em uma lista, se utiliza o método `.append()` ou `.extend()`

`.append()` - adiciona um elemento novo ao fim da lista.
Exemplo:
![[Pasted image 20260322120458.png]]

Lembrando que podemos converter o tipo do elemento que vai ser adicionado e é obrigado caso seja adicionado uma string.
Exemplo:
![[Pasted image 20260322120835.png]]


Também podemos adicionar um elemento de uma outra lista indicando o índice do elemento que deseja adicionar.
Exemplo:
![[Pasted image 20260322121202.png]]

`.extend()` - pode adicionar mais de um elemento novo ao fim da lista.
Exemplo:
![[Pasted image 20260322121305.png]]

As regras de conversão e adição de elemento de outra lista do `.append()` também se aplica no `.extend()`. Apenas com a diferença em que é possível realizar com mais de um elemento de uma vez.

Para remover elementos de uma lista, utilizaremos o método `del`, indicando o índice do elemento que queremos deletar.
Exemplo:
![[Pasted image 20260322124940.png]]

Todas as regras sobre índice sempre vai se aplicar quando utilizarmos em qualquer um dos métodos. Então podemos usar a sintaxe `:` para indicar o começo e o fim dos elementos que queremos remover.
Exemplo:
![[Pasted image 20260322125117.png]]

Ligações
[[Conceito de listas - list()]]
[[Cópia e fatiamento de listas]]
[[Índices e conteúdo]]
[[Uso de listas como filas (incompleto)]]
[[Uso de listas como pilhas (incompleto)]]
