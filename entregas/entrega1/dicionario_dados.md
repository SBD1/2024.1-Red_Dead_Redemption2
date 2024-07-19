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
| idInstanciaAnimal | Código identificador único da instancia animal | int | 1-5000 | pk | not null |
| idAnimal | Código identificador único do animal | int | 1-5000 | pk, fk2 | not null |
| vidaAtual | Vida que o animal possui no momento | int | 1-100 | | not null, default = 1 |
| staminaAtual | Energia atual do animal | int | 1-100 | | not null, default = 1 |
| idSala | Código identificar da sala onde o animal está | int | 1-100 | fk3 | |
| idPersonagemDono | Código que identifica o dono do animal | int | 1-100 | fk4 | |


### Tabela: ANIMAL_TIPO

- Descrição da Tabela: Tabela que identifica o tipo de cada animal no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int | 1-5000 | pk | not null |
| tipo | Identifica o tipo de animal | vachar[30] | a-z, A-Z |  | not null |


### Tabela: ANIMAL_AMIGAVEL

- Descrição da Tabela: Tabela que armazena informações detalhadas sobre animais amigáveis, incluindo características físicas e habitat.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int | 1-5000 | pk | not null |
| idRegiaoHabitatNatural | Código identificador da região (habitat) onde vive o animal | int | 1-5000 | fk1 | not null |
| especie | Espécie do animal | vachar[30] | a-z, A-Z | | not null |
| velocidade | Velocidade máxima que o animal pode atingir | int | 1-200 | | not null |
| vidaMax | Expectativa de vida máxima do animal em anos | int | 1-30 |  | not null |
| staminaAtual | Energia atual do animal | int | 1-100 |  | not null |
| textura | Tipo de textura da pele do animal | vachar[30] | a-z, A-Z | | not null |


### Tabela: ANIMAL_HOSTIL

- Descrição da Tabela: Tabela que armazena informações detalhadas sobre animais hostis, incluindo características físicas e habitat.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAnimal | Código identificador único do animal | int | 1-5000 | pk | not null |
| idRegiaoHabitatNatural | Código identificador da região (habitat) onde vive o animal | int | 1-5000 | fk1 | not null |
| especie | Espécie do animal | vachar[30] | a-z, A-Z | | not null |
| velocidade | Velocidade máxima que o animal pode atingir | int | 1-200 | | not null |
| vidaMax | Expectativa de vida máxima do animal em anos| int | 1-30 |  | not null |
| staminaAtual | Energia atual do animal | int | 1-100 |  | not null |
| textura | Tipo de textura da pele do animal | vachar[30] | a-z, A-Z | | not null |


### Tabela: JOGADOR_DOMA_ANIMAL_AMIGÁVEL

- Descrição da Tabela: Esta tabela registra os casos em que um jogador conseguiu domesticar um animal amigável. Cada registro na tabela associa um jogador a uma instância específica de um animal amigável que ele domou.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaAnimal | Código identificador único da instancia animal | int | 1-5000 | pk, fk1 | not null |
| idPersonagem | Código identificador único de um personagem (Jogador) | int | 1-5000 | pk,fk2 | not null |


### Tabela: ANIMAL_HOSTIL_POSSUI_ATAQUE

- Descrição da Tabela: Tabela que relaciona animais hostis com seus modos de ataque, indicando quais ataques cada animal pode realizar.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAtaque | Código identificador único do modo de ataque do animal | int | 1-5000 | pk,fk1 | not null |
| idAnimal | Código identificador único do animal | int | 1-5000 | pk,fk2 | not null |


### Tabela: ATAQUE

- Descrição da Tabela: Tabela que armazena informações sobre os diferentes tipos de ataques que um animal pode realizar.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idAtaque | Código identificador único do modo de ataque do animal | int | 1-5000 | pk,fk1 | not null |
| descricao | Descreve como o animal realiza o seu ataque | vachar[100] | a-z, A-Z | | not null |
| dano | Valor do dano que o animal realiza ao atacar | int | 1-200 |  | not null |


### Tabela: ANIMAL_HOSTIL_ATACA_JOGADOR

- Descrição da Tabela: Esta tabela registra os eventos em que um animal hostil atacou um jogador. Cada registro na tabela associa um jogador a uma instância específica de um animal hostil que o atacou.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaAnimal | Código identificador único da instancia animal | int | 1-5000 | pk, fk1 | not null |
| idPersonagem | Código identificador único de um personagem | int | 1-5000 | pk,fk2 | not null |


### Tabela: PERSONAGEM_TIPO

- Descrição da Tabela: Tabela que identifica o tipo de cada animal no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem | int | 1-5000 | pk | not null |
| tipo | Identifica o tipo de personagem  | vachar[30] | a-z, A-Z |  | not null |


### Tabela: MISSÃO

- Descrição: Armazena informações sobre as missões disponíveis no jogo

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idMissão | Código identificador único de uma missão | int | 1-5000 | pk | not null |
| título | Nome da missão | vachar[60] | a-z, A-Z | | not null |
| nivelDificuldade | Nível do quão complicado é a missão | vachar[60] | a-z, A-Z | | not null |
| idHistoria | Código identificador único de uma história | int | 1-5000 | fk1 | not null |
| idRegiao | Código identificador da região onde será realizado a missão | int | 1-5000 | fk2 | not null |
| status | Como está o andamento da missão | vachar[60] | a-z, A-Z |  |  |
| idPersonagem | Código identificador único de um personagem | int | 1-5000 | fk3 | not null |


### Tabela: MISSÃO_DEPENDE_DE_MISSAO

- Descrição: Define dependências entre missões, indicando quais missões precisam ser concluídas antes de iniciar outra. 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idMissaoAtual | Código identificador da Missão que está sendo realizada | int | 1-5000 | pk,fk1 |
| idMissaoAnterior | Código identificador da Missão da qual a MissaoAtual necessita para ser realizada | int | 1-5000 | pk,fk2 |


### Tabela: OBJETIVO

- Descrição: Armazena objetivos específicos dentro das missões, incluindo recompensas em XP e dinheiro.

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idObjetivo | Código identificador do objetivo da missão | int | 1-5000 | pk |
| título | Nome do objetivo | vachar[60] | a-z, A-Z | | not null |
| retornoXp | Texto que descreve o propósito da missão | int | 1-10000 | | not null |
| retornoDinheiro | Texto que descreve o propósito da missão | int | 1-10000 | | not null |
| idMissão | Código identificador único de uma missão | int | 1-5000 | fk1 | not null |


### Tabela: HISTORIA

- Descrição: Contém as histórias que embasam as missões do jogo, incluindo títulos e enredos.

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| idHistoria | Código identificador do objetivo da historia da missão | int | 1-5000 | pk | not null |
| título | Nome da missão  | vachar[60] | a-z, A-Z | | not null |
| enredo | Texto que a história por trás da missão | vachar[1000] | a-z, A-Z | | not null |


### Tabela: NPC

- Descrição da Tabela: Registra informações sobre os NPCs (Personagens Não Jogadores) no jogo

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem | int | 1-5000 | pk | not null |
| nome | Nome pelo qual o NPC é identificado  | vachar[30] | a-z, A-Z |  | not null |
| velocidade | Velocidade que o NPC alcança | int | 1-40 |  | |
| idInventario | Código identificador úncio de um inventário  | int | 1-5000 | fk1 | not null |
| vidaMax | Expectativa de vida máxima do animal em anos  | int | 1-100 |  | not null |
| idClasse | Código identificador único da classe que o NPC participa | int | 1-5000 | fk2 | not null |
| idGuange | Código identificador único da guange que o NPC participa  | int | 1-5000 | fk3 | |


### Tabela: INSTANCIA_NPC

- Descrição da Tabela: Registra instâncias específicas de NPCs

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaNPC | Código identificador único de um personagem | int | 1-5000 | pk | not null |
| idPersonagem | Código identificador único de um personagem | int | 1-5000 | pk,fk | not null |
| vidaAtual | Identifica a vida restante da Instancia NPC | int | 1-100 | | not null |
| idMissão | Código identificador único de uma missão | int | 1-5000 | pk, fk1 | |
| idGuange | Código identificador único da guange que o NPC participa  | int | 1-5000 | pk,fk2 | |


### Tabela: GANGUE

- Descrição: Armazenará as informações sobre as formações de gangues rivais no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| id_gangue | Código identificador único da gangue | int |  | pk | not null |
| nome | Nome da gangue | vachar[30] | a-z, A-Z | | not null |
| descrição | Informações importantes para a caracterização da gangue | vachar[60] | a-z, A-Z | not null |
| idInstanciaNPCLíder | Id do personagem que lidera a gangue (jogador ou instância de NPC) | int | 1-5000 | fk1 | not null |


### Tabela: HABILIDADE

- Descrição: Armazenará as informações sobre as habilidades de uma classe.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_habilidade | Código identificador único da habilidade | int |  | pk, identity |
| nome | Nome da habilidade | char | 15 | sk |
| porcentagem | Porcentagem da habilidade que será acrescida às capacidades existentes do personagem | float |  | not null, min = 0.0, max = 1.0 |
| id_classe | Id da classe à qual pertence a habilidade | int |  | fk |


### Tabela: HISTÓRIA

- Descrição: Armazenará as informações das histórias.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_história | Código de identificação único da história. | int |  | pk, identity |
| título | Nome da história | char | 500 | sk |
| enredo | Texto do enredo da história | char | 1000 | not null |


### Tabela: INSTÂNCIA_ANIMAL

- Descrição: Armazenará as informações das instâncias de animais vivas no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_instância_animal | Código identificador da instância do animal | int |  | pk, identity |
| id_animal | Código identificador da espécie de animal | int |  | fk |
| vida_atual | Vida atual de uma instância de animal | int |  | not null |
| stamina_atual | Energia atual que a instância tem para se movimentar | int |  | not null |


### Tabela: INSTÂNCIA_ARMA_FOGO

- Descrição: Armazenará as informações sobre as instâncias de armas de fogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_inst_arma_fogo | Código identificador único da instância de arma de fogo | int |  | pk, identity |
| id_arma_fogo | Código identificador do tipo de arma | int |  | fk |
| id_inventário | Código do inventário do personagem que utiliza a instância da arma | int |  | fk |


### Tabela: INSTÂNCIA_ARMA_MELEE

- Descrição: Armazenará as informações sobre as instâncias de armas melee.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_inst_arma_melee | Código identificador único da instância de arma melee | int |  | pk, identity |
| id_arma_melee | Código identificador do tipo de arma | int |  | fk |
| id_inventário | Código do inventário do personagem que utiliza a instância da arma | int |  | fk |


### Tabela: INSTÂNCIA_ESTABELECIMENTO

- Descrição: Armazenará as informações sobre as instâncias de estabelecimento que serão geradas no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_estab | Código identificador do tipo de estabelecimento | int |  | pk |
| id_região | Código da região onde instância do estabelecimento se encontra | int |  | pk |
| id_instância_npc_dono | Código da instância de NPC proprietária da instância do estabelecimento | int |  | pk |

### Tabela: INSTÂNCIA_ITEM

- Descrição: Armazenará as informações sobre as instâncias de item. 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_inst_item | Código identificador único da instância de item  | int |  | pk, identity |
| id_item | Código do tipo de item | int |  | fk |
| id_inventário | Código do inventário ao qual o a instância está depositada | int |  | fk |
| tipo | Consumível ou Equipável | int |  | Consumível = 0, Equipável = 1 |


### Tabela: INSTÂNCIA_NPC

- Descrição: Armazenará as informações relativas às instâncias de NPC.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |              
| --- | --- | --- | --- | --- |
| id_instância_npc | Código identificador da instância de NPC | int |  | pk, identity |
| id_npc | Código do tipo de NPC ao qual a instância pertence | int |  | fk |
| id_inventário | Código identificador do inventário de um jogador | int |  | fk |
| id_gangue | Código identificador da gangue à qual pertence um jogador | int |  | fk |
| vida_atual | Vida atual da instância | int |  | not null |
| id_missão | Código da missão que uma instância participa. Pode ser nulo (não participa de nenhuma missão) | int |  | fk |


### Tabela: INVENTÁRIO

- Descrição: Armazenará as informações sobre o inventário dos personagens (jogadores e instâncias de NPC).
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_inventário | Código identificador do inventário | int |  | pk, identity |
| id_personagem | Código identificador do dono do inventário | int |  | fk |
| capacidade | Total de itens que um inventário pode suportar | int |  | not null, default = 30 |
| total_itens | Total de itens presentes em um inventário | int |  | min = 0, max = capacidade |


### Tabela: ITEM_CONSUMÍVEL

- Descrição: Armazenará as informações sobre os tipos de itens consumíveis do jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_item | Código identificador único do item | int |  | pk, identity |
| nome | Nome do item | char | 10 | not null |
| reparação_vida | Quantidade de pontos de vida que o jogador receberá ao consumir o item | int |  | not null |
| reparação_stamina | Quantidade de pontos de stamina que o jogador receberá ao consumir o item | int |  | not null |

### Tabela: ITEM_EQUIPÁVEL

- Descrição: Armazenará as informações sobre os tipos de itens equipáveis do jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_item | Código identificador único do item | int |  | pk, identity |
| nome | Nome do item | char | 10 | not null |
| parte_corpo | Parte do corpo que o item cobre | char | 10 | not null |



### Tabela: JOGADOR

- Descrição: Armazenará as informações sobre os jogadores (pessoas reais).
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_personagem | Código identificador único do personagem | int |  | pk, identity |
| nome | Nome do personagem | char | 12 | not null |
| velocidade | Velocidade máxima com que um personagem consegue se deslocar | int |  | not null, min = 1, max = 10 |
| id_inventário | Código identificador do inventário de um jogador | int |  | fk |
| vida_máx | Vida que o jogador recebe ao ser gerado | int |  | not null, default = 100 |
| id_classe | Código identificador da classe do personagem | int |  | fk |
| id_gangue | Código identificador da gangue à qual pertence um jogador | int |  |  |
| xp | Quantidade de xp do jogador | int |  | default = 0 |
| dinheiro | Quantidade de dinheiro em moedas do jogador | int |  | default = 0 |
| vida_max | Vida máxima do jogador | int |  |  |
| vida_atual | Vida atual do jogador | int |  | default = vida_max |
| stamina_max | Quantidade de stamina máxima do jogador | int |  |  |
| stamina_atual | Quantidade de stamina atual do jogador | int |  | default = 0 |


### Tabela: LINHA_FALA

- Descrição: Armazenará as linhas de fala de um diálogo. 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_diálogo | Código identificador único do diálogo | int |  | fk |
| id_linha_fala | Código identificador (fraco) da linha de fala | int |  | pk, identity |
| texto_de_fala | Texto propriamento dito falado pelo personagem  | char | 150 | not null |


### Tabela: MAPA

- Descrição: Armazenará as informações dos mapas do jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_mapa | Código identificador único do mapa | int |  | pk, identity |
| nome | Nome do mapa | char | 20 | not null |


### Tabela: MISSÃO

- Descrição: Armazenará as informações das missões.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_missão | Código identificador único da missão | int |  | pk, identity |
| título | Título da missão | char | 50 | sk |
| nível_dificuldade | Nível dificuldade da missão | int |  | not null, default = 1, min = 1, max = 10 |
| id_história | Código identificador da história contada na missão | int |  | fk |
| id_região | Código identificador de qual região se passa uma determinada missão | int |  | fk |
| status | Código de status da missão | int |  | not null, valores possíveis = {0: iniciado, 1: em andamento , 2: concluído} |

### Tabela: MISSÃO_REQUER_MISSÃO

- Descrição: Armazena as dependências entre as missões.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_missão | Código identificador da missão. | int |  | pk, fk |
| id_missão_requisito | Código identificador da missão-requisito | int |  | pk, fk |


### Tabela: NPC

- Descrição: Armazenará as informações sobre os tipos de NPCS disponíveis no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_npc | Código identificador único do NPC | int |  | pk, identity |
| nome | Nome do NPC | char | 12 | not null |
| velocidade | Velocidade máxima com que um NPC consegue se deslocar | int |  | not null, min = 1, max = 10 |
| vida_máx | Vida que o jogador recebe ao ser gerado | int |  | not null, default = 100 |
| id_classe | Código identificador da classe do personagem | int |  | fk |

### Tabela: OBJETIVO

- Descrição: Armazenará os objetivos de uma missão.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_objetivo | Código de identificação único do objetivo. | int |  | pk, identity |
| título | Descrição do objetivo. | char | 100 | sk |
| retorno_xp | Total de xp's que um jogador receberá ao completar um determinado objetivo. | int |  | not null, default = 0 |
| retorno_dinheiro | Total em moedas que um jogador receberá ao completar um determinado objetivo. | int |  | not null, default = 0 |
| id_missão | Código identificador da missão à qual o objetivo pertence. | int |  | fk |


### Tabela: PROJÉTIL

- Descrição: Armazenará as informações sobre os projéteis disparados no mapa pelos personagens.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_projétil | Código identificador único do projétil disparado | int |  | pk, identity |
| id_inst_arma_fogo | Código da instância da arma de fogo que disparou o projétil | int |  | fk |
| posição_x | Posição x atual do projétil no mapa | int |  | not null |
| posição_y | Posição y atual do projétil no mapa | int |  | not null |
| posição_z | Posição z atual do projétil no mapa | int |  | not null |
| colidiu | Registra se o projétil colidiu com algum objeto do mapa | bool |  | not null, default = false |
| velocidade | Velocidade de deslocamento do projétil | int |  | not null, default = 500 |


### Tabela: REGIÃO

- Descrição: Armazenará as informações das regiões do jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_região | Código identificador único da região | int |  | pk, identity |
| id_mapa | Código identificador do mapa ao qual a região pertence | int |  | fk |
| nome | Nome da região | char | 15 | not null |
| descrição | Descrição da região | char | 50 | not null |

### Tabela: REGIÃO_FAZ_FRONTEIRA_COM_REGIÃO

- Descrição: Armazenará as informações de como as regiões de um mapa se conectam.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_mapa | Código identificador do mapa ao qual a região pertence | int |  | pk, fk |
| id_região | Código identificador único da região | int |  | pk, fk |
| id_região | Código identificador único da região fronteiriça | int |  | pk, fk |