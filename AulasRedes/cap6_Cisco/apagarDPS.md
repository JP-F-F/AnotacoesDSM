### Fornecimento de acesso ao Meio Físico

Conforme os pacotes vão viajando pela rede e seus ambientes(entre hosts locais e hosts remotos) eles podem se deparar com diferentes características.
Uma LAN Ethernet geralmente consiste em muitos hosts que disputam o acesso na mídia da rede. A subcamada MAC resolve isso. Com links seriais, o método de acesso só pode consistir em uma conexão direta entre apenas dois dispositivos, geralmente dois roteadores. Portanto, eles não exigem as técnicas empregadas pela subcamada MAC IEEE 802.

A interface do roteador encapsulam o pacote no quadro apropriado. O método adequado de controle de acesso de mídia é usado para acessar cada link. 
Em qualquer troca de pacotes de camada de rede pode haver várias transições de camadas de enlace de dados e de meios físicos.

Em cada salto ao longo do caminho, um roteador executa as seguintes funções da Camada 2:

1. Aceita um quadro de um meio;
2. Desencapsula o quadro;
3. Encapsula novamente o pacote em um novo quadro;
4. Encaminha o novo quadro apropriado para o meio desse segmento da rede física.

Conforme o roteador processa os quadros, ele usa os serviços da camada de enlace de dados para receber o quadro de um meio e desencapsulá-lo para a PDU de camada 3, encapsular de novo a PDU em um novo quadro no meio do próximo link da rede

### Padrões da camada de Enlace de Dados

Os protocolos da camada de enlace de dados geralmente não são definidos por RFCs (Request for Comments), ao contrário dos protocolos das camadas superiores do conjunto TCP / IP.