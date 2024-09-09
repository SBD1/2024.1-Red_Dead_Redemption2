# Dicionário de dados

### Tabela: MAPA

- Descrição da Tabela: Contém informações sobre os mapas disponíveis no sistema.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idMapa    | Código identificador único do mapa       | int          |                    | pk    | not null, default = nextval('mapa_id_seq')                 |
| descricao | Descrição do mapa                        | char(100)    |                    |       | not null                                                   |

### Tabela: REGIAO

- Descrição da Tabela: Contém informações sobre as regiões associadas aos mapas.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idRegiao  | Código identificador único da região     | int          |                    | pk    | not null, default = nextval('regiao_id_seq')               |
| idMapa    | Referência ao mapa associado             | int          |                    | fk    | not null, references MAPA(idMapa)                          |
| descricao | Descrição da região                      | varchar      |                    |       | not null                                                   |
| nome      | Nome da região                           | varchar(50)  |                    |       | not null                                                   |

### Tabela: AREA

- Descrição da Tabela: Contém informações sobre as áreas dentro das regiões.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idArea    | Código identificador único da área       | int          |                    | pk    | not null, default = nextval('area_id_seq')                 |
| idRegiao  | Referência à região associada            | int          |                    | fk    | not null, references REGIAO(idRegiao)                      |
| nome      | Nome da área                             | varchar(50)  |                    |       | not null                                                   |
| Leste     | Referência à área a leste                | int          |                    | fk    | references AREA(idArea)                                    |
| Oeste     | Referência à área a oeste                | int          |                    | fk    | references AREA(idArea)                                    |
| Sul       | Referência à área ao sul                 | int          |                    | fk    | references AREA(idArea)                                    |
| Norte     | Referência à área ao norte               | int          |                    | fk    | references AREA(idArea)                                    |

### Tabela: ARMA

- Descrição da Tabela: Contém informações sobre as armas disponíveis.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idArma    | Código identificador único da arma       | int          |                    | pk    | not null, default = nextval('arma_id_seq')                 |
| nome      | Nome da arma                             | varchar(50)  |                    |       | not null                                                   |
| efeito    | Efeito causado pela arma                 | varchar      |                    |       | not null                                                   |
| ponto     | Pontos de dano causados pela arma        | int          |                    |       | not null                                                   |

### Tabela: LOJA

- Descrição da Tabela: Contém informações sobre as lojas dentro das áreas.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idLoja    | Código identificador único da loja       | int          |                    | pk    | not null, default = nextval('loja_id_seq')                 |
| idArea    | Referência à área associada              | int          |                    | fk    | not null, references AREA(idArea)                          |
| descricao | Descrição da loja                        | varchar(100) |                    |       | not null                                                   |

### Tabela: ITEM

- Descrição da Tabela: Contém informações sobre os itens disponíveis nas lojas.

| Nome           | Descrição                                | Tipo de Dado   | Valores permitidos | Chave | Restrições de domínio                                      |
|----------------|------------------------------------------|----------------|--------------------|-------|------------------------------------------------------------|
| idItem         | Código identificador único do item       | int            |                    | pk    | not null, default = nextval('item_id_seq')                 |
| idLoja         | Referência à loja associada              | int            |                    | fk    | references LOJA(idLoja)                                    |
| nome           | Nome do item                             | varchar(50)    |                    |       | not null                                                   |
| acao           | Ação realizada pelo item                 | varchar(200)   |                    |       | not null                                                   |
| valor          | Valor monetário do item                  | numeric(10,2)  |                    |       | not null                                                   |
| tipo           | Tipo de item                             | char(50)       |                    |       | not null                                                   |
| descricaoItem  | Descrição do item                        | varchar(100)   |                    |       | not null                                                   |

### Tabela: NPC

- Descrição da Tabela: Contém informações sobre os NPCs (personagens não jogáveis).

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idNPC     | Código identificador único do NPC        | int          |                    | pk    | not null, default = nextval('npc_id_seq')                  |
| item      | Referência ao item associado             | int          |                    | fk    | not null, references ITEM(idItem)                          |
| nome      | Nome do NPC                              | varchar(50)  |                    |       | not null                                                   |

### Tabela: GANGUE

- Descrição da Tabela: Contém informações sobre as gangues.

| Nome           | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|----------------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idGangue       | Código identificador único da gangue     | int          |                    | pk    | not null, default = nextval('gangue_id_seq')               |
| nomeGangue     | Nome da gangue                           | varchar(50)  |                    |       | not null                                                   |
| simboloGangue  | Símbolo representativo da gangue         | char(50)     |                    |       | not null                                                   |

### Tabela: MISSAO

- Descrição da Tabela: Contém informações sobre as missões.

| Nome        | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-------------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idMissao    | Código identificador único da missão     | int          |                    | pk    | not null, default = nextval('missao_id_seq')               |
| NPC         | Referência ao NPC associado              | int          |                    | fk    | not null, references NPC(idNPC)                            |
| nomeMissao  | Nome da missão                           | varchar(50)  |                    |       | not null                                                   |
| arma        | Referência à arma associada              | int          |                    | fk    | not null, references ARMA(idArma)                          |

### Tabela: NPC_MISSAO

- Descrição da Tabela: Relaciona NPCs, gangues e missões.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idNPC     | Referência ao NPC associado              | int          |                    | fk    | not null, references NPC(idNPC)                            |
| gangue    | Referência à gangue associada            | int          |                    | fk    | not null, references GANGUE(idGangue)                      |
| missao    | Referência à missão associada            | int          |                    | fk    | not null, references MISSAO(idMissao)                      |

### Tabela: JOGADOR

- Descrição da Tabela: Contém informações sobre os jogadores.

| Nome       | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|------------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idJogador  | Código identificador único do jogador    | int          |                    | pk    | not null, default = nextval('jogador_id_seq')              |
| nome       | Nome do jogador                          | varchar(50)  |                    |       | not null, unique                                           |
| idArea     | Referência à área associada              | int          |                    | fk    | not null, references AREA(idArea)                          |
| pontosVida | Pontos de vida do jogador                | int          |                    |       | not null                                                   |
| idGangue   | Referência à gangue

 associada            | int          |                    | fk    | not null, references GANGUE(idGangue)                      |


## Tabela: ARSENAL
| Campo     | Tipo  | Descrição                                       |
|-----------|-------|-------------------------------------------------|
| idArsenal | INT   | Identificador do arsenal, chave primária.       |
| arma      | INT   | Identificador da arma, chave estrangeira para a tabela ARMA. |

**Chaves Estrangeiras:**
- `idArsenal` referencia `JOGADOR(idJogador)`
- `arma` referencia `ARMA(idArma)`

## Tabela: INSTANCIA_ITEM
| Campo           | Tipo  | Descrição                                                       |
|-----------------|-------|-----------------------------------------------------------------|
| idInstanciaItem | INT   | Identificador único da instância do item, chave primária.       |
| idItem          | INT   | Identificador do item, chave estrangeira para a tabela ITEM.    |
| idJogador       | INT   | Identificador do jogador, chave estrangeira para a tabela JOGADOR. |

**Chaves Estrangeiras:**
- `idItem` referencia `ITEM(idItem)`
- `idJogador` referencia `JOGADOR(idJogador)`

## Tabela: INVENTARIO
| Campo       | Tipo  | Descrição                                         |
|-------------|-------|---------------------------------------------------|
| idJogador   | INT   | Identificador do jogador, chave primária.         |
| dinheiro    | INT   | Quantidade de dinheiro que o jogador possui.      |

**Chaves Estrangeiras:**
- `idJogador` referencia `JOGADOR(idJogador)`

## Tabela: INSTANCIA_JOGADOR_MISSAO
| Campo       | Tipo  | Descrição                                         |
|-------------|-------|---------------------------------------------------|
| idJogador   | INT   | Identificador do jogador, chave estrangeira para a tabela JOGADOR. |
| idMissao    | INT   | Identificador da missão, chave estrangeira para a tabela MISSAO.  |

**Chaves Estrangeiras:**
- `idJogador` referencia `JOGADOR(idJogador)`
- `idMissao` referencia `MISSAO(idMissao)`

## Tabela: HABILIDADE
| Campo           | Tipo       | Descrição                             |
|-----------------|------------|---------------------------------------|
| idHabilidade    | INT        | Identificador único da habilidade, chave primária. |
| nomeHabilidade  | VARCHAR(50)| Nome da habilidade.                   |
| dano            | INT        | Dano causado pela habilidade.         |
| descricao       | VARCHAR(100)| Descrição da habilidade.             |

## Tabela: INIMIGO
| Campo         | Tipo  | Descrição                                         |
|---------------|-------|---------------------------------------------------|
| idNPC         | INT   | Identificador do NPC, chave primária.             |
| idHabilidade  | INT   | Identificador da habilidade, chave estrangeira para a tabela HABILIDADE. |
| moedas        | INT   | Quantidade de moedas que o inimigo possui.        |

**Chaves Estrangeiras:**
- `idNPC` referencia `NPC(idNPC)`
- `idHabilidade` referencia `HABILIDADE(idHabilidade)`

## Tabela: AMIGO
| Campo     | Tipo  | Descrição                           |
|-----------|-------|-------------------------------------|
| idNPC     | INT   | Identificador do NPC, chave primária.|
| humor     | INT   | Nível de humor do NPC amigo.        |

**Chaves Estrangeiras:**
- `idNPC` referencia `NPC(idNPC)`

## Tabela: INSTANCIA_INIMIGO
| Campo                | Tipo  | Descrição                                         |
|----------------------|-------|---------------------------------------------------|
| idInstancia_Inimigo  | INT   | Identificador único da instância do inimigo, chave primária. |
| idNPC                | INT   | Identificador do NPC, chave estrangeira para a tabela NPC. |
| idArea               | INT   | Identificador da área, chave estrangeira para a tabela AREA. |
| idItem               | INT   | Identificador do item, chave estrangeira para a tabela ITEM. |
| pontosVidaMax        | INT   | Pontos de vida máximos do inimigo.                |
| pontosVida           | INT   | Pontos de vida atuais do inimigo.                 |
| multiplicador        | INT   | Multiplicador de força do inimigo.                |

**Chaves Estrangeiras:**
- `idNPC` referencia `NPC(idNPC)`
- `idArea` referencia `AREA(idArea)`
- `idItem` referencia `ITEM(idItem)`

Aqui está o dicionário de dados em markdown para as tabelas que você mencionou:

### Tabela: COLDRE

- Descrição da Tabela: Contém informações sobre o coldre que armazena armas.

| Nome    | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio         |
|---------|------------------------------------------|--------------|--------------------|-------|-------------------------------|
| idItem  | Código identificador do item             | int          |                    | fk    | not null, referencia ITEM(idItem) |
| arma    | Código identificador da arma no coldre   | int          |                    | fk    | not null, referencia ARMA(idArma)  |

### Tabela: FALAS

- Descrição da Tabela: Contém informações sobre as falas dos NPCs em determinadas áreas do jogo.

| Nome    | Descrição                                  | Tipo de Dado  | Valores permitidos | Chave | Restrições de domínio             |
|---------|--------------------------------------------|---------------|--------------------|-------|-----------------------------------|
| idNPC   | Código identificador do NPC                | int           |                    | fk    | not null, referencia NPC(idNPC)   |
| idArea  | Código identificador da área               | int           |                    | fk    | not null, referencia AREA(idArea) |
| texto   | Texto da fala                              | varchar(400)  |                    |       |                                   |
| momento | Momento em que a fala ocorre               | int           |                    |       | not null                          |

