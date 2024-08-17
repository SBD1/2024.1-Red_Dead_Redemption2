import psycopg2
from database import create_connection

connection = create_connection()
cur = connection.cursor()

def create_tables():
    """Create tables in the PostgreSQL database."""
    comandos = [
        """
        CREATE TABLE IF NOT EXISTS mapa (
            idMapa SERIAL PRIMARY KEY,
            nome VARCHAR(30) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS regiao (
            idRegiao SERIAL PRIMARY KEY,
            idMapa INT NOT NULL,
            nome VARCHAR(30) NOT NULL,
            descricao VARCHAR(60) NOT NULL,
            CONSTRAINT fk_mapa FOREIGN KEY(idMapa) REFERENCES mapa(idMapa) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS regiao_faz_fronteira_com_regiao (
            idRegiaoOrigem INT,
            idRegiaoDestino INT,
            PRIMARY KEY(idRegiaoOrigem, idRegiaoDestino),
            CONSTRAINT fk_origem FOREIGN KEY (idRegiaoOrigem) REFERENCES regiao(idRegiao) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_destino FOREIGN KEY (idRegiaoDestino) REFERENCES regiao(idRegiao) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS sala (
            idSala SERIAL PRIMARY KEY,
            idRegiao INT NOT NULL,
            nome VARCHAR(30) NOT NULL,
            descricao VARCHAR(60) NOT NULL,
            CONSTRAINT fk_regiao FOREIGN KEY(idRegiao) REFERENCES regiao(idRegiao) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS sala_conecta_com_sala (
            idSalaOrigem INT,
            idSalaDestino INT,
            PRIMARY KEY(idSalaOrigem, idSalaDestino),
            CONSTRAINT fk_origem FOREIGN KEY(idSalaOrigem) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_destino FOREIGN KEY(idSalaDestino) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS estabelecimento (
            idEstab SERIAL PRIMARY KEY,
            nome VARCHAR(30) NOT NULL,
            descricao VARCHAR(60) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS personagem_tipo (
            idPersonagem SERIAL PRIMARY KEY,
            tipo INT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS inventario (
            idInventario SERIAL PRIMARY KEY,
            totalItens INT NOT NULL DEFAULT 0,
            capacidade INT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS classe (
            idClasse SERIAL PRIMARY KEY,
            nome VARCHAR(20) NOT NULL    
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS historia (
            idHistoria SERIAL PRIMARY KEY,
            titulo VARCHAR(60) NOT NULL,
            enredo VARCHAR(1000) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS missao (
            idMissao SERIAL PRIMARY KEY,
            titulo VARCHAR(60) NOT NULL,
            nivelDificuldade INT NOT NULL CHECK(nivelDificuldade BETWEEN 1 AND 10),
            idHistoria INT NOT NULL,
            idRegiao INT NOT NULL,
            status DECIMAL(3,2) NOT NULL DEFAULT 0.00,
            CONSTRAINT fk_historia FOREIGN KEY(idHistoria) REFERENCES historia(idHistoria) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_regiao FOREIGN KEY(idRegiao) REFERENCES regiao(idRegiao) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS missao_depende_de_missao (
            idMissaoAtual INT,
            idMissaoAnterior INT,
            PRIMARY KEY(idMissaoAtual, idMissaoAnterior),
            CONSTRAINT fk_atual FOREIGN KEY(idMissaoAtual) REFERENCES missao(idMissao) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_anterior FOREIGN KEY(idMissaoAnterior) REFERENCES missao(idMissao) 
            ON DELETE RESTRICT ON UPDATE CASCADE   
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS jogador (
            idPersonagem INT PRIMARY KEY,
            idInventario INT NOT NULL,
            idSala INT NOT NULL,
            idClasse INT NOT NULL,
            idGangue INT NOT NULL,
            nome VARCHAR(30) NOT NULL,
            xp INT NOT NULL DEFAULT 0,
            dinheiro INT NOT NULL DEFAULT 0,
            velocidade INT NOT NULL DEFAULT 7 CHECK(velocidade BETWEEN 1 AND 10),
            vidaMax INT NOT NULL DEFAULT 100 CHECK(vidaMax BETWEEN 1 AND 100),
            vidaAtual INT NOT NULL DEFAULT 100 CHECK(vidaAtual BETWEEN 1 AND 100),
            staminaMax INT NOT NULL DEFAULT 1000 CHECK(staminaMax BETWEEN 1 AND 1000),
            staminaAtual INT NOT NULL DEFAULT 1000 CHECK(staminaAtual BETWEEN 1 AND 1000),
            username VARCHAR(30) NOT NULL,
            senha_hash VARCHAR(255) NOT NULL,
            CONSTRAINT fk_jogador FOREIGN KEY(idPersonagem) REFERENCES personagem_tipo(idPersonagem) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_inventario FOREIGN KEY(idInventario) REFERENCES inventario(idInventario) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_sala FOREIGN KEY(idSala) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_classe FOREIGN KEY(idClasse) REFERENCES classe(idClasse) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS npc (
            idPersonagem INT PRIMARY KEY,
            nome VARCHAR(30) NOT NULL,
            velocidade INT NOT NULL DEFAULT 7 CHECK(velocidade BETWEEN 1 AND 10),
            vidaMax INT NOT NULL DEFAULT 100 CHECK(vidaMax BETWEEN 1 AND 100),
            staminaMax INT NOT NULL DEFAULT 1000 CHECK(staminaMax BETWEEN 1 AND 1000),
            CONSTRAINT fk_npc FOREIGN KEY(idPersonagem) REFERENCES personagem_tipo(idPersonagem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS instancia_npc (
            idInstanciaNPC SERIAL PRIMARY KEY,
            idPersonagem INT NOT NULL,
            idGangue INT NOT NULL,
            idInventario INT NOT NULL,
            idMissao INT NOT NULL,
            idSala INT NOT NULL,
            CONSTRAINT fk_personagem FOREIGN KEY(idPersonagem) REFERENCES npc(idPersonagem) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_inventario FOREIGN KEY(idInventario) REFERENCES inventario(idInventario) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_missao FOREIGN KEY(idMissao) REFERENCES missao(idMissao) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_sala FOREIGN KEY(idSala) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS instancia_estabelecimento (
            idInstEstab SERIAL,
            idEstab INT,
            idSala INT NOT NULL,
            idDono INT NOT NULL,
            PRIMARY KEY(idInstEstab, idEstab),
            CONSTRAINT fk_sala FOREIGN KEY(idSala) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_dono FOREIGN KEY(idDono) REFERENCES instancia_npc(idInstanciaNPC) 
            ON DELETE RESTRICT ON UPDATE CASCADE 
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ataque (
            idAtaque SERIAL PRIMARY KEY,
            descricao VARCHAR(100) NOT NULL,
            dano INT DEFAULT 50 CHECK (dano BETWEEN 1 AND 100)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS animal_tipo (
            idAnimal SERIAL PRIMARY KEY,
            tipo INT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS animal_hostil (
            idAnimal INT PRIMARY KEY,
            habitatNatural VARCHAR(100) NOT NULL,
            especie VARCHAR(30) NOT NULL,
            velocidade INT DEFAULT 50 CHECK(velocidade BETWEEN 1 AND 10),
            vidaMax INT DEFAULT 50 CHECK(vidaMax BETWEEN 1 AND 100),
            staminaMax INT DEFAULT 50 CHECK(staminaMax BETWEEN 1 AND 100),
            textura VARCHAR(30) NOT NULL,
            CONSTRAINT fk_animal_hostil FOREIGN KEY(idAnimal) REFERENCES animal_tipo(idAnimal) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS animal_amigavel (
            idAnimal INT PRIMARY KEY,
            habitatNatural VARCHAR(100) NOT NULL,
            especie VARCHAR(30) NOT NULL,
            velocidade INT DEFAULT 50 CHECK(velocidade BETWEEN 1 AND 10),
            vidaMax INT DEFAULT 50 CHECK(vidaMax BETWEEN 1 AND 100),
            staminaMax INT DEFAULT 50 CHECK(staminaMax BETWEEN 1 AND 100),
            textura VARCHAR(30) NOT NULL,
            CONSTRAINT fk_animal_amigavel FOREIGN KEY(idAnimal) REFERENCES animal_tipo(idAnimal) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS animal_hostil_possui_ataque (
            idAtaque INT,
            idAnimal INT,
            PRIMARY KEY(idAtaque, idAnimal),
            CONSTRAINT fk_ataque FOREIGN KEY(idAtaque) REFERENCES ataque(idAtaque) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_animal_hostil FOREIGN KEY(idAnimal) REFERENCES animal_hostil(idAnimal) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS animal_amigavel_possui_ataque (
            idAtaque INT,
            idAnimal INT,
            PRIMARY KEY(idAtaque, idAnimal),
            CONSTRAINT fk_ataque FOREIGN KEY(idAtaque) REFERENCES ataque(idAtaque) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_animal_amigavel FOREIGN KEY(idAnimal) REFERENCES animal_amigavel(idAnimal) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_tipo (
            idItem SERIAL PRIMARY KEY,
            tipo VARCHAR(30) NOT NULL,
            peso DECIMAL(5,2) NOT NULL CHECK(peso >= 0),
            valor INT NOT NULL DEFAULT 0,
            nivel INT NOT NULL DEFAULT 0
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_consumivel (
            idItem INT PRIMARY KEY,
            tempoEspera INT DEFAULT 0,
            CONSTRAINT fk_item_consumivel FOREIGN KEY(idItem) REFERENCES item_tipo(idItem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_arma (
            idItem INT PRIMARY KEY,
            distanciaAlcance INT DEFAULT 100 CHECK (distanciaAlcance >= 1),
            nivel INT NOT NULL DEFAULT 1,
            tempoRecarregamento INT NOT NULL DEFAULT 3,
            CONSTRAINT fk_item_arma FOREIGN KEY(idItem) REFERENCES item_tipo(idItem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_defesa (
            idItem INT PRIMARY KEY,
            nivelProtecao INT DEFAULT 50 CHECK (nivelProtecao BETWEEN 1 AND 100),
            tipoDefesa VARCHAR(30) NOT NULL,
            CONSTRAINT fk_item_defesa FOREIGN KEY(idItem) REFERENCES item_tipo(idItem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_utilitario (
            idItem INT PRIMARY KEY,
            descricao VARCHAR(60) NOT NULL,
            CONSTRAINT fk_item_utilitario FOREIGN KEY(idItem) REFERENCES item_tipo(idItem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS item_arma_possui_ataque (
            idAtaque INT,
            idItem INT,
            PRIMARY KEY(idAtaque, idItem),
            CONSTRAINT fk_ataque FOREIGN KEY(idAtaque) REFERENCES ataque(idAtaque) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_item FOREIGN KEY(idItem) REFERENCES item_arma(idItem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue (
            idGangue SERIAL PRIMARY KEY,
            nome VARCHAR(30) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_sala (
            idGangue INT,
            idSala INT,
            PRIMARY KEY(idGangue, idSala),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_sala FOREIGN KEY(idSala) REFERENCES sala(idSala) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_estabelecimento (
            idGangue INT,
            idInstEstab INT,
            idEstab INT,
            PRIMARY KEY(idGangue, idInstEstab, idEstab),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_inst_estab FOREIGN KEY(idInstEstab, idEstab) REFERENCES instancia_estabelecimento(idInstEstab, idEstab) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_missao (
            idGangue INT,
            idMissao INT,
            PRIMARY KEY(idGangue, idMissao),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_missao FOREIGN KEY(idMissao) REFERENCES missao(idMissao) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_mapa (
            idGangue INT,
            idMapa INT,
            PRIMARY KEY(idGangue, idMapa),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_mapa FOREIGN KEY(idMapa) REFERENCES mapa(idMapa) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_regiao (
            idGangue INT,
            idRegiao INT,
            PRIMARY KEY(idGangue, idRegiao),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_regiao FOREIGN KEY(idRegiao) REFERENCES regiao(idRegiao) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_animal (
            idGangue INT,
            idAnimal INT,
            PRIMARY KEY(idGangue, idAnimal),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_animal FOREIGN KEY(idAnimal) REFERENCES animal_tipo(idAnimal) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_jogador (
            idGangue INT,
            idPersonagem INT,
            PRIMARY KEY(idGangue, idPersonagem),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_personagem FOREIGN KEY(idPersonagem) REFERENCES jogador(idPersonagem) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS gangue_instancia_npc (
            idGangue INT,
            idInstanciaNPC INT,
            PRIMARY KEY(idGangue, idInstanciaNPC),
            CONSTRAINT fk_gangue FOREIGN KEY(idGangue) REFERENCES gangue(idGangue) 
            ON DELETE RESTRICT ON UPDATE CASCADE,
            CONSTRAINT fk_instancia_npc FOREIGN KEY(idInstanciaNPC) REFERENCES instancia_npc(idInstanciaNPC) 
            ON DELETE RESTRICT ON UPDATE CASCADE
        );
        """
    ]

    try:
        for comando in comandos:
            cur.execute(comando)

        connection.commit()
        print("Tabelas criadas com sucesso")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        connection.close()

if __name__ == '__main__':
    create_tables()
