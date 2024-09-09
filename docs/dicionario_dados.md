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

### Tabela: ARSENAL

- Descrição da Tabela: Contém informações sobre o arsenal do jogador, que relaciona o jogador às armas que possui.

| Nome      | Descrição                                     | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|-----------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idArsenal | Identificador do arsenal, referência ao jogador | int          |                    | pk, fk| not null, references JOGADOR(idJogador)                    |
| arma      | Identificador da arma                         | int          |                    | pk, fk| not null, references ARMA(idArma)                          |

### Tabela: INSTANCIA_ITEM

- Descrição da Tabela: Contém instâncias específicas dos itens que os jogadores possuem.

| Nome            | Descrição                                  | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------------|--------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idInstanciaItem | Identificador único da instância do item   | int          |                    | pk    | not null, default = nextval('instancia_item_id_seq')       |
| idItem          | Identificador do item                      | int          |                    | fk    | not null, references ITEM(idItem)                          |
| idJogador       | Identificador do jogador                   | int          |                    | fk    | references JOGADOR(idJogador)                              |

### Tabela: INVENTARIO

- Descrição da Tabela: Contém informações sobre o inventário do jogador.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idJogador | Identificador do jogador                 | int          |                    | pk, fk| not null, references JOGADOR(idJogador)                    |
| dinheiro  | Quantidade de dinheiro que o jogador possui | int          |                    |       |                                                            |

### Tabela: INSTANCIA_JOGADOR_MISSAO

- Descrição da Tabela: Relaciona os jogadores às missões que estão participando.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idJogador | Identificador do jogador                 | int          |                    | fk    | not null, references JOGADOR(idJogador)                    |
| idMissao  | Identificador da missão                  | int          |                    | fk    | references MISSAO(idMissao)                                |

### Tabela: HABILIDADE

- Descrição da Tabela: Contém as habilidades que podem ser usadas pelos personagens do jogo.

| Nome            | Descrição                                  | Tipo de Dado  | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------------|--------------------------------------------|---------------|--------------------|-------|------------------------------------------------------------|
| idHabilidade    | Identificador único da habilidade          | int           |                    | pk    | not null, default = nextval('habilidade_id_seq')           |
| nomeHabilidade  | Nome da habilidade                         | varchar(50)   |                    |       | not null                                                   |
| dano            | Dano causado pela habilidade               | int           |                    |       |                                                            |
| descricao       | Descrição da habilidade                    | varchar(100)  |                    |       | not null                                                   |

### Tabela: INIMIGO

- Descrição da Tabela: Contém informações sobre os inimigos do jogo.

| Nome         | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|--------------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idNPC        | Identificador do NPC inimigo             | int          |                    | pk, fk| not null, references NPC(idNPC)                            |
| idHabilidade | Identificador da habilidade do inimigo   | int          |                    | fk    | references HABILIDADE(idHabilidade)                        |
| moedas       | Quantidade de moedas que o inimigo possui | int          |                    |       | not null                                                   |

### Tabela: AMIGO

- Descrição da Tabela: Contém informações sobre os NPCs amigos do jogador.

| Nome      | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|-----------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idNPC     | Identificador do NPC amigo               | int          |                    | pk, fk| not null, references NPC(idNPC)                            |
| humor     | Nível de humor do NPC amigo              | int          |                    |       | not null                                                   |

### Tabela: INSTANCIA_INIMIGO

- Descrição da Tabela: Contém informações sobre instâncias específicas dos inimigos em áreas do jogo.

| Nome                | Descrição                                | Tipo de Dado | Valores permitidos | Chave | Restrições de domínio                                      |
|---------------------|------------------------------------------|--------------|--------------------|-------|------------------------------------------------------------|
| idInstancia_Inimigo | Identificador único da instância do inimigo | int          |                    | pk    | not null, default = nextval('instancia_inimigo_id_seq')    |
| idNPC               | Identificador do NPC inimigo             | int          |                    | fk    | not null, references NPC(idNPC)                            |
| idArea              | Identificador da área                    | int          |                    | fk    | not null, references AREA(idArea)                          |
| idItem              | Identificador do item                    | int          |                    | fk    | references ITEM(idItem)                                    |
| pontosVidaMax       | Pontos de vida máximos do inimigo        | int          |                    |       | not null                                                   |
| pontosVida          | Pontos de vida atuais do inimigo         | int          |                    |       | not null                                                   |
| multiplicador       | Multiplicador de força do inimigo        | int          |                    |       | not null                                                   |


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

