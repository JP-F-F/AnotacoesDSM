# Endereçamento IPv4

## Sub-rede de uma rede IPv4

### Sub-rede em um limite de octeto

As sub-redes IPv4 são criadas com um ou mais bits de host sendo usados como bits de rede.
Quanto mais bits de host forem emprestados, mais sub-redes poderão ser definidas. 
Quanto mais bits forem emprestados para aumentar o número de sub-redes reduz o número de hosts por sub-rede.
***É mais fácil dividir redes em sub-redes nos limites dos octetos: /8, /16 e /24.***

![Tabela com os prefixos e etc de Sub-redes](../imagens/tblPrefixosSubRedes.png)

### Sub-rede dentro de um limite de octeto

Entretanto, as sub-redes podem pedir emprestado bits de qualquer posição dos bits de host para criar outras máscaras.
Por exemplo, um endereço de rede /24 costuma ser dividido em sub-redes usando prefixos mais longos ao pedir 
bits emprestados do quarto octeto.

![Tabela com as mascáras de sub-redes além do octeto](../imagens/tblSubRedesAlemOcteto.png)

Cada bit emprestado no quarto octeto, o número de sub-redes disponíveis é dobrado, enquanto reduz o número 
de endereços de host por sub-rede.

## Sub-rede uma barra 16 e um prefixo 8

