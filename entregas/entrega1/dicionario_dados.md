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
| idInventario | Código identificador do inventário do NPC  | int | 1-5000 | fk1 | not null |
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

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idGangue | Código identificador único da gangue | int |  | pk | not null |
| nome | Nome da gangue | vachar[30] | a-z, A-Z | | not null |
| descrição | Informações importantes para a caracterização da gangue | vachar[60] | a-z, A-Z | not null |
| idInstanciaNPCLíder | Id do personagem que lidera a gangue (jogador ou instância de NPC) | int | 1-5000 | fk1 | not null |


### Tabela: GANGUE_CONFRONTA_GANGUE

- Descrição: Armazenará as informações sobre as formações de gangues rivais no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idGangueVencedora | Código identificador único da gangue | int | 1-5000 | pk,fk1 | not null |
| idGanguePerdedora | Código identificador único da gangue que está sendo desafiada | int | 1-5000 | pk, fk2 | not null |
| dataConfronto | Informações importantes para a caracterização da gangue | vachar[60] | 1-31, / | not null |


### Tabela: DIALOGO

- Descrição: Esta tabela armazena informações sobre diálogos no contexto de um sistema de jogo ou simulação.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idDialogo | Código identificador único de um diálogo | int | 1-5000 | pk | not null |
| idInstanciaNPCFalante | Id do NPC que está realizando o dialogo (jogador ou instância de NPC) | int | 1-5000 | fk1 | not null |
| descricao | Descrição da fala do qual o dialogo é composto | vachar[100] | a-z, A-Z | not null |


### Tabela: LINHA_DE_FALA

- Descrição: Esta tabela contém as linhas de fala que compõem os diálogos registrados no sistema.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idLinhaDeFala | Código identificar das linhas de fala dos diálogos | int | 1-5000 | pk | not null |
| idDialogo | Código identificador único de um diálogo | int | 1-5000 | pk,fk | not null |
| texto | Descrição da fala do qual o dialogo é composto | vachar[100] | a-z, A-Z | not null |

----------------------------------------------------------------------------------------------------------
### Tabela: CLASSE

- Descrição: Armazena as informações sobre as classes disponíveis no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idClasse | Código para identificar a classe disponíveis no jogo | int | 1-5000 | pk | not null |
| nome | Nome de uma classe específica | int | 1-5000 | | not null |


### Tabela: CLASSE_POSSUI_HABILIDADE

- Descrição: Armazena as habilidades associadas a cada classe no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idClasse | Código para identificar a classe disponíveis no jogo | int | 1-5000 | pk,fk1 | not null |
| idHabilidade | Código identificador único da habilidade específica de uma classe | int | 1-5000 | pk,fk2 | not null |


### Tabela: HABILIDADE

- Descrição: Armazena as habilidades que podem ser possuídas pelas classes.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idHabilidade | Código identificador único da habilidade específica de uma classe | int | 1-5000 | pk | not null |
| nome | Nome de uma classe específica | vachar[30] | a-z, A-Z | | not null |
| porcentagem | Porcentagem restante de uma habilidade | int | 1-100 | | not null |


### Tabela: PERSONAGEM_TIPO

- Descrição: Esta tabela classifica os personagens em diferentes tipos, permitindo a categorização e filtragem no jogo.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um jogador | int | 1-5000 | pk | not null |
| tipo | Identifica o tipo de personagem | vachar[30] | a-z, A-Z | | not null |


### Tabela: PERSONAGEM

- Descrição: Armazena informações detalhadas sobre cada personagem no jogo

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um jogador | int | 1-5000 | pk | not null |
| tipo | Identifica o tipo de personagem | vachar[30] | a-z, A-Z | | not null |


### Tabela: JOGADOR

- Descrição: Contém informações sobre os jogadores, incluindo desempenho, progresso e modos de autenticação

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem (Jogador) | int | 1-5000 | pk | not null |
| nome | Nome de um jogador específico | vachar[30] | a-z, A-Z | | not null |
| velocidade | Velocidade que o jogador alcança | int | 1-40 |  |  |
| idInventario | Código identificador úncio de um inventário | int | 1-5000 | fk1 | not null |
| vidaMax | Expectativa de vida máxima do jogador em anos | int | 1-120 |  | not null |
| idClasse | Código para identificar a classe a qual o jogador pertence | int | 1-5000 | fk2 | not null |
| idGangue | Código para identificar a gangue a qual o jogador pertence | int | 1-5000 | fk3 | |
| xp | Pontuação para medir o progresso e a evolução de um jogador | int | 1-10000 |  | default = 0 |
| dinheiro | Valor total de dinheiro que o jogador possui | int | 1-10000 |  | default = 0 |
| vidaAtual | Vida que o animal possui no momento | int | 1-100 |  | not null |
| staminaMax | Energia Máxima que o jogador pode obter | int | 1-5000 |  | not null |
| staminaAtual | Energia atual do jogador | int | 1-5000 |  | default = 0 |
| idSala | Código identificador da sala em que o jogador está presente | int | 1-5000 | fk4 | not null |
| login | Processo de autenticação que permite a um jogador acessar sua conta do jogador | vachar[30] | a-z, A-Z, @, #, $, %, . | | not null |
| senha | Combinação secreta de caracteres que um jogador utiliza para acessar a sua conta| vachar[30] | a-z, A-Z, @, #, $, %, . | | not null |


### Tabela: JOGADOR_CUMPRE_MISSÃO

- Descrição: Registra a participação dos jogadores em missões, incluindo o progresso e recompensas obtidas.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idPersonagem | Código identificador único de um personagem (Jogador) | int | 1-5000 | pk,fk1 | not null |
| idMissão | Código identificador da missão que o jogador está participando | int | 1-5000 | pk,fk2 | not null |
| data | Data em que a missão está sendo realizada | vachar[30] | 1-31, / | | not null |
| retornoTotalXP | Quantidade de XP obtido após o cumprimento da missão | int | 1-10000 | | not null |
| retornoTotalDinheiro | Quantidade de dinheiro obtido após o cumprimento da missão | int | 1-10000 | | not null |


### Tabela: INVENTARIO

- Descrição: Armazena informações sobre o inventário de um jogador, incluindo itens e capacidade.

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInventario | Código identificador úncio de um inventário  | int | 1-5000 | pk | not null |
| idPersonagem | Código identificador do personagem (Jogador) dono do inventário | int | 1-5000 | pk,fk1 | not null |
| totalItens | Quantidade de itens (objetos) que o jogador possui | int | 1-5000 | | default = 0 |
| capacidade | Capacidade máxima de Itens que o inventario consegue armazenar | int | 1-5000 | | not null, default = 1 |


### Tabela: ARMA_MELEE

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item (Arma)  | int | 1-5000 | pk | not null |
| nome | Nome de uma arma específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da Arma | vachar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde a arma | int | 1-8 | | not null, default = 1 |
| preco | Custo total da arma | int | 1-200 | | not null, default = 1 |
| durabilidadeMaxima | Tempo de durabilidade máxima da arma | int | 1-30 | | not null, default = 1 |
| danoPorAtaque | Quantidade de vida que pode ser afeta ao sofrer um dano por ataque | int | 1-5000 | | not null, default = 1 |
| nivelAfiação | Medida que indica o quão cortante ou perfurante é uma arma_melee | vachar[30] | a-z, A-Z | | not null |


### Tabela: ARMA_FOGO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item (Arma) | int | 1-5000 | pk | not null |
| nome | Nome de uma arma específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da Arma | vachar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde a arma | int | 1-8 | | not null, default = 1 |
| preco | Custo total da arma | int | 1-200 | | not null, default = 1 |
| durabilidadeMaxima | Tempo de durabilidade máxima da arma | int | 1-30 | | not null, default = 1 |
| danoPorAtaque | Quantidade de vida que pode ser afeta ao sofrer um dano por ataque | int | 1-5000 | | not null, default = 1 |
| velocidadeDisparo | Velocidade com a qual a arma dispara projéteis ou balas | int | 1-150 | | not null, default = 1 |
| velocidadeReload | Tempo necessário para recarregar a arma, descrito em formato textual (ex: "rápido", "lento") | vachar[30] | a-z, A-Z | | not null |


### Tabela: ITEM_TIPO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item | int | 1-5000 | pk | not null |
| tipo | Identifica o tipo de item | vachar[30] | a-z, A-Z |  | not null |


### Tabela: ITEM_CONSUMÍVEL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item consumível  | int | 1-5000 | pk | not null |
| nome | Nome de uma arma específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do item consumível  | vachar[30] | a-z, A-Z  | | |
| peso | Quantidade de massa corresponde ao item consumível  | int | 1-8 | | not null, default = 1 |
| preco | Custo total do item consumível  | int | 1-200 | | not null, default = 1 |
| durabilidadeMaxima | Tempo de durabilidade máxima do item consumível | int | 1-30 | | not null, default = 1 |
| qtdReparacaoStamina | Quantidade de stamina restaurada ao reparar o item consumível  | int | 1-100 |  | not null, default = 1 |
| qtdReparacaoVida | Quantidade de vida restaurada ao reparar o item consumível  | int | 1-100 | | not null, default = 1 |


### Tabela: ITEM_EQUIPÁVEL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idItem | Código identificador do item | int | 1-5000 | pk | not null |
| nome | Nome de um item específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do item | vachar[30] | a-z, A-Z | | |
| peso | Quantidade de massa corresponde ao item | int | 1-8 | | not null, default = 1 |
| preco | Custo total do item | int | 1-200 | | not null, default = 1 |
| durabilidadeMaxima | Tempo de durabilidade máxima do item | int | 1-30 | | not null, default = 1 |
| parteDoCorpo | Parte do corpo onde o item é equipado | vachar[30] | a-z, A-Z |  | not null, default = 'Desconhecido'|


### Tabela: INSTANCIA_ITEM

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaItem | Código identificador da instancia do item | int | 1-5000 | pk | not null |
| idItem | Código identificador do item | int | 1-5000 | pk, fk1 | not null |
| idInventario | Código identificador úncio de um inventário  | int | 1-5000 | pk, fk2 | not null |
| idPersonagem | Código identificador único de um personagem (Jogador) | int | 1-5000 | pk,fk3 | not null |


### Tabela: PROJETIL

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idProjetil | Código identificador de um projetil | int | 1-5000 | pk | not null |
| idInstanciaItem | Código identificador da instancia do item | int | 1-5000 | pk, fk1 | not null |
| posX | Coordenada X da posição do projetil no espaço | int | -10000 a 10000 | | |
| posY | Coordenada Y da posição do projetil no espaço  | int | -10000 a 10000 | | |
| posZ | Coordenada Z da posição do projetil no espaço  | int | -10000 a 10000 | | |
| colidiu | Indica se o projetil colidiu com um objeto ou não | boolean | true, false | | not null, default = false |
| velocidade | Velocidade do projetil em movimento | int | 1-1000 | | not null |


### Tabela: ID_SALA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idSala | Código identificador de uma sala | int | 1-5000 | pk | not null |
| idRegiao | Código identificador da região onde está a sala | int | 1-5000 | fk1 | not null |
| nome | Nome de uma sala específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da sala | vachar[60] | a-z, A-Z | | not null |


### Tabela: REGIAO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idRegiao | Código identificador de uma regiao | int | 1-5000 | pk | not null |
| idMapa | Código identificador do mapa onde está a região | int | 1-5000 | fk1 | not null |
| nome | Nome de uma região específica | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características da região | vachar[60] | a-z, A-Z | | not null |


### Tabela: REGIAO_FAZ_FRONTEIRA_COM_REGIAO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idRegiaoOrigem | Código identificador da região de origem | int | 1-5000 | pk, fk1 | not null |
| idRegiaoDestino | Código identificador da região de chegada | int | 1-5000 | pk, fk2 | not null |


### Tabela: MAPA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idMapa | Código identificador de um mapa | int | 1-5000 | pk | not null |
| nome | Nome de um mapa específico | vachar[30] | a-z, A-Z |  | not null |


### Tabela: ESTABELECIMENTO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idEstabelecimento | Código identificador de um mapa | int | 1-5000 | pk | not null |
| nome | Nome de um estabelecimento específico | vachar[30] | a-z, A-Z |  | not null |
| descricao | Apresenta as características do estabelecimento | vachar[60] | a-z, A-Z | | not null |


### Tabela: INSTANCIA_ESTABELECIMENTO

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idInstanciaEstabelecimento | Código identificador de uma instancia de um estabelecimento | int | 1-5000 | pk | not null |
| idEstabelecimento | Código identificador do estabelecimento | int | 1-5000 | pk, fk1 | not null |
| idInstanciaNPCDona | Código identificador do NPC dono do estabelecimento | int | 1-5000 | fk2 | not null |
| idSala | Código identificar da sala onde está presente o estabelecimento | int | 1-5000 | fk3 | not null |


### Tabela: SALA_CONECTA_COM_SALA

- Descrição: 

| Nome | Descrição | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio |
| --- | --- | --- | --- | --- | --- |
| idSalaOrigem | Código identificador da sala de origem | int | 1-5000 | pk, fk1 | not null |
| idSalaDestino | Código identificador da sala de chegada | int | 1-5000 | pk, fk2 | not null |