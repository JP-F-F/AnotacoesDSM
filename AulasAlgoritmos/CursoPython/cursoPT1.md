# Introdução a Programação de computadores e Python

## Introdução a Programação

### Linguagens Naturais VS. Linguagens de Programação

Computadores entendem linguagem de máquina.
Conjuntos completos de comandos são chamados de **Lista de instruções(IL)** 

### Linguagem de máquina VS. Linguagem de alto nível

A IL é o **Alfabeto de um linguagem de máquina**.
Linguagens de alto nível são aquelas que permitem as pessoas entender com certa facilidade o que está
sendo escrito para a máquina assim permitindo que as pessoas expressarem comandos que são mais complexos que a
IL oferece.
Programas escritos em linguagens de alto nível é chamado de **código fonte**

### Compilação VS. Interpretação

Existem duas maneira de transformar um programa em linguagem de alto nível para linguagem de máquina:

* **Compilação**: O programa original é convertido uma vez(isso ocorre toda a vez que o código-fonte é alterado)
ao obter um arquivo(um arquivo .exe para códigos executados no ms windows) contendo o código de máquina.
* **interpretação**: traduz o programa toda vez que ele é executado, o **interpretador** faz esse processo

### O que o interpretador faz

Programas são básicamente texto, por isso o código fonte geralmente é colocado em arquivos de texto.
Então o interpretador vai ler esse arquivo, então primeiramente ele irá verificar se a escrita está correta, caso ele encontre um erro ele irá encerrar o processo e retornará uma mensagem de erro.
Ele támbem irá informar onde está o erro e o que o causou (claro nem sempre ele é muito preciso nisso).


### Compilação VS. Intepretação, vantagens e desvantagens

![Vantagens e desvatagens compilação e interpretação](../CursoPython/imgsCurso/compEinterVantagens.png)

## Introdução ao Python

### Rivais do Python

O Python tem dois concorrentes diretos, com propriedades e predisposições comparáveis. São eles:

* Perl - uma linguagem de script criada originalmente por Larry Wall, uma linguagem mais tradicional e 
conservadora, se parece com algumas linguagens antigas derivadas do C;
* Ruby - uma linguagem de script criada por Yukihiro Matsumoto, uma linguagem inovadora.

### Onde vemos o Python

Ele é muito usado para implementar **serviços de internet** complexos, como mecanismos de pesquisa, 
armazenamento em nuvem e ferramentas, mídias socias e etc.

### Porquê não o python 

Embora python seja bem popular, existem algumas áreas que ele está ausente, como:

* **programação de baixo nível (às vezes chamada de programação "próxima ao metal"):** se você quiser implementar 
um driver ou mecanismo gráfico extremamente eficaz, não usará Python;
* **aplicativos para dispositivos móveis:** embora esse território ainda esteja esperando para ser conquistado 
pelo Python, provavelmente acontecerá algum dia.

# Tipos de dados em python, Váriaveis, operadores e operações I/O básicas

## Seção 1 - O programa Olá Mundo

### Mecanismos de Palavra-Chave

Argumentos de palavra-chave possuem **três** elementos:
* Uma **Palavra-chave** que identifica o argumento;
* Um **Sinal de igual**;
* Um **valor** atribuído a esse argumento.

Qualuer argumento de palavra-chave dever ser o último argumento declarado na função

Podemos usar o "parametro" "END=''" quando queremos alterar o final de uma linha do PRINT()
Podemos usar o "SEP=''" quando quisermos definir como o PRINT deve separar os argumentos recebidos.

## Seção 2 - literais pyhton

Podemos usar a letra 'e' para fazer com que o número seja multiplicado pelo expoente, assim podemos resumir
a escrita de números muito grandes. EX: 3E8.
OBS: o expoente (o valor após o E) tem que ser um número inteiro; a base (o valor na frente do E) pode ser um 
número inteiro ou um valor flutuante.

## Seção 3 - Operadores - ferramentas de manipulação de dados

**OBS: A divisão inteira muitas vezes é chamada tambem de DIVISÃO DE PISO**

## Seção 4 Váriaveis - Caixas em formas de Dados

Convenções para nomes de váriaveis:

* os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
* nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun, my_function)
* também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada.

**Palavras-chave do python:** 'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

## Seção 6 - interação com o usuário

