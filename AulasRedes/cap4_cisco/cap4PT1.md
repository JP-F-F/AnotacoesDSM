# Camada Física

## Propósito da camada física

### conexão física

Antes que ocorra qualquer conexão em rede primeiro é necessário estabelecer uma conexão física com uma rede local.
Conexões físicas podem ser tanto uma conexão com fio usando um cabo ou uma conexão sem fio usando ondas de rádio
O tipo de conexão física usada depende da configuração de rede. 
Dispositivos em uma rede sem fio precisam estar conectados a um ponto de acesso sem fio (AP) ou roteador sem fio.

#### Placas de interface de rede

As placas de interface de rede(NICs) conectam os dispositivos á rede. 
NICs de Ethernet servem para conexões com fio.
NICs de rede local sem fio (WLANs) servem para conexões sem fio.
Dispositivos finais podem incluir um ou dois tipos de NICs
----------------------------------------------------------------------------------------------------------
**OBS: Nem todas as conexões físicas são iguais, em termos de nível de desempenho, durante uma conexão com uma rede.**

### Camada física

A camada física do modelo OSI fornece os meios os meios de transporte dos bits de um quadro da camada de enlace no meio físico da rede.
Tal camada aceita um quadro completo da camada de enlace e o codifica em uma série de sinais que são transmitidos á mídia local.
Os bits codificados que formam um quadro são recebidos por um dispositivo final ou um dispositivo intermediário.
A camada física codifica os quadros e cria os sinais de onda elétrica, óptica ou de rádio que representam os bits em cada quadro. Esses sinais são então enviados pela mídia, um de cada vez.

## Características da camada física

### Padrões da camada física

A camada física consiste em circuitos eletrônicos, meios físicos e conectores desenvolvidos pelos engenheiros.
Os padrões de hardware, mídia, codificação e sinalização da camada física são definidos e governados por essas organizações de padrões: 

* International Organization for Standardization (ISO)
* Telecommunications Industry Association/Electronic Industries Association (TIA/EIA)
* União Internacional de Telecomunicações (ITU)
* Instituto Nacional de Padronização Americano (ANSI)
* Institute of Electrical and Electronics Engineers (IEEE)
* Autoridades reguladoras de telecomunicações nacionais, incluem Federal Communication Commission (FCC) nos EUA 
* European Telecommunications Standards Institute (ETSI)

### Componentes Físicos

As 3 áreas funcionais abordadas pelos padrões de camada física:

* Componentes Físicos;
* Codificação;
* Sinalização.

#### Componentes Físicos

Componentes físicos = dispositivos de hardware eletrônico, mídia e outros conectores que transmitem os sinais que representam os bits.
Componentes de Hardware = NICs, interfaces e conectores, materiais de cabo e projetos de cabo.
estes são especificados nos padrões associados à camada física.

### Codificação

Codificação/codificação de linha é um método que converte fluxos de bits em um "código" predefinido.
Esses códigos são agrupamentos de bits que fornecem um padrão previsível que pode ser reconhecido pelo emissor e pelo receptor.
Basicamente a codificação é o método ou o padrão usado para representar as informações digitais.

### Sinalização

A camada física deve gerar sinais elétricos, ópticos ou sem fio que representam os valores "0" e "1".
A maneira como os bits são representados é chamada de sinalização.
Os padrões da camada física definem qual tipo de sinal representa "1" e qual representa "0", esse processo pode ser tão simples quanto alterar um nível de um sinal elétrico ou de pulso óptico.

### Largura de Banda

Meios físicos diferentes aceitam a transferência de bits a taxas diferentes.
Largura de Banda = capacidade na qual um meio pode transportar dados.
A largura de banda digital mede a quantidade de dados que podem fluir de um lugar para outro durante um determinado tempo.
A largura de banda é geralmente medida em Kbps, Mbps e Gbps.

Uma combinação de fatores determina a largura de banda prática de uma rede:

* As propriedades do meio físico
* As tecnologias escolhidas para sinalização e detecção de sinais de rede

[tabela largura de banda](../imagens/tbl_larguraDeBanda.png)

### Terminologia de Largura de Banda

Termos usados para medir a qualidade da largura de banda:

* Latência;
* Rendimento;
* Dados úteis.

#### Latência 

latência = tempo necessário para os dados viajarem de um ponto a outro, incluindo atrasos.
Em uma internetwork ou em uma rede com vários segmentos, a taxa de transferência não pode ser mais rápida que o link mais lento no caminho da origem ao destino.
Ou seja mesmo que todos os segmentos tenham uma banda larga, apenas um segmento no caminho com uma taxa baixa de tranferência pode desalerar tudo.

#### Taxa de Transfêrencia 

taxa de transfêrencia = medida da transferência de bits através da mídia durante um determinado período.
Geralmente a taxa de transferencia não corresponde á largura de banda que foi específicada na camada física.
A taxa de transfêrencia geralmente é menor que a largura de banda.
Fatores que influênciam essa taxa.

* A quantidade de tráfego;
* O tipo de tráfego;
* A latência criada pelo número de dispositivos de rede encontrados entre a origem e o destino.

#### Dados Úteis

GoodPut = a medida de dados usáveis transferidos em um determinado período, Goodput é a taxa de transferência menos a sobrecarga de tráfego para estabelecer sessões, reconhecimentos, encapsulamento e bits retransmitidos.
O GoodPut é sempre menor que a taxa de transfêrencia.