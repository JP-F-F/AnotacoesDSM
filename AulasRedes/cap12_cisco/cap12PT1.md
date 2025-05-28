# Endereçamento IPv6

## Problemas do IPv4

### Coexistência do IPv4 e IPv6

Não há uma data exata para migrar para o IPv6. Tanto o IPv4 como o IPv6 coexistirão no futuro próximo. 
A IETF criou vários protocolos e ferramentas para ajudar os administradores de rede a migrarem as redes para IPv6. 
As técnicas de migração podem ser divididas em três categorias:

* Pilha Dupla:
    A pilha dupla permite que IPv4 e IPv6 coexistam no mesmo segmento de rede. 
    Os dispositivos de pilha dupla executam os protocolos IPv4 e IPv6 simultaneamente. 
    Conhecido como IPv6 nativo, isso significa que a rede do cliente tem uma conexão IPv6 com seu ISP e é 
    capaz de acessar o conteúdo encontrado na internet através de IPv6.

* Tunelamento:
    Tunelamento é um método de transporte de pacote IPv6 através de uma rede IPv4. 
    O pacote IPv6 é encapsulado dentro de um pacote IPv4, de forma semelhante a outros tipos de dados.

* Conversão:
    A NAT64 (Network Address Translation 64) permite que os dispositivos habilitados para IPv6 se comuniquem 
    com os dispositivos habilitados para IPv4 usando uma técnica de conversão semelhante à NAT IPv4. 
    Um pacote IPv6 é traduzido para um pacote IPv4 e um pacote IPv4 é traduzido para um pacote IPv6.

**Note: O tunelamento e a tradução são para transição para o IPv6 nativo e só devem ser usados quando**
**necessário. O objetivo deve ser as comunicações IPv6 nativas da origem até o destino.**

## Representação do endereço IPv6

### Formatos de endereço IPv6

Os endereços IPv6 têm 128 bits e são escritos como uma sequência de valores hexadecimais. 
Cada 4 bits são representados por um único dígito hexadecimal, totalizando 32 valores hexadecimais, como mostra a Figura 1. 
Os endereços IPv6 não diferenciam maiúsculas e minúsculas e podem ser escritos tanto em minúsculas como em maiúsculas.

#### Formato preferido

O formato preferencial para escrever um endereço IPv6 é x: x: x: x: x: x: x: x, com cada “x” consistindo de 
quatro valores hexadecimais.
No IPv6, um hexteto é o termo não oficial usado para se referir a um segmento de 16 bits ou quatro valores hexadecimais.
Cada “x” equivale a um único hexteto, 16 bits ou quatro dígitos hexadecimais.

***Existem duas regras que ajudam a reduzir o número de dígitos necessários para representar um endereço IPv6.***

### Regra 1 - otimizar zeros a esquerda

A primeira regra para ajudar a reduzir a notação de endereços IPv6 é omitir os 0s (zeros) à esquerda de 
qualquer seção de 16 bits ou hexteto. 
Aqui estão quatro exemplos de maneiras de omitir zeros à esquerda:

* 01AB pode ser representado como 1AB
* 09f0 pode ser representado como 9f0
* 0a00 pode ser representado como a00
* 00ab pode ser representado como ab

Mais exemplos:

````
prefencial -> 2201 : 0db8 : 0000 : 0000 : 0000 : 0200
nenhum 0 a esquerda -> 2201 : db8 : 0 : 0 : 0 : 200
````

### Regra 2 - dois pontos duplos 

A segunda regra para ajudar a reduzir a notação de endereços IPv6 é que o uso de dois-pontos duplo (::) pode 
substituir uma única sequência contígua de um ou mais segmentos de 16 bits (hextetos) compostos exclusivamente por 0s. 
Por exemplo, 2001:db8:cafe: 1:0:0:0:1 (0s iniciais omitidos) poderia ser representado como 2001:db8:cafe:1::1. 
O dois-pontos duplos (::) é usado no lugar dos três hextets all-0 (0:0:0).
Os dois-pontos em dobro (::) só podem ser usados uma vez em um endereço; caso contrário, haveria mais de um endereço resultante possível. 
Quando associada à técnica de omissão dos 0s à esquerda, a notação de endereço IPv6 pode ser bastante 
reduzida. **É o chamado formato compactado.**

Se um endereço tiver mais de uma cadeia contígua de todos os hextets 0, a prática recomendada é usar dois 
pontos duplos (::) na cadeia mais longa. 
Se as strings forem iguais, a primeira string deve usar dois pontos duplos (::)

Exemplos:
````
prefencial -> 2201 : 0db8 : 0000 : 0000 : 0000 : 0200
comprenssados/espaços -> 2201 : 0db8 :: 0200
````