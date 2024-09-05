import psycopg2
from database import create_connection

connection = create_connection()
cur = connection.cursor()

def create_tables():
    """ create tables in the PostgreSQL database """
    comandos = (
        """

        CREATE TABLE IF NOT EXISTS MAPA(
        idMapa            SERIAL PRIMARY KEY,
        descricao         CHAR(100) NOT NULL
        );

        """,

        """
        CREATE TABLE IF NOT EXISTS REGIAO(
        idRegiao          SERIAL PRIMARY KEY,
        idMapa            INT NOT NULL,
        descricao         INT NOT NULL,
        nome              CHAR(50) NOT NULL,
        FOREIGN KEY (idMapa) REFERENCES MAPA (idMapa)
        );

        """,
        """
        CREATE TABLE IF NOT EXISTS AREA(
        idArea        SERIAL PRIMARY KEY,
        idRegiao      INT NOT NULL,
        areaLeste     INT  REFERENCES AREA(idArea),
        areaOeste     INT  REFERENCES AREA(idArea),
        areaSul       INT  REFERENCES AREA(idArea),
        areaNorte     INT  REFERENCES AREA(idArea),
        FOREIGN KEY (idRegiao) REFERENCES REGIAO (idRegiao)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS ARMA(
        idArma       SERIAL PRIMARY KEY,
        nome            CHAR(50) NOT NULL,
        efeito          CHAR(50) NOT NULL,
        ponto           NUMERIC(4,2) NOT NULL,
        quantidadeUso   NUMERIC(4,2) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ARSENAL(
        idArsenal  SERIAL PRIMARY KEY,
        numSlots    INT  NOT NULL,
        arma     INT  NOT NULL,
        FOREIGN KEY (arma) REFERENCES ARMA (idArma)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ITEM(
        idItem           SERIAL PRIMARY KEY,
        nome             VARCHAR(50) NOT NULL,
        acao             VARCHAR(200) NOT NULL,
        valor            NUMERIC(4,2) NOT NULL,
        tipo             CHAR(20) NOT NULL,
        descricaoItem    VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS NPC(
        idNPC      SERIAL PRIMARY KEY,
        item       INT  NOT NULL,
        nome       CHAR(50) NOT NULL,
        FOREIGN KEY (item) REFERENCES ITEM (idItem)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS GANGUE(
        idGangue                       SERIAL PRIMARY KEY,
        nomeGangue                     CHAR(50) NOT NULL,
        simboloGangue                      CHAR(20) NOT NULL,
        treinadorResponsavel         INT  NOT NULL,
        FOREIGN KEY (treinadorResponsavel) REFERENCES NPC (idNPC)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS TREINAMENTO(
        idTreinamento         SERIAL PRIMARY KEY,
        NPC                  INT  NOT NULL,
        nomeTreinamento       CHAR(50) NOT NULL,
        arma              INT  NOT NULL,
        FOREIGN KEY (NPC) REFERENCES NPC (idNPC),
        FOREIGN KEY (arma) REFERENCES ARMA (idArma)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS TREINADOR(
        idNPC            INT  NOT NULL,
        gangue             INT  NOT NULL,
        treinamento       INT  NOT NULL,
        FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
        FOREIGN KEY (gangue) REFERENCES GANGUE (idGangue),
        FOREIGN KEY (treinamento) REFERENCES TREINAMENTO (idTreinamento)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS JOGADOR(
        idJogador  SERIAL PRIMARY KEY,
        idArsenal INT  NOT NULL,
        nome       CHAR(50) NOT NULL,
        idArea     INT  NOT NULL,
        pontosVida INT  NOT NULL,
        idGangue     INT  NOT NULL,
        FOREIGN KEY (idArsenal) REFERENCES ARSENAL (idArsenal),
        FOREIGN KEY (idArea) REFERENCES AREA (idArea),
        FOREIGN KEY (idGangue) REFERENCES GANGUE (idGangue)
        );
        """ ,
        """
        CREATE TABLE IF NOT EXISTS INSTANCIA_ITEM(
        idInstanciaItem      SERIAL PRIMARY KEY,
        idItem               INT  NOT NULL,
        FOREIGN KEY (idItem) REFERENCES ITEM (idItem)
        );
        """,
        """

        CREATE TABLE IF NOT EXISTS INVENTARIO(
        idJogador               INT NOT NULL,
        instanciaItem	         INT NULL,
        dinheiro                INT NULL,
        FOREIGN KEY (idJogador) REFERENCES JOGADOR (idJogador),
        FOREIGN KEY (instanciaItem) REFERENCES INSTANCIA_ITEM (idInstanciaItem)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS INSTANCIA_JOGADOR_TREINAMENTO(
        idJogador            INT NOT NULL,
        idTreinamento         INT NULL,
        FOREIGN KEY (idJogador) REFERENCES JOGADOR (idJogador),
        FOREIGN KEY (idTreinamento) REFERENCES TREINAMENTO (idTreinamento)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS HABILIDADE(
        idHabilidade     SERIAL PRIMARY KEY,
        nomeHabilidade   CHAR(50) NOT NULL,
        dano             INT NULL,
        descricao        CHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS INIMIGO(
        idNPC            INT NOT NULL,
        idHabilidade     INT NULL,
        moedas           INT NOT NULL,
        FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
        FOREIGN KEY (idHabilidade) REFERENCES HABILIDADE (idHabilidade)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS INSTANCIA_INIMIGO(
        idNPC             INT NOT NULL,
        idArea            INT NOT NULL,
        idInstanciaItem   INT NULL,
        pontosVida        INT NOT NULL,
        multiplicador     INT NOT NULL,
        FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
        FOREIGN KEY (idArea) REFERENCES AREA (idArea),
        FOREIGN KEY (idInstanciaItem) REFERENCES INSTANCIA_ITEM (idInstanciaItem)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS FERRAMENTA(
        idItem          INT NOT NULL,
        forca           INT NULL,
        FOREIGN KEY (idItem) REFERENCES ITEM (idItem)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS TONICO(
        idItem            INT NOT NULL,
        ingrediente       CHAR(50) NOT NULL,
        FOREIGN KEY (idItem) REFERENCES ITEM (idItem)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS LOJA(
        idLoja            SERIAL PRIMARY KEY,
        idNPC             INT NOT NULL,
        idArea              INT NOT NULL,
        idInstanciaItem   INT NOT NULL,
        descricao         CHAR(100) NOT NULL,
        FOREIGN KEY (idNPC) REFERENCES NPC (idNPC),
        FOREIGN KEY (idArea) REFERENCES AREA (idArea),
        FOREIGN KEY (idInstanciaItem) REFERENCES INSTANCIA_ITEM (idInstanciaItem)
        );

        """)
    try:
        for comando in comandos:
            cur.execute(comando)

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("Tabelas geradas com êxito!")

if __name__ == '__main__':
    create_tables()
