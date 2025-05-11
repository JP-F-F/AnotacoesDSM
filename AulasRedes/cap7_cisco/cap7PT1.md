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