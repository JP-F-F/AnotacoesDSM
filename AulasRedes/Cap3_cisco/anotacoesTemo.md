# Colocar essas anotações no arquivo **cisco_cap3**

# Modelos De Referência

## Os benefícios de usar um modelo em camadas

Modelos de rede são úteis pois eles permitem que nós tenhamos uma consciência de o que está acontecendo com os pacotes e etc, afinal na vida real não é possível ver pacotes de rede viajando.
Por isso um modelo em camadas é usado para modularizar as operações de uma rede em camadas gerenciáveis.

Benefícios de usar esse tipo de modelo:
 * Auxiliar no projeto de protocolos porque os protocolos que operam em uma camada específica definiram as  informações sobre as quais atuam e uma interface definida para as camadas acima e abaixo.
 * Fomentar a concorrência porque produtos de diferentes fornecedores podem trabalhar juntos.
 * Impedir que alterações de tecnologia ou capacidade em uma camada afetem outras camadas acima e abaixo
 * Fornecer uma linguagem comum para descrever funções e capacidades de rede.

Existem dois modelos em camadas que são usados para isso:

 * Modelo de referência OSI (Open System Interconnection)
 * Modelo de referência TCP / IP

## Modelo de Referência OSI

Esse modelo fornece uma extensa lista de funções e serviços que podem ocorrer em cada camada, tal modelo oferece também consistência em todos os tipos de protocolo e serviços, assim descrevendo o que deve ser feitos em camadas específicas, sem mostrar uma forma obrigatória de como deve ser feito.
Esse modelo também descreve a interação entre as camadas que estão diretamente relacionadas. 

[Tabela Camadas OSI](../imagens/tblCamadasOSI.png)

## Modelo de Protocolo TCP/IP

Esse modelo é usado para comunicação entre redes, este modelo TCP/IP é um modelo de protocolo que descreve as funções que ocorrem em cada camada dos protocolos dentro da suíte TCP/IP.

[Tabela do Modelo de Protocolo TCP/IP](../imagens/tblModelTCPIP.png)

## Comparação entre o Modelo OSI e o Modelo TCP/IP

As principais semelhanças se encontram nas camadas de transporte e rede, e sua principal diferença está em como as camadas de cima e de baixo se relacionam.

 * A Camada OSI 3, a camada de rede, é mapeada diretamente para a camada de Internet TCP / IP. Essa camada é usada para descrever os protocolos que endereçam e encaminham mensagens em uma rede interconectada.
 * A Camada OSI 4, a camada de transporte, mapeia diretamente para a camada de transporte TCP / IP. Essa camada descreve os serviços e as funções gerais que fornecem uma entrega ordenada e confiável de dados entre os hosts origem e destino.
 * A camada de aplicativos TCP / IP inclui vários protocolos que fornecem funcionalidade específica para uma variedade de aplicativos do usuário final. As camadas 5, 6 e 7 do modelo OSI são usadas como referências para desenvolvedores e fornecedores de software de aplicação para produzir aplicaçõesque operam em redes.
 * Ambos os modelos TCP/IP e OSI são usados geralmente para referenciar protocolos em várias camadas. Como o modelo OSI separa a camada de enlace de dados da camada física, geralmente é usado para referenciar as camadas inferiores.

# Encapsulamento de Dados

## Segmentando Mensagens

A melhor abordagem para transmissão de dados na rede é dividir os dados em pequenos pedaços que são mais fáceis de gerenciar.

A segmentação é o _processo de **dividir** um fluxo de dados em **unidades menores** para transmissão_.
A segmentação é necessária pois as redes usam os conjuntos TCP/IP que envia dados em pacotes IP individuais.
Mesmo que pacotes tenham o mesmo destino, isso não garante que eles serão enviados pelo mesmo caminho.

As duas principais vantagens da Segmentação:

 * Aumenta a velocidade - Como um fluxo de dados grande é segmentado em pacotes, grandes quantidades de dados podem ser enviadas pela rede sem amarrar um link de comunicação. Isso permite que muitas conversas diferentes sejam intercaladas na rede chamada multiplexação.
 * Aumenta a eficiência -Se um único segmento não conseguir alcançar seu destino devido a uma falha na rede ou no congestionamento da rede, somente esse segmento precisa ser retransmitido em vez de reenviar todo o fluxo de dados

