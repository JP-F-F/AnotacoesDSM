# Camada de enlace

## Finalidade da camada de enlace

### A camada de enlace 

A camada de enlace **prepara os dados da rede para a rede física**. Também é _responsável pela placa de interface de rede (NIC) para comunicações de placa de interface de rede_. 
A camada de enlace de dados faz o seguinte:

* Permite que as camadas superiores acessem a mídia. O protocolo de camada superior não está completamente ciente do tipo de mídia que é usado para encaminhar os dados.
* Aceita dados, geralmente pacotes de Camada 3 (ou seja, IPv4 ou IPv6), e os encapsula em quadros da Camada 2.
* Controla como os dados são colocados e recebidos na mídia.
* Troca quadros entre pontos de extremidade através da mídia de rede.
* Recebe dados encapsulados, geralmente pacotes de Camada 3, e os direciona para o protocolo de camada superior apropriado.
* Executa a detecção de erros e rejeita qualquer quadro corrompido.

**A camada de enlace de dados prepara os dados de rede para a rede física**.

Nas redes de computadores um NÓ é **um dispositivo que pode receber, criar, armazenar ou encaminhar dados ao longo de um caminho de comunicação**.
Nó pode ser tanto um dispositivo final de rede(laptops e etc) quanto um dispositivo intermerdiário(switchs e etc).

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