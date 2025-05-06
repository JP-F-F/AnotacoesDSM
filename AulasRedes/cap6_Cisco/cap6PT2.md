# Camada de enlace de dados

## Quadro de enlace de dados

### O quadro 

As informações anexadas nesse quadro são definidas pelo protocolo que está em uso na rede.
**A camada de link de dados prepara os dados encapsulados (geralmente um pacote IPv4 ou IPv6) para o transporte pela**
**mídia local, encapsulando-o com um cabeçalho e um trailer para criar um quadro.**
O protocolo de link de dados é responsável pela comunicação NIC para NIC dentro da rede. Embora existam diversos
protocolos diferentes que descrevem os quadros dessa camada, **todo tipo de quadro tem três partes básicas.**
* Cabeçalho;
* Dados;
* Trailer;

Diferente de outros protocolos de encapsulamento, a camada de link de dados acrescenta informações na forma de um
<mark>trailer</mark> no fim do quadro.
Os protocolos da camada de enlace encapsulam os dados no campo de dados do quadro.
A estrutura do quadro e os campos do cabeçalho e trailer variam de acordo com o protocolo. 
Em <strong>ambientes frágeis</strong>, é necessário que aja mais controles para garantir a entrega dos quadros.
Assim <strong>aumentando o tamanho do cabeçalho e do trailer</strong>

### Campos do Quadro

O enquadramento quebra o fluxo de dados em **grupos decifráveis**, as informações de controle inseridas no
cabeçalho e trailer são diferentes campos.
Assim fornecendo aos sinais físicos uma estrutura reconhecivel por nós e decodificada em pacotes de destino.
Os campos de quadro genérico são mostrados na figura. Nem todos os protocolos incluem todos esses campos. Os padrões para um protocolo de enlace de dados específico definem o formato real do quadro.

![Campos do Quadro](../imagens/camposDoQuadro.png)

Os campos de quadro incluem o seguinte:

* **Sinalizadores de início e fim do quadro** - Usado para identificar os limites de início e fim do quadro.
* **Endereçamento** - indica os nós de origem e destino na mídia.
* **Tipo** - identifica o protocolo da camada 3 no campo de dados.
* **Controle** - Identifica serviços especiais de controle de fluxo, como qualidade de serviço (QoS). A QoS dá prioridade ao encaminhamento para certos tipos de mensagens. Por exemplo, os quadros de voz sobre IP (VoIP) normalmente recebem prioridade porque são sensíveis ao atraso.

* **Dados** - Contém a carga útil do quadro (ou seja, cabeçalho do pacote, cabeçalho do segmento e os dados).
* **Detecção de Erro** - Incluído após os dados para formar o trailer.

Os protocolos DLL acrescentam o trailer ao final do quadro, esse processo se chama <mark>detecção de erros</mark>
<strong>O trailer determina se o quadro chegou sem erros</strong>. Este coloca um resumo lógico ou matemático dos
bits que compõem o quadro no trailer. A camada de enlace adiciona essa detecção de erros pois os sinais na mídia 
podem estar sujeito a interferências, distorções ou perdas que alterariam significativamente os valores de bits 
que esses sinais representam.

Um nó de transmissão **cria um resumo lógico dos conteúdos do quadro**, conhecido como **valor de verificação de** 
**redundância cíclica (cyclic redundancy check - CRC)** Este valor é colocado no campo FCS (Sequência de Verificação de 
Quadro) para exibição ou conteúdo do quadro. No trailer Ethernet, o FCS fornece um método para o nó de recebimento 
determinar se o quadro apresentou erros de transmissão.