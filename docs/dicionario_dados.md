# Dicionário de dados

<!-- Copiar o modelo abaixo -->

<!-- ### Tabela: NOME

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  | -->

### Tabela: INSTANCIA_ANIMAL

- Descrição da Tabela: Instância específica de um animal no sistema, contendo informações sobre sua vida atual, energia e localização.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaAnimal | Código identificador único da instancia animal | int |  | pk | not null |
| idAnimal | Código identificador único do animal | int |  | pk, fk1 | not null |
| vidaAtual | Vida que o animal possui no momento | int | 1-100 | | not null, default = 100 |
| staminaAtual | Energia atual do animal | int | 1-100 | | not null, default = 100 |
| idSala | Código identificar da sala onde o animal está | int |  | fk3 | |


### Tabela: ANIMAL_TIPO

- Descrição da Tabela: Tabela que identifica o tipo de cada animal no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int |  | pk | not null |
| tipo | Identifica o tipo de animal | int |  |  | not null |


### Tabela: ANIMAL_AMIGAVEL

- Descrição da Tabela: Tabela que armazena informações detalhadas sobre animais amigáveis, incluindo características físicas e habitat.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int |  | pk, fk1 | not null |
| idRegiaoHabitatNatural | Código identificador da região (habitat) onde vive o animal | int |  | fk2 | not null |
| especie | Espécie do animal | varchar[30] | a-z, A-Z | | not null |
| velocidade | Velocidade máxima que o animal pode atingir | int | 1-100 | | not null |
| vidaMax | Expectativa de vida máxima do animal em anos | int | 1-100 |  | not null |
| staminaMAx | Energia máxima do animal | int | 1-100 |  | not null |
| textura | Tipo de textura da pele do animal | varchar[30] | a-z, A-Z | | not null |


### Tabela: ANIMAL_HOSTIL

- Descrição da Tabela: Tabela que armazena informações detalhadas sobre animais hostis, incluindo características físicas e habitat.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int |  | pk, fk1 | not null |
| idRegiaoHabitatNatural | Código identificador da região (habitat) onde vive o animal | int |  | fk2 | not null |
| especie | Espécie do animal | varchar[30] | a-z, A-Z | | not null |
| velocidade | Velocidade máxima que o animal pode atingir | int | 1-100 | | not null |
| vidaMax | Expectativa de vida máxima do animal em anos| int | 1-100 |  | not null |
| staminaMax | Energia máxima do animal | int | 1-100 |  | not null |
| textura | Tipo de textura da pele do animal | varchar[30] | a-z, A-Z | | not null |


### Tabela: JOGADOR_DOMOU_ANIMAL_AMIGAVEL

- Descrição da Tabela: Esta tabela registra os casos em que um jogador conseguiu domesticar um animal amigável. Cada registro na tabela associa um jogador a uma instância específica de um animal amigável que ele domou.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaAnimal | Código identificador único da instancia animal | int |  | pk, fk1 | not null |
| idJogador | Código identificador único de um jogador | int |  | pk,fk2 | not null |


### Tabela: ANIMAL_HOSTIL_POSSUI_ATAQUE

- Descrição da Tabela: Tabela que relaciona animais hostis com seus modos de ataque, indicando quais ataques cada animal pode realizar.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAtaque | Código identificador único do modo de ataque do animal | int |  | pk,fk1 | not null |
| idAnimal | Código identificador único do animal | int |  | pk,fk2 | not null |


### Tabela: ATAQUE

- Descrição da Tabela: Tabela que armazena informações sobre os diferentes tipos de ataques que um animal pode realizar.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAtaque | Código identificador único do modo de ataque do animal | int |  | pk,fk1 | not null |
| descricao | Descreve como o animal realiza o seu ataque | varchar[100] | a-z, A-Z | | not null |
| dano | Valor do dano que o animal realiza ao atacar | int | 1-100 |  | not null |


### Tabela: ANIMAL_HOSTIL_ATACA_JOGADOR

- Descrição da Tabela: Esta tabela registra os eventos em que um animal hostil atacou um jogador. Cada registro na tabela associa um jogador a uma instância específica de um animal hostil que o atacou.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaAnimal | Código identificador único da instancia animal | int |  | pk, fk1 | not null |
| idJogador | Código identificador único de um personagem | int |  | pk,fk2 | not null |


### Tabela: PERSONAGEM_TIPO

- Descrição da Tabela: Tabela que identifica o tipo de cada animal no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem | int |  | pk | not null |
| tipo | Identifica o tipo de personagem  | varchar[30] | a-z, A-Z |  | not null |


### Tabela: MISSÃO

- Descrição: Armazena informações sobre as missões disponíveis no jogo

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idMissao | Código identificador único de uma missão | int |  | pk | not null |
| titulo | Nome da missão | varchar[60] | a-z, A-Z | | not null |
| nivelDificuldade | Nível do quão complicado é a missão | int | 1-10 | | not null |
| idHistoria | Chave estrangeira da história que representa a história contada na missão. | int |  | fk1 | not null |
| idRegiao | Chave estrangeira da região onde se passa a missão. | int |  | fk2 | not null |
| status | Porcentagem de andamento da missão. Corresponde ao número de objetivos completados associados à missão. | decimal(3,2) | 0.00 - 1.00 |  |  |

### Tabela: MISSÃO_DEPENDE_DE_MISSAO

- Descrição: Define dependências entre missões, indicando quais missões precisam ser concluídas antes de iniciar outra. 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idMissaoAtual | Código identificador da Missão que está sendo realizada | int |  | pk,fk1 |
| idMissaoAnterior | Código identificador da Missão da qual a MissaoAtual necessita para ser realizada | int |  | pk,fk2 |


### Tabela: OBJETIVO

- Descrição: Armazena objetivos específicos dentro das missões, incluindo recompensas em XP e dinheiro.

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idObjetivo | Código identificador do objetivo da missão | int |  | pk |
| titulo | Nome do objetivo | varchar[60] | a-z, A-Z | | not null |
| retornoXP | Retorno em xp que um jogador receberá ao completar a missão com êxito. | int | 1-1000 | | not null |
| retornoDinheiro | Retorno em dinheiro que um jogador receberá ao completar a missão com êxito. | int | 1-1000 | | not null |
| idMissão | Chave estrangeira para a missão à qual o objetivo está associado. | int |  | fk1 | not null |


### Tabela: HISTORIA

- Descrição: Contém as histórias que embasam as missões do jogo, incluindo títulos e enredos.

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idHistoria | Código identificador do objetivo da historia da missão | int |  | pk | not null |
| titulo | Nome da missão  | varchar[60] | a-z, A-Z | | not null |
| enredo | Texto que a história por trás da missão | varchar[1000] | a-z, A-Z | | not null |


### Tabela: NPC

- Descrição da Tabela: Registra informações sobre os NPCs (Personagens Não Jogadores) no jogo

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem | int |  | pk, fk1 | not null |
| nome | Nome pelo qual o NPC é identificado  | varchar[30] | a-z, A-Z |  | not null |
| velocidade | Velocidade que o NPC alcança | int | 1-10 |  |  |
| vidaMax | Quantidade de vida que o NPC recebe ao nascer.  | int | 1-100 |  | not null, default = 100 |
| staminaMax | Quantidade de stamina que um NPC recebe ao nascer. | int | 1-1000 |  | not null, default = 1000 |


### Tabela: INSTANCIA_NPC

- Descrição da Tabela: Registra instâncias específicas de NPCs

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaNPC | Código identificador único de uma instância de NPC | int |  | pk | not null |
| idPersonagem | Chave estrangeira para o NPC que a instância se refere | int |  | pk,fk1 | not null |
| idGangue | Chave estrangeira para a gangue da qual a instância de NPC faz parte  | int |  | pk,fk2 | |
| idInventario | Chave estrangeira para a o inventário da instância de NPC. | int |  | pk,fk3 | |
| idMissao | Chave estrangeira para a missão da qual a instância de NPC faz parte | int |  | pk, fk4 | |
| idSala | Código identificador da sala em que a instância está presente | int |  | fk5 | not null |
| vidaAtual | Identifica a vida restante da instância de NPC | int | 1-100 | | not null, default = 100 |


### Tabela: GANGUE

- Descrição: Armazenará as informações sobre as formações de gangues rivais no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idGangue | Código identificador único da gangue | int |  | pk | not null |
| nome | Nome da gangue | varchar[30] | a-z, A-Z | | not null |
| descricao | Informações importantes para a caracterização da gangue | varchar[60] | a-z, A-Z | not null |
| idInstanciaNPCLider | Chave estrangeira para a instância de NPC que lidera a gangue. | int |  | fk1 | not null |


### Tabela: GANGUE_CONFRONTA_GANGUE

- Descrição: Armazenará as informações sobre as formações de gangues rivais no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idGangueVencedora | Chave estrangeira para o código da gangue que venceu o combate. | int |  | pk,fk1 | not null |
| idGanguePerdedora | Chave estrangeira para o código da gangue que perdeu o combate. | int |  | pk, fk2 | not null |
| dataConfronto | Data de quando ocorreu o confronto. | date |  | not null |


### Tabela: DIALOGO

- Descrição: Esta tabela armazena informações sobre diálogos no contexto de um sistema de jogo ou simulação.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idDialogo | Código identificador único de um diálogo | int |  | pk | not null |
| idInstanciaNPCFalante | Chave para a instância de NPC que fala o referido diálogo. | int |  | fk1 | not null |
| descricao | Descrição do diálogo | varchar[100] | a-z, A-Z | not null |


### Tabela: LINHA_DE_FALA

- Descrição: Esta tabela contém as linhas de fala que compõem os diálogos registrados no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idLinhaDeFala | Código identificador da linha de fala de um diálogo | int |  | pk | not null |
| idDialogo | Código identificador único de um diálogo | int |  | pk,fk | not null |
| texto | Texto da linha de fala. | varchar[100] | a-z, A-Z | not null |


### Tabela: CLASSE

- Descrição: Armazena as informações sobre as classes disponíveis no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idClasse | Código para identificar a classe disponíveis no jogo | int |  | pk | not null |
| nome | Nome da classe | varchar[20] | a-z, A-Z |  | not null |


### Tabela: CLASSE_POSSUI_HABILIDADE

- Descrição: Armazena as habilidades associadas a cada classe no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idClasse | Código para identificar a classe disponíveis no jogo | int |  | pk,fk1 | not null |
| idHabilidade | Código identificador único da habilidade específica de uma classe | int |  | pk,fk2 | not null |


### Tabela: HABILIDADE

- Descrição: Armazena as habilidades que podem ser possuídas pelas classes.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idHabilidade | Código identificador único da habilidade específica de uma classe | int |  | pk | not null |
| nome | Nome da habilidade | varchar[30] | a-z, A-Z | | not null |
| porcentagem | Porcentagem da habilidade acrescentada às características do personagem (NPC ou jogador) | decimal(3,2) | 0.00 - 1.00 | | not null |


### Tabela: PERSONAGEM_TIPO

- Descrição: Esta tabela classifica os personagens em diferentes tipos, permitindo a categorização e filtragem no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem | int |  | pk | not null |
| tipo | Identifica o tipo de personagem | int | a-z, A-Z |  | not null |


### Tabela: JOGADOR

- Descrição: Contém informações sobre os jogadores, incluindo desempenho, progresso e modos de autenticação

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um jogador. É chave estrangeira para a tabela de tipos (personagem_tipo) | int |  | pk, fk1 | not null |
| idInventario | Código identificador úncio de um inventário | int |  | fk2 | not null |
| idSala | Código identificador da sala em que o jogador está presente | int |  | fk3 | not null |
| idClasse | Código para identificar a classe a qual o jogador pertence | int |  | fk4 | not null |
| idGangue | Código para identificar a gangue a qual o jogador pertence | int |  | fk5 | |
| nome | Nome de um jogador específico | varchar[30] | a-z, A-Z | | not null |
| xp | Pontuação para medir o progresso e a evolução de um jogador | int |  |  | default = 0 |
| dinheiro | Valor total de dinheiro que o jogador possui | int |  |  | default = 0 |
| velocidade | Velocidade que o jogador alcança | int | 1-10 |  | default = 7 |
| vidaMax | Quantidade de vida máxima que um jogador pode ter. Corresponde àquela que ele recebe ao nascer. | int | 1-100 |  | default = 100, not null |
| vidaAtual | Vida que o jogador possui no momento | int | 1-100 |  | not null, default = 100 |
| staminaMax | Energia Máxima que o jogador pode obter | int | 1-1000 |  | not null, default = 1000 |
| staminaAtual | Energia atual do jogador | int | 1-1000 |  | default = 1000 |
| username | Processo de autenticação que permite a um jogador acessar sua conta do jogador | varchar[30] | a-z, A-Z, @, #, $, %, . | | not null |
| senha_hash | Hash da senha do jogador, após processo de criptografia | varchar[255] | a-z, A-Z, @, #, $, %, . |  | not null |


### Tabela: JOGADOR_CUMPRE_MISSÃO

- Descrição: Registra a participação dos jogadores em missões, incluindo o progresso e recompensas obtidas.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idJogador | Chave estrangeira para o id do jogador que cumpriu a missão. | int |  | pk,fk1 | not null |
| idMissao | Chave estrangeira para a missão que o jogador completou. | int |  | pk,fk2 | not null |
| dataMissao | Data em que a missão foi realizada | date |  |  | not null |
| retornoTotalXP | Quantidade de XP obtido após o cumprimento da missão | int |  |  | not null |
| retornoTotalDinheiro | Quantidade de dinheiro obtido após o cumprimento da missão | int |  |  | not null |


### Tabela: INVENTARIO

- Descrição: Armazena informações sobre o inventário de um jogador, incluindo itens e capacidade.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInventario | Código identificador único de um inventário  | int |  | pk | not null |
| totalItens | Quantidade de itens (objetos) que o jogador possui | int |  | | default = 0 |
| capacidade | Capacidade máxima de Itens que o inventário consegue armazenar | int |  |  | not null |


### Tabela: ARMA_MELEE

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador da arma melee, sendo uma chave estrangeira para a tabela de tipos. | int |  | pk | not null |
| nome | Nome de uma arma específica | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da Arma | varchar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde a arma | int | 1-8 | | not null, default = 1 |
| preco | Custo total da arma | int |  |  | not null, default = 1 |
| durabilidadeMaxima | Quantidade máxima de vezes que uma arma pode ser utilizada. | int |  |  | not null |
| danoPorAtaque | Quantidade de vida que pode ser afeta ao sofrer um dano por ataque | int |  |  | not null |
| nivelAfiacao | Nível de afiação da arma. O nível de afiação aumenta o danoPorAtaque | int |  |  | not null |


### Tabela: ARMA_FOGO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador da arma de fogo, sendo uma chave estrangeira para a tabela de tipos. | int |  | pk | not null |
| nome | Nome de uma arma específica | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da Arma | varchar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde a arma | int | 1-8 | | not null, default = 1 |
| preco | Custo total da arma | int |  |  | not null, default = 1 |
| durabilidadeMaxima | Quantidade máxima de vezes que uma arma pode ser utilizada. | int |  |  | not null |
| danoPorAtaque | Quantidade de vida que pode ser afeta ao sofrer um dano por ataque | int |  |  | not null |
| velocidadeDisparo | Velocidade com a qual a arma dispara projéteis | int |  |  | not null |
| velocidadeReload | Tempo necessário para recarregar a arma | time |  |  | not null |


### Tabela: ITEM_TIPO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item | int |  | pk | not null |
| tipo | Identifica o tipo de item | int |  |  | not null |


### Tabela: ITEM_CONSUMIVEL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item consumível, sendo uma chave estrangeira para a tabela de tipos. | int |  | pk | not null |
| nome | Nome do item consumível | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do item | varchar[60] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde ao item | int | 1-8 | | not null |
| preco | Custo total da arma | decimal(3,2) |  |  | not null |
| durabilidadeMaxima | Quantidade máxima de vezes que um item pode ser utilizado. | int |  |  | not null |
| qtdReparacaoStamina | Quantidade de stamina restaurada ao utilizar o item consumível  | int | 1-1000 |  | not null |
| qtdReparacaoVida | Quantidade de vida restaurada ao utilizar o item consumível  | int | 1-100 | | not null |


### Tabela: ITEM_EQUIPAVEL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item equipável, sendo uma chave estrangeira para a tabela de tipos. | int |  | pk | not null |
| nome | Nome do item equipável | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do item | varchar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde ao item | int | 1-8 | | not null |
| preco | Custo total da arma | int |  |  | not null |
| durabilidadeMaxima | Quantidade máxima de vezes que um item pode ser utilizado. | int |  |  | not null |
| parteDoCorpo | Parte do corpo onde o item é equipado | varchar[30] | a-z, A-Z |  | not null |


### Tabela: INSTANCIA_ITEM

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaItem | Código identificador da instancia do item | int |  | pk | not null |
| idItem | Chave estrangeira para o tipo do qual deriva a instância | int |  | pk, fk1 | not null |
| idInventario | Chave estrangeira para o inventário que contém o item. Um item pode estar fora de um inventário. | int |  | fk2 |  |
| durabilidadeAtual | Durabilidade atual do objeto. A durabilidade atual é diminuída a cada uso do objeto. | int |  |  | not null |


### Tabela: PROJETIL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idProjetil | Código identificador de um projetil | int |  | pk | not null |
| idInstanciaItem | Chave estrangeira para o código da instância de arma de fogo que disparou o projétil | int |  | pk, fk1 | not null |
| posX | Coordenada X da posição do projetil no espaço | int | | | |
| posY | Coordenada Y da posição do projetil no espaço  | int |  |  |  |
| posZ | Coordenada Z da posição do projetil no espaço  | int |  |  |  |
| colidiu | Indica se o projetil colidiu com um objeto ou não | boolean |  |  | not null, default = false |
| velocidade | Velocidade do projétil em movimento | int | 1-1000 |  | not null |


### Tabela: REGIAO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idRegiao | Código identificador de uma região | int |  | pk | not null |
| idMapa | Código identificador do mapa onde está a região | int |  | fk1 | not null |
| nome | Nome de uma região específica | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da região | varchar[60] | a-z, A-Z |  | not null |


### Tabela: REGIAO_FAZ_FRONTEIRA_COM_REGIAO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idRegiaoOrigem | Código identificador da região de origem | int |  | pk, fk1 | not null |
| idRegiaoDestino | Código identificador da região de chegada | int |  | pk, fk2 | not null |


### Tabela: MAPA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idMapa | Código identificador de um mapa | int |  | pk | not null |
| nome | Nome de um mapa específico | varchar[30] | a-z, A-Z |  | not null |


### Tabela: ESTABELECIMENTO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idEstab | Código identificador de um mapa | int |  | pk | not null |
| nome | Nome de um estabelecimento específico | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do estabelecimento | varchar[60] | a-z, A-Z | | not null |


### Tabela: INSTANCIA_ESTABELECIMENTO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstEstab | Código identificador de uma instancia de um estabelecimento | int |  | pk | not null |
| idEstab | Código identificador do estabelecimento | int |  | pk, fk1 | not null |
| idSala | Código identificar da sala onde está presente o estabelecimento | int |  | fk2 | not null |
| idDono | Código identificador do dono da instância do estabelecimento. Pode ser um jogador ou uma instância de NPC. | int |  | fk3 | not null |

### Tabela: SALA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idSala | Código identificador de uma sala | int |  | pk | not null |
| idRegiao | Código identificador da região onde está a sala | int |  | fk1 | not null |
| nome | Nome de uma sala específica | varchar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da sala | varchar[60] | a-z, A-Z |  | not null |


### Tabela: SALA_CONECTA_COM_SALA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idSalaOrigem | Código identificador da sala de origem | int |  | pk, fk1 | not null |
| idSalaDestino | Código identificador da sala de chegada | int |  | pk, fk2 | not null |


## Histórico de versões

| Versão |    Data    | Descrição               |     
| :----: | :--------: | ----------------------- |
| `1.0`  | 08/05/2024 | Primeira versão completa do dicionário de dados |
| `2.0`  | 20/07/2024 | Segunda versão completa do dicionário de dados  |
| `2.1`  | 07/08/2024 | Correções pontuais pós-release.  |