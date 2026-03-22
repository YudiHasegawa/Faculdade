Caracteres especiais usados em strings para reservar espaço e, posteriormente, inserir valores variáveis.

%d : números inteiros
%s : strings
%f : números decimais

Podemos mudar o número de posições de uma variável, por exemplo, pegar a variável "idade" e adicionar uma posição a mais na esquerda. Para realizar essa operação utilizaremos "%3d":
![[Pasted image 20260319141321.png]]

Veja que agora a variável contém 3 posições, porém a posição adicionada está vazia. Se você quiser que um número ocupe esse espaço, basta digitar o número que seja antes da quantidade de posições:
![[Pasted image 20260319141515.png]]

Para adicionar uma posição de uma variável para a direita, basta colocar o sinal de - antes do número de posições:
![[Pasted image 20260319141733.png]]

Outro exemplo:
nome = "João"
idade = 22
altura = 1.70
"%s tem %d anos e %f de altura" % (nome, idade, altura)
João tem 22 anos e 1.700000 de altura

O % foi utilizado para indicar as composições da string anterior com os conteúdos das variáveis. Quando contém mais de um, utilizado parênteses (). Porém, se analisarmos, a altura fica "1.700000". Para mudar isso, podemos utilizar dois valores entre o símbolo % e a letra f. O primeiro indica o tamanho total em caracteres a reservar; e o segundo, o número de casas decimais:
![[Pasted image 20260319142101.png]]

Podemos também omitir o número da esquerda para representar desde o início:
![[Pasted image 20260319143953.png]]

Ligações
[[Conceito de strings]]
[[Operações com Strings]]
[[Tipos de variáveis]]
[[Índices e conteúdo]]
[[F-Strings, format]]
