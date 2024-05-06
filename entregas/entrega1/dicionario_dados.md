# Dicionário de dados

<!-- Copiar o modelo abaixo -->

<!-- ### Tabela: NOME

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  | -->

### Tabela: Amigável

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: ANIMAL

- Descrição: Armazenará as informações das espécies de animais.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_animal | Código identificador único do animal | int |  | pk, identity |
| espécie | Nome da espécie do animal | char | 30 | sk |
| habitat | Habitat onde vive uma espécie de animal | char | 20 |  |
| velocidade | Velocidade de deslocamento de um animal | int |  | not null, default = 1 |
| vida_máx | Vida máxima de uma espécie de animal | int |  | not null, default = 30 (máx = 100) |
| stamina_máx | Energia máxima que uma espécie possui para se movimentar  | int |  | not null, default = 100 |
| textura | Textura da pele/escama da espécie | char | 10 |  |


### Tabela: Arma

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: ARMA_FOGO

- Descrição: Armazena os tipos de armas de fogo disponíveis no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_arma | Chave de identificação das armas | int |  |  |
| nome | Nome da arma | char | 15 |  |
| descricao | Descrição da arma (e.g história de fabricação, material de fabricação) | char | 100 |  |
| categoria | Tipo de arma (e.g.) |  |  |  |
| preco | Preço necessário para comprar a arma de um NPC | int |  |  |
| peso | Peso da arma (em kg). Diminui a stamina | int |  |  |
| durabilidade | Quantidade de tiros (em centenas) que uma arma pode atirar até exigir reparo | int |  |  |
| dano | Dano causado por um único projétil disparado pela arma  | int |  |  |
| vel_reload | Tempo necessário para recarregar a arma (em ms) | int |  |  |
| vel_disparo | Intervalo de tempo mínimo entre dois disparos (em ms) | int |  |  |


### Tabela: Arma Melee

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Classe

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Consumível

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: DIÁLOGO

- Descrição: Armazenará as informações sobre os diálogos falados pelos NPCs.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_diálogo | Código identificador do diálogo | int |  | pk |
| id_instância_npc | Código identificador da instância de NPC que fala um determinado diálogo | int |  | fk |
| descrição | Contextualização do diálogo | char | 100 | not null |


### Tabela: Equipável

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Estabelecimento

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Gangue

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Habilidade

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: HISTÓRIA

- Descrição: Armazenará as informações das histórias.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_história | Código de identificação único da história. | int |  | pk, identity |
| título | Nome da história | char | 500 | sk |
| enredo | Texto do enredo da história | char | 1000 | not null |


### Tabela: Hostil

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: INSTÂNCIA_ANIMAL

- Descrição: Armazenará as informações das instâncias de animais vivas no jogo.
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
| id_instância_animal | Código identificador da instância do animal | int |  | pk, identity |
| id_animal | Código identificador da espécie de animal | int |  | fk |
| vida_atual | Vida atual de uma instância de animal | int |  | not null |
| stamina_atual | Energia atual que a instância tem para se movimentar | int |  | not null |


### Tabela: Instância de Arma

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Instância de Arma de Fogo

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Instância de Arma Melee

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Instância de Estabelecimento

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Instância de Item

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Instância de NPC

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Inventário

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Item

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Jogador

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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


### Tabela: Personagem

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Projétil

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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