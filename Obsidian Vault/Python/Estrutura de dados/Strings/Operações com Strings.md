As variáveis do tipo string suportam operações como fatiamento, concatenação e composição.

Concatenação - soma o conteúdo de variáveis string utilizando o operador de adição (+).
Exemplo:
s = "ABC"
s + "C"
ABCC
s  + "D" * 4
ABCCDDDD

Composição - utiliza strings como modelos em que podemos inserir outras strings.
Exemplo:
idade = 22
"João tem %d anos" % idade
João tem 22 anos

O % foi utilizado para indicar a composição da string anterior com o conteúdo da variável idade. O %d é um marcador de posição. O marcador indica que naquela posição estaremos colocando um valor inteiro.

Quando temos mais de um marcador na string, somos obrigados a escrever os valores a substituir entre parênteses.
Exemplo:
![[Pasted image 20260321192652.png]]

Existem outros métodos de composição mais atualizados, como format e F-Strings.

Fatiamento - permite utilizar apenas uma parte de uma string utilizando dois pontos no índice da string. O número à esquerda dos dois pontos indica a posição de início: e o à direita, do fim sem incluí-la
Exemplo:
![[Pasted image 20260319143539.png]]

Podemos também omitir o número da esquerda ou o da direita para representar do início ou até o final:
![[Pasted image 20260319143756.png]]

Ligações:
[[Conceito de strings]]
[[Índices e conteúdo]]
[[Operadores de atribuição especiais]]
[[Operadores e operações matemáticas]]
[[Operadores lógicos]]
[[Operadores relacionais]]
[[Marcadores de posição]]
[[F-Strings, format]]