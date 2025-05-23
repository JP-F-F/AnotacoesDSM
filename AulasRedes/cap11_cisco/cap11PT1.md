# Endereçamento IPv4

## Estrutura do IPv4

### Partes de Rede e de Host

![A parte do host e a da rede do IPv4](../imagens/ipv4RedeVShost.png)

Os bits na parte de rede do endereço devem ser iguais em todos os dispositivos que residem na mesma rede. 
Os bits na parte de host do endereço devem ser exclusivos para identificar um host específico dentro de uma rede.

### A Máscara de sub-rede

A máscara de sub-rede IPv4 é usada para diferenciar a parte da rede da parte do host de um endereço IPv4. Quando um endereço IPv4 é atribuído a um dispositivo, a máscara de sub-rede é usada para determinar o endereço de rede do dispositivo. 
O endereço de rede representa todos os dispositivos na mesma rede.

![partes da máscara de sub-rede](../imagens/partesDaMascaraSubRede.png)

Para identificar as partes da rede e do host de um endereço IPv4, a máscara de sub-rede é comparada com o endereço IPv4 bit por bit, da esquerda para a direita.

Observe que, na verdade, a máscara de sub-rede não contém a parte da rede ou host de um endereço IPv4, apenas 
informa ao computador onde procurar a parte do endereço IPv4 que é a parte da rede e qual parte é a parte do host.

O processo real usado para identificar a parte da rede e a parte de host é chamado de AND.

### Comprimento do Prefixo

Expressar os endereços de rede e host, com a máscara, em decimal é uma coisa complexa.
Por isso usamos um método alternativo para identificar uma máscara de sub-rede, um método 
chamado comprimento do prefixo.
O comprimento do prefixo é o número de bits definido como 1 na máscara de sub-rede. 
Está escrito em "notação de barra", que é anotada por uma barra (/) seguida pelo número 
de bits definido como 1. 
Portanto, conte o número de bits da máscara de sub-rede e preceda-o com uma barra.

![comparando sub-rede e prefixo](../imagens/subRedeEpreFixo.png)

Ao representar um endereço IPv4 usando um comprimento de prefixo, o endereço IPv4 é 
gravado seguido do comprimento do prefixo sem espaços. 
**Por exemplo, 192.168.10.10 255.255.255.0 seria gravado como 192.168.10.10/24.**

### Determinando a rede - lógica AND

Um AND lógico é uma das três operações booleanas usadas na lógica booleana ou digital. 
As outras duas são OR e NOT. A operação AND é usada para determinar o endereço de rede.
Para identificar o endereço de rede de um host IPv4, é feito um AND lógico, bit a bit, 
entre o endereço IPv4 e a máscara de sub-rede. 
Quando se usa AND entre o endereço e a máscara de sub-rede, o resultado é o endereço de rede.

![Exemplo dessa comparação and](../imagens/exCompANDsubrede.png)

Usando a primeira sequência de bits como exemplo, observe que a operação E é executada no 
1 bit do endereço do host com o 1 bit da máscara de sub-rede. 
Isso resulta em um bit 1 para o endereço de rede.
A operação AND entre um endereço de host IPv4 e uma máscara de sub-rede resulta no 
endereço de rede IPv4 para este host. 
Neste exemplo, a operação AND entre o endereço de host 192.168.10.10 e a máscara de 
sub-rede 255.255.255.0 (/24) resulta no endereço de rede IPv4 192.168.10.0/24.
***Esta é uma operação IPv4 importante, pois informa ao host a qual rede pertence***

### Endereços de Broadcast, de Host e de Rede

Dentro de cada rede há três tipos de endereços IP:

* Endereço de rede
* Endereços de host
* Endereço de broadcast

#### Endereço de Rede

Um endereço de rede é um endereço que representa uma rede específica. 
Um dispositivo pertence a esta rede se atender a três critérios:

* Tem a mesma máscara de sub-rede que o endereço de rede.
* Ele tem os mesmos bits de rede que o endereço de rede, conforme indicado pela máscara de sub-rede.
* Ele está localizado no mesmo domínio de difusão que outros hosts com o mesmo endereço de rede.

Conforme mostrado na tabela, o endereço de rede tem todos os 0 bits na parte do host, conforme determinado pela máscara de sub-rede. 
Neste exemplo, o endereço de rede é 192.168.10.0/24. 
**Um endereço de rede não pode ser atribuído a um dispositivo.**

![Endereço de Rede exemplo](../imagens/subredeEnderecoRede.png)

#### Endereço de Host

Endereços de host são endereços que podem ser atribuídos a um dispositivo(Pc, celular etc).
Uma parte do host do endereço é os bits indicados por 0 bits na máscara de sub-rede. 
Os endereços de host podem ter qualquer combinação de bits na parte do host, exceto para 
todos os 0 bits (isso seria um endereço de rede) ou todos os 1 bits (isso seria um endereço de difusão).
Todos os dispositivos dentro da mesma rede devem ter a mesma máscara de sub-rede e os mesmos bits de rede. 
**Somente os bits do host serão diferentes e devem ser exclusivos.**

Os endereços 192.168.10.1/24 - 192.168.10.254/24 podem ser atribuídos a um dispositivo na rede.

## Unicast, BroadCast e MultiCast

### Broadcast

Um pacote de broadcast possui um endereço IP de destino com todos os (1s) na parte do host ou 32 (um) bits.
**Note: O IPv4 usa pacotes de difusão. No entanto, não há pacotes de difusão com IPv6.**

Um pacote de difusão deve ser processado por todos os dispositivos no mesmo domínio de difusão. 
Um domínio de difusão identifica todos os hosts no mesmo segmento de rede.
Uma transmissão pode ser direcionada ou limitada. 
Um broadcast direcionado é enviado para todos os hosts em uma rede específica.
Uma broadcast limitado é enviado para 255.255.255.255.

O tráfego broadcast deve ser limitado para não prejudicar o desempenho da rede ou dos dispositivos.

Como os roteadores separam domínios de broadcast, **subdividir as redes pode melhorar seu** 
**desempenho ao eliminar o excesso de tráfego broadcast.**

#### transmissões direcionadas por IP

Além do endereço de transmissão 255.255.255.255, há um endereço IPv4 de transmissão para cada rede.
Chamado de transmissão direcionada, este endereço usa o endereço mais alto na rede, que é 
o endereço onde todos os bits de host são 1s.
Para enviar dados para todos os hosts em uma rede, um host pode enviar um único pacote 
endereçado ao endereço de difusão da rede
