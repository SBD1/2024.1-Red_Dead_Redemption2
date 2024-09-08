-- Tabela MAPA
begin;
   CREATE SEQUENCE mapa_id_seq START 1;
   CREATE TABLE IF NOT EXISTS MAPA(
      idMapa            int NOT NULL DEFAULT nextval('mapa_id_seq') PRIMARY KEY,
      descricao         CHAR(100) NOT NULL
   );
   ALTER SEQUENCE mapa_id_seq OWNED BY MAPA.idMapa;
   savepoint create_tb_MAPA;
commit;


-- Tabela REGIAO
begin;
   CREATE SEQUENCE regiao_id_seq START 1;
   CREATE TABLE IF NOT EXISTS REGIAO(
      idRegiao          int NOT NULL DEFAULT nextval('regiao_id_seq') PRIMARY KEY,
      idMapa            INT NOT NULL,
      descricao         VARCHAR NOT NULL,
      nome              VARCHAR(50) NOT NULL,
      FOREIGN KEY (idMapa) REFERENCES MAPA (idMapa)
   );
   ALTER SEQUENCE regiao_id_seq OWNED BY REGIAO.idRegiao;
   savepoint create_tb_REGIAO;
commit;


-- Tabela AREA
begin;
   CREATE SEQUENCE area_id_seq START 1;
   CREATE TABLE IF NOT EXISTS AREA(
      idArea        int NOT NULL DEFAULT nextval('area_id_seq') PRIMARY KEY,
      idRegiao      INT NOT NULL,
      nome          VARCHAR(50) NOT NULL,
      areaLeste     INT  REFERENCES AREA(idArea),
      areaOeste     INT  REFERENCES AREA(idArea),
      areaSul       INT  REFERENCES AREA(idArea),
      areaNorte     INT  REFERENCES AREA(idArea),
      FOREIGN KEY (idRegiao) REFERENCES REGIAO (idRegiao)
   );
   ALTER SEQUENCE area_id_seq OWNED BY AREA.idArea;
   savepoint create_tb_AREA;
commit;


-- Tabela ARMA
begin;
   CREATE SEQUENCE arma_id_seq START 1;
   CREATE TABLE IF NOT EXISTS ARMA(
      idArma       int NOT NULL DEFAULT nextval('arma_id_seq') PRIMARY KEY,
      nome            VARCHAR(50) NOT NULL,
      efeito          VARCHAR NOT NULL,
      ponto           INT NOT NULL
   );
   ALTER SEQUENCE arma_id_seq OWNED BY ARMA.idArma;
   savepoint create_tb_ARMA;
commit;


-- Tabela LOJA
begin;
   CREATE SEQUENCE loja_id_seq START 1;
   CREATE TABLE IF NOT EXISTS LOJA(
      idLoja              INT NOT NULL DEFAULT nextval('loja_id_seq') PRIMARY KEY,
      idArea              INT NOT NULL,
      descricao           VARCHAR(100) NOT NULL,
      FOREIGN KEY (idArea) REFERENCES AREA (idArea)
   );
   ALTER SEQUENCE loja_id_seq OWNED BY LOJA.idLoja;
   savepoint create_tb_LOJA;
commit;

-- Tabela ITEM
begin;
   CREATE SEQUENCE item_id_seq START 1;
   CREATE TABLE IF NOT EXISTS ITEM(
      idItem           int NOT NULL DEFAULT nextval('item_id_seq') PRIMARY KEY,
      idLoja           INT NULL, 
      nome             VARCHAR(50) NOT NULL,
      acao             VARCHAR(200) NOT NULL,
      valor            NUMERIC(10,2) NOT NULL,
      tipo             CHAR(50) NOT NULL,
      descricaoItem    VARCHAR(100) NOT NULL, 
      FOREIGN KEY (idLoja) REFERENCES LOJA (idLoja)
   );
   ALTER SEQUENCE item_id_seq OWNED BY ITEM.idItem;
   savepoint create_tb_ITEM;
commit;


-- Tabela NPC
begin;
   CREATE SEQUENCE npc_id_seq START 1;
   CREATE TABLE IF NOT EXISTS NPC(
      idNPC      INT NOT NULL DEFAULT nextval('npc_id_seq') PRIMARY KEY,
      item       INT NOT NULL,
      nome       VARCHAR(50) NOT NULL,
      FOREIGN KEY (item) REFERENCES ITEM (idItem)
   );
   ALTER SEQUENCE npc_id_seq OWNED BY NPC.idNPC;
   savepoint create_tb_NPC;
commit;


-- Tabela GANGUE
begin;
   CREATE SEQUENCE gangue_id_seq START 1;
   CREATE TABLE IF NOT EXISTS GANGUE(
      idGangue         int NOT NULL DEFAULT nextval('gangue_id_seq') PRIMARY KEY,
      nomeGangue       VARCHAR(50) NOT NULL,
      simboloGangue        CHAR(50) NOT NULL
   );
   ALTER SEQUENCE gangue_id_seq OWNED BY GANGUE.idGangue;
   savepoint create_tb_GANGUE;
commit;


-- Tabela MISSAO
begin;
   CREATE SEQUENCE missao_id_seq START 1;
   CREATE TABLE IF NOT EXISTS MISSAO(
      idMissao         int NOT NULL DEFAULT nextval('missao_id_seq') PRIMARY KEY,
      NPC                  INT  NOT NULL,
      nomeMissao       VARCHAR(50) NOT NULL,
      arma              INT  NOT NULL,
      FOREIGN KEY (NPC) REFERENCES NPC (idNPC),
      FOREIGN KEY (arma) REFERENCES ARMA (idArma)
   );
   ALTER SEQUENCE missao_id_seq OWNED BY MISSAO.idMissao;
   savepoint create_tb_MISSAO;
commit;


-- Tabela NPC_MISSAO
begin;
   CREATE TABLE IF NOT EXISTS NPC_MISSAO(
      idNPC            INT  NOT NULL,
      gangue             INT  NOT NULL,
      missao       INT  NOT NULL,
      FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
      FOREIGN KEY (gangue) REFERENCES GANGUE (idGangue),
      FOREIGN KEY (missao) REFERENCES MISSAO (idMissao)
   );
   savepoint create_tb_NPC_MISSAO;
commit;


-- Tabela JOGADOR
begin;
   CREATE SEQUENCE jogador_id_seq START 1;
   CREATE TABLE IF NOT EXISTS JOGADOR(
      idJogador    INT NOT NULL DEFAULT nextval('jogador_id_seq') PRIMARY KEY,
      nome         VARCHAR(50) NOT NULL,
      idArea       INT  NOT NULL,
      pontosVida   INT  NOT NULL,
      idGangue       INT  NOT NULL,
      estado       INT  NOT NULL DEFAULT 1,
      FOREIGN KEY (idArea) REFERENCES AREA (idArea),
      FOREIGN KEY (idGangue) REFERENCES GANGUE (idGangue),
      UNIQUE (nome)
   );
   ALTER SEQUENCE jogador_id_seq OWNED BY JOGADOR.idJogador;
   savepoint create_tb_JOGADOR;
commit;

-- Tabela ARSENAL
begin;
   CREATE SEQUENCE arsenal_id_seq START 1;
   CREATE TABLE IF NOT EXISTS ARSENAL(
      idArsenal  INT NOT NULL,
      arma     INT NOT NULL,
      FOREIGN KEY (idArsenal) REFERENCES JOGADOR (idJogador),
      FOREIGN KEY (arma) REFERENCES ARMA (idArma),
      PRIMARY KEY (idArsenal,arma)
   );
   ALTER SEQUENCE arsenal_id_seq OWNED BY ARSENAL.idArsenal;
   savepoint create_tb_ARSENAL;
commit;

-- Tabela INSTANCIA_ITEM
begin;
   CREATE SEQUENCE instancia_item_id_seq START 1;
   CREATE TABLE IF NOT EXISTS INSTANCIA_ITEM(
      idInstanciaItem      INT NOT NULL DEFAULT nextval('instancia_item_id_seq') PRIMARY KEY,
      idItem               INT  NOT NULL,
      idJogador            INT NULL DEFAULT NULL,
      FOREIGN KEY (idItem) REFERENCES ITEM (idItem),
      FOREIGN KEY (idJogador) REFERENCES JOGADOR (idJogador)
   );
   ALTER SEQUENCE instancia_item_id_seq OWNED BY INSTANCIA_ITEM.idInstanciaItem;
   savepoint create_tb_INSTANCIA_ITEM;
commit;


-- Tabela INVENTARIO
begin;
   CREATE TABLE IF NOT EXISTS INVENTARIO(
      idJogador               INT NOT NULL,
      dinheiro                INT NULL,
      FOREIGN KEY (idJogador) REFERENCES JOGADOR (idJogador)
   );
   savepoint create_tb_INVENTARIO;
commit;  


-- Tabela INSTANCIA_JOGADOR_MISSAO
begin;
   CREATE TABLE IF NOT EXISTS INSTANCIA_JOGADOR_MISSAO(
      idJogador            INT NOT NULL,
      idMissao         INT NULL,
      FOREIGN KEY (idJogador) REFERENCES JOGADOR (idJogador),
      FOREIGN KEY (idMissao) REFERENCES MISSAO (idMissao)
   );
   savepoint create_tb_INSTANCIA_JOGADOR_MISSAO;
commit;


-- Tabela HABILIDADE
begin;
   CREATE SEQUENCE habilidade_id_seq START 1;
   CREATE TABLE IF NOT EXISTS HABILIDADE(
      idHabilidade     INT NOT NULL DEFAULT nextval('habilidade_id_seq') PRIMARY KEY,
      nomeHabilidade   VARCHAR(50) NOT NULL,
      dano             INT NULL,
      descricao        VARCHAR(100) NOT NULL
   );
   ALTER SEQUENCE habilidade_id_seq OWNED BY HABILIDADE.idHabilidade;
   savepoint create_tb_HABILIDADE;
commit;


-- Tabela INIMIGO
begin;
   CREATE TABLE IF NOT EXISTS INIMIGO(
      idNPC            INT NOT NULL,
      idHabilidade     INT NULL,
      moedas           INT NOT NULL,
      FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
      FOREIGN KEY (idHabilidade) REFERENCES HABILIDADE (idHabilidade)
   );
      savepoint create_tb_INIMIGO;
commit;


-- Tabela INSTANCIA_INIMIGO
begin;
   CREATE SEQUENCE instancia_inimigo_id_seq START 1;
   CREATE TABLE IF NOT EXISTS INSTANCIA_INIMIGO(
      idInstancia_Inimigo INT NOT NULL DEFAULT nextval('instancia_inimigo_id_seq') PRIMARY KEY,
      idNPC             INT NOT NULL,
      idArea            INT NOT NULL,
      idItem            INT NULL,
      pontosVidaMax     INT NOT NULL,
      pontosVida        INT NOT NULL,
      multiplicador     INT NOT NULL,
      FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
      FOREIGN KEY (idArea) REFERENCES AREA (idArea),
      FOREIGN KEY (idItem) REFERENCES ITEM (idItem)
   );
   ALTER SEQUENCE instancia_inimigo_id_seq OWNED BY INSTANCIA_INIMIGO.idInstancia_Inimigo;
   savepoint create_tb_INSTANCIA_INIMIGO;
commit;


-- Tabela Coldre
begin;
   CREATE TABLE IF NOT EXISTS COLDRE(
      idItem           INT NOT NULL,
      arma          INT NOT NULL,
      FOREIGN KEY (idItem) REFERENCES ITEM (idItem),
      FOREIGN KEY (arma) REFERENCES ARMA (idArma)
   );
   savepoint create_tb_COLDRE;
commit;

-- Tabela Falas
begin;
   CREATE TABLE IF NOT EXISTS FALAS(
      idNPC           INT NOT NULL,
      idArea          INT NOT NULL,
      texto           VARCHAR(400),
      momento         INT NOT NULL,
      FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
      FOREIGN KEY (idArea) REFERENCES AREA (idArea)
   );
commit;

-- Tabela Instancia_NPC_Tipo
begin;
   CREATE TABLE IF NOT EXISTS INSTANCIA_NPC_TIPO(
      idNPC           INT NOT NULL,
      tipo            CHAR(50) NOT NULL,
      FOREIGN KEY (idNPC) REFERENCES NPC (idNPC)
   );
   savepoint create_tb_INSTANCIA_NPC_TIPO;
commit;
