# As Regras (?)

## Dispositivos em Uma Bolha

Nós vemos redes atráves dos diagramas de topologia certo? certo. Os dispositivos veem a rede de forma peculiar, pense como se eles estivesssem dentro de bolhas, ou seja ele só sabe as informações sobre si próprio, e pensando nisso são os protocolos que fazem os dispositivos terem mais consciencia da rede, sabendo assim algumas informações sobre ela, como para onde suas mensagens vão e etc.
Os protocolos são as regras que regem como uma rede se comunica. A rede é divida em pedaços, em pacotes para ser mais exato, e é aqui que os protocolos agem, fazendo assim com que os pacotes cheguem em seus destinos.

Os protocolos _"DHCP/ICMPv6"_ forneçem informações sobre os endereçamentos IP, informando ao dispositivo, a qual rede ele pertence, endereço de gateway padrão, endereço do servidor DNS.
O _TCP_ é um protocolo utilizado para garantir a fiabilidade, ou seja ele garante que todas as informações enviadas e recebidas serão enviadas, pois caso algum endereço IP não faça a entrega o TCP reenviara as informações.

## Fundamentos das Comunicações

Os metodos de comunicação tem três elementos comuns
 * Fonte da Mensagem (remetente) - As fontes da mensagem são pessoas ou dispositivos eletrônicos que precisam enviar uma mensagem para outras pessoas ou dispositivos.
 * Destino da mensagem (destinatário) - O destino recebe a mensagem e a interpreta.
 * Canal - Consiste na mídia que fornece o caminho pelo qual a mensagem viaja da origem ao destino.

A comunicação é regida por protocolos, eles são específicos para o metódo de comunicação que está sendo usado.

## Estabelecimento de regras

Os protocolos devem ter em conta os seguintes requisitos para entregar com êxito uma mensagem compreendida pelo receptor:
 * Um emissor e um receptor identificados;
 * Língua e gramática comum;
 * Velocidade e ritmo de transmissão;
 * Requisitos de confirmação ou recepção

## Requisitos de Protocolo de rede

Além de identificar a origem e o destino, os protocolos de computadores e de redes definem os detalhes sobre como uma mensagem é transmitida por uma rede. Protocolos de computador comuns incluem os seguintes requisitos:

 * Codificação de mensagens;
 * Formatação e encapsulamento de mensagens;
 * Tamanho da mensagem;
 * Tempo da mensagem;
 * Opções de envio de mensagem.

## Codificação de Mensagem

Uma das etapas iniciais do envio de uma mensagem é codificá-la. Codificação é o processo de conversão da informação pra uma forma mais aceitável de transmissão. A decodificação é o processo inverso para interpretar a mensagem.
Mensagens na rede são convertidas em bits antes de serem enviadas, Cada bit é codificado em um padrão de tensões em fios de cobre, luz infravermelha em fibras ópticas ou microondas para sistemas sem fio.

## Formatação e encapsulamento de mensagens

Ao enviar uma mensagem, é necessário usar um formato ou uma estrutura específica, que variam dependendo do tipo de mensagem e do canal. Aqui também é identificado o endereço do remetente e do destinatário.

## Tamanho da mensagem 

Na comunicação entre computadores, quando mensagens muito longas são enviadas o host de origem a divide em partes, e envia as partes separadas, cada uma dessas partes/quadros tem suas próprias informações de endereço, o host final vai recontruir essas partes na mensagem original, mensagens muito longas ou muito curtas não são enviadas, existe um tamanho max e min para as mensagens.

## Tempo De Mensagem

O tempo da mensagem é algo muito importante na comunicação, sendo composto pelas seguintes caracteristicas:

 * **Controle de Fluxo**: Processo de gerenciamento da taxa de transmissão, define quanta informação pode ser enviada e a velocidade que pode ser entregue;
 * **Tempo Limite de Resposta**: Os hosts da rede usam protocolos de rede que especificam quanto tempo esperar pelas respostas e que ação executar se ocorrer um tempo limite de resposta.
 * **Método de Acesso**: Determina quando alguém pode enviar uma mensagem,quando um dispositivo deseja transmitir em uma LAN sem fio, é necessário que a placa de interface de rede (NIC) da WLAN determine se a mídia sem fio está disponível.

## Opções de envio de mensagem

Essas opções se referem a para quantas máquinas a máquina:
 * **Unicast** - As informações estão sendo transmitidas para um único dispositivo final.
 * **Multicast** - Informações estão sendo transmitidas para um ou mais dispositivos finais.
 * **Broadcast** - Informações estão sendo transmitidas para todos os dispositivos finais

# Protocolos

## Visão Geral do Protocolo de Rede

Os protocolos de rede definem um formato comum e um conjunto de regras para a troca de mensagens entre dispositivos. Estes são implementados por dispositivos finais e intermediários em software, hardware ou ambos.

[tabela tipos de Protocolos](../imagens/tabela_tiposProtocolos.png)

