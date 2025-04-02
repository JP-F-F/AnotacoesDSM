# Anotações baseadas no modulo 2 do curso da cisco (2.0 - 2.3)

# Configurações básicas de Dispositivo

## Nomes de dispositivo

A primeira coisa que fazemos na configuração de um dispositivo, é dar a ele um nome exclusivo ou um nome de host.
Pensa que é tipo dar nome de váriavel, seja descritivo nos nomes, eles devem ser intuitivos.

**Como aplicar o nome de um dsipositivo na CLI**:
Nós primeiro entramos no modo de configuração global.
Após isso digite o comando _hostname (nome para maquina)_.
Caso você queira tirar/esconder o nome use o comando _no hostname_

## Diretrizes de Senha

O Cisco IOS pode ser configurado para usar senhas do modo hierárquico para permitir privilégios de acesso diferentes a um dispositivo de rede.
Todos os modos da CLI e a telnet devem ter suas respectivas senhas, devem também ser criptografadas e devem fornecer notificações legais.

**Dicas para uma senha fortissima**:

 * Use senhas com mais de oito caracteres.
 * Use uma combinação de letras maiúsculas e minúsculas, números, caracteres especiais e/ou sequências numéricas.
 * Evite usar a mesma senha para todos os dispositivos.
 * Não use palavras comuns porque elas são facilmente adivinhadas.

E pra você não sofrer criando muitas senhas dessas, é só usar um gerador de senhas.

## Colocando senhas nos dispositivos

**Colocando senha no EXEC de usuário**:
 * Primeiro a gente entra no modo EXEC global;
 * Depois usamos o comando _line console 0_;
 * Depois usamos o comando _password (insira senha aqui)_;
 * Depois usamos o comando _login_ para ativar o acesso EXEC do usuário;
 * por fim use o comando _end/exit_ caso você queira sair do modo global.

Pronto agora o console vai pedir uma senha para quem for usar o EXEC de usuário.

**Colocando senha no EXEC privilegiado**:
 * Entra no modo EXEC global;
 * Usa o comando _line console 0_;
 * Usa o comando _enable secret (insira a senha aqui)_;
 * Use o comado _end/exit_ para sair do modo global se desejado.

### Configurando a senha do VTY

As linhas de terminal virtual (VTY) permitem acesso remoto usando Telnet ou SSH ao dispositivo.

**Colocando a senha no VTY**:
 * Entre no Modo EXEC global;
 * Entre no Modo VTY, usando o comando _line vty 0 15_ ( a gente pode configurar cada porta individualmente digitando o número da porta, mas caso a gente queira configurar todas de uma vez a gente usa esse 0 15);
 * Use o comando _password (insira senha aqui)_;
 * Use o comando _login_;
 * E se necessário use o comando _end/exit_ para sair do modo vty.

### Criptografando as senhas

Os arquivos startup-config e running-config exibem a maioria das senhas em texto simples. O que torna isso uma ameaça pois assim qualquer pessoa spode ver as senhas se conseguir acesso a esses arquivos.
**para criptografar as nossas senhas seguimos os seguintes passos**:
 * primeiro entramos no modo de comfiguração global da máquina (usa o _config terminal_)
 * E aí usamos o comando **service password-encryption**

O comando **service password-encryption** serve para aplicar uma criptografia fraca todas as senhas não criptografadas nos arquivos de configuração (startup-config e running-config). Ou seja esse comando serve para proibir pessoas não autorizadas vejam as senhas nos arquivos.

Caso você deseje verificar se as senhas estão realmente encriptografadas, _use o comando **show running-config**_

### mensagens de Banner

Essas mensagens servem para avisar que só pessoal autorizado pode acessar aqueles arquivos e etc, auxiliar em processos legais caso alguém seja processado pela invasão de um dispositivo. Sem contar que alguns sistemas legais/jurídicos não permitem que processos ou monitoramento de usuários, ocorra sem que haja um aviso visível.

Para criar esses banner usamos o comando **banner motd #mensagem do banner aqui#**, nesse caso o "#" na sintaxe é um caractere de delimitação. **OBS: _QUALQUER_ caractere pode ser usado como caractere de delimitação _CONTANTO_ que esse caractere não apareça na msg do banner**. Pronto, após a execução do comando, o banner sempre será exibido em qualquer tentativa de acessar o disposito, até que o banner seja removido

## Salvar configurações

### Arquivos de Configuração

Existem dois arquivos que armezam as configurações do Dispositivo:

**startup-config**: Este arquivo é armazenado na NVRAM. Ele contém todos os comandos que o dispositivo usará na (re)inicialização. O flash não perde sue conteúdo quando o dispositivo está desligado.

**running-config**: É armazenado na RAM, ele reflete a configuração atual. Modificar uma configuração ativa afeta o funcionamento do dispositivo. Quando o dispositivo é desligado todo o conteúdo é perdido.

No modo EXEC privilegiado podemos usar o comando _show running-config_ para visualizarmos as configurações de execução que estão armazenadas na RAM.
E pra ver as informações do arquivo _startup-config_ basta também usar o comando SHOW.

Para salvarmos os dados de configurações e evitar suas perdas caso o dispositivo seja desligado, podemos usar o comando **copy nomeDoArquivo(EX: startup-config running-config)** no modo privilegiado.

para salvarmos as configurações atuais em execução usamos **copy running-config startup-config** assim estaremos colocando os arquivos do running no startup, mas se nós fizermos o contrário **copy startup-config running-config** Nós básicamente retornaremos as ultimas configurações salvas para a execução atual.

### Alterando configurações ativas

Caso nós desejemos voltar o dispositivo para a configuração anterior podemos remover os comandos alterados individualmente, ou podemos usar o comando **reload** para restaurar o _startup-config.

**OBS: tenha cuidado ao usar o comando RELOAD, pois após o seu uso o dispositivo ficará alguns momentos Offline, causando assim tempo de inatividade na rede.**

Quando um reload é iniciado o IOS percebe que há configurações não salvas, assim ela irá mostrar um prompt perguntando se nós desejamos salvar as configurações, podemos responder _yes, y, no ou n_ para essa pergunta.

E em casos que configurações indesejadas foram salvas no startup-config, pode ser necessário limpar todas as configurações e reiniciar o dispositivo, para fazermos isso podemos usar o comando **erase nomeDoArquivo(EX: startup-config)**.

# Portas e Endereços

## Endereços IP

Endereços de IP são o principal meio de permitir que os dispositivos se localizem e estabeleçam uma comunicação ponto a ponto na internet. _Todo dispositivo final de uma rede deve ter um endereço IP.

### Estrutura do endereço IPv4

A estrutura desse tipo de endereço é chamada de notação decimal com ponto, sendo representada por **quatro números decimais entre 0 e 255**.

Nesse tipo de endereço uma mascára de sub-rede é necessária. Essa mascára de sub-rede é um **valor 32 bits**, que diferencia a parte da rede do endereço da parte host.
Juntando isso com o IPv4, a máscara de sub-rede determina qual sub-rede o dispositivo é membro.
O endereço de gateway padrão é o endereço IP do roteador que o host usará para acessar redes remotas, incluindo a Internet.

### O IPv6

Esses endereços têm 128 bits