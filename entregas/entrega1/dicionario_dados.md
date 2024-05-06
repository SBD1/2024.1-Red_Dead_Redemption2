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


### Tabela: Animal

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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


### Tabela: Diálogo

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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


### Tabela: Instância de Animal

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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


### Tabela: Linha de Fala

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


### Tabela: Mapa

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


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


### Tabela: Região

- Descrição: 
- Observações: 

| Nome | Descrição | Tipo de Dado | Tamanho | Restrições de domínio |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |