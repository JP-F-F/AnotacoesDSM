# Switching Ethernet

## Quadros Ethernet

### Encapsulamento Ethernet

A Ethernet usa comunicações com fio, utilizando par trançado, ligações de fibra óptica e cabos coaxiais.
Ela opera na camada física e na de enlace de dados. 
Larguras de banda suportadas:

* 10 Mbps
* 100 Mbps
* 1000 Mbps (1 Gbps)
* 10,000 Mbps (10 Gbps)
* 40,000 Mbps (40 Gbps)
* 100,000 Mbps (100 Gbps)

Os padrões Ethernet definem os protocolos da 2 e as tecnologias da camada 1

### Subcamadas de enlace de dados

Protocolos IEEE 802 LAN/MAN e Ethernet, operam nas seguintes duas subcamadas da camada de link de dados:
Controle de Link Lógico(LCC) e controle de acesso a mídia(MAC). 

Função do LCC e MAC na camada de link de dados:

* **Subcamada LLC** - Essa subcamada IEEE 802.2 se comunica entre o software de rede nas camadas superiores e 
o hardware do dispositivo nas camadas inferiores. Ela coloca a informação no quadro que identifica qual 
protocolo de camada de rede está sendo usado para o quadro. Essas informações permitem que vários protocolos 
da camada 3, como IPv4 e IPv6, usem a mesma interface de rede e mídia.
* **Subcamada MAC** - Esta subcamada (IEEE 802.3, 802.11 ou 802.15 por exemplo) é implementada em hardware e é 
responsável pelo encapsulamento de dados e controle de acesso a mídia. Ele fornece endereçamento de camada de 
link de dados e é integrado com várias tecnologias de camada física.

### Subcamada MAC

A subcamada MAC é **responsável pelo encapsulamento de dados e acesso à mídia**.

O encapsulamento de dados IEEE 802.3 inclui o seguinte:

* **Quadro Ethernet** - Esta é a estrutura interna do quadro Ethernet.
* **Endereçamento Ethernet** - O quadro Ethernet inclui um endereço MAC de origem e de destino para fornecer o 
quadro Ethernet da NIC Ethernet para a NIC Ethernet na mesma LAN.
* **Detecção de erro Ethernet** - O quadro Ethernet inclui um trailer de sequência de verificação de quadros (FCS) usado para detecção de erros.

### Campos de um Quadro Ethernet

O tamanho mínimo de quadro Ethernet é 64 bytes e o máximo é 1518 bytes.
Qualquer quadro com comprimento menor que 64 bytes é considerado um **"fragmento de colisão" ou um "quadro** 
**desprezível"** e é automaticamente descartado pelas estações receptoras. Quadros com mais de 1.500 bytes de 
dados são considerados ***“jumbo” ou “baby giant”***.
**Quadros com tamanhos excessivos ou abaixo do mínimo são descartados.**

![Campos Ethernet](../imagens/camposEthernet.png)

![Tabela Campos Ethernet](../imagens/tblCamposEthernet.png)

## Endereços MAC de Ethernet

### Endereços MAC e hexadecimal

Um endereço MAC Ethernet consiste em um valor binário de 48 bits.
Hexadecimal é usado para identidicar endereços ethernet, é mais fácil, pois um HEX identifica quatro bits
binários.
Ao usar hexadecimal, os zeros à esquerda são sempre exibidos para concluir a representação de 8 bits. 
_Por exemplo_, o valor binário 0000 1010 é mostrado em hexadecimal como 0A.

### Endereços MAC Ethernet

O endereço MAC é usado para identificar os dispositivos físicos de origem e destino (NICs) no segmento de rede local. 
O endereçamento MAC fornece um método para identificação de dispositivo na camada de enlace de dados do modelo OSI.

**Todos os endereços MAC devem ser exclusivos do dispositivo Ethernet ou da interface Ethernet**.
Para garantir essa **EXCLUSIVIDADE** os fornecedores que vendem dispositivos ethernet fazem um registro
no IEEE onde recebem um código hexadecimal, chamado de **Identificador Exclusivo Organizacionalmente(OUI)**.

Quando um fornecedor atribui um endereço MAC a um dispositivo ou interface Ethernet, o fornecedor deve fazer o seguinte:

* Use sua OUI atribuída como os primeiros 6 dígitos hexadecimais.
* Atribua um valor exclusivo nos últimos 6 dígitos hexadecimais.

### Processamento de Quadros

Às vezes, o endereço MAC é referido como endereço gravado de fábrica (BIA, burned-in-address) porque o 
endereço é codificado na memória somente leitura (ROM) na NIC. Isso significa que o endereço é codificado no 
chip da ROM permanentemente.
Quando o computador inicia, a NIC copia o endereço MAC da ROM para a RAM.

### Endereço MAC Unicast

**Na Ethernet, se utiliza diferentes endereços MAC para comunicação unicast, broadcast e multicast da Camada 2.**
Um endereço MAC de unicast é o endereço exclusivo usado quando um quadro é enviado de um único dispositivo de 
transmissão para um único dispositivo de destino.
O processo que um host de origem usa para determinar o endereço MAC de destino associado a um endereço IPv4 é 
conhecido como ARP (Address Resolution Protocol).
O processo que um host de origem usa para determinar o endereço MAC de destino associado a um endereço IPv6 é 
conhecido como ND (Neighbour Discovery Discovery).

### Endereço MAC Broadcast

Um quadro de transmissão Ethernet é recebido e processado por cada dispositivo na LAN Ethernet. Os recursos de 
uma transmissão Ethernet são os seguintes:

* Possui um endereço MAC de destino de FF-FF-FF-FF-FF-FF em hexadecimal (48 números binários (sendo eles no valor de 0 ou 1)).
* É inundada todas as portas de switch Ethernet, exceto a porta de entrada.
* Ele não é encaminhado por um roteador.

Se os dados encapsulados forem um pacote de transmissão IPv4, isso significa que o pacote contém um endereço 
IPv4 de destino que possui todos os 1s na parte do host. Essa numeração no endereço significa que todos os 
hosts naquela rede local (domínio de broadcast) receberão e processarão o pacote.

### Endereço MAC Multicast

Um quadro de multicast Ethernet é recebido e processado por um grupo de dispositivos na LAN Ethernet que 
pertencem ao mesmo grupo de multicast. Os recursos de um multicast Ethernet são os seguintes:

* Há um endereço MAC de destino 01-00-5E quando os dados encapsulados são um pacote multicast IPv4 e um 
endereço MAC de destino de 33-33 quando os dados encapsulados são um pacote multicast IPv6.
* Há outros endereços MAC de destino multicast reservados para quando os dados encapsulados não são IP, como 
STP (Spanning Tree Protocol) e LLDP (Link Layer Discovery Protocol).
* São inundadas todas as portas de switch Ethernet, exceto a porta de entrada, a menos que o switch esteja 
configurado para espionagem multicast.
* Ele não é encaminhado por um roteador, a menos que o roteador esteja configurado para rotear pacotes multicast.

**ESPIONAGEM MULTICAST = Espionagem multicast, ou "IGMP snooping" em inglês, é uma técnica utilizada em redes** 
**de computadores para identificar grupos de dispositivos que recebem o mesmo fluxo de dados multicast**

***O intervalo de endereços multicast IPv4 é 224.0.0.0 a 239.255.255.255.***
***O intervalo de endereços multicast IPv6 começa com ff00::/8.***

Como os endereços multicast representam um grupo de endereços (às vezes chamado de grupo de hosts), eles só 
podem ser utilizados como destino de um pacote. A origem sempre será um endereço unicast.

