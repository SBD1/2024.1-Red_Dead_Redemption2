CREATE OR REPLACE FUNCTION check_catalogo_fc() RETURNS trigger AS $check_catalogo_fc$
BEGIN
    PERFORM * FROM CATALOGO WHERE idItem = NEW.idItem;
    IF FOUND THEN
    RAISE EXCEPTION 'Este item já existe na tabela de catalogo';
    END IF;
    RETURN NEW; 
END;
$check_catalogo_fc$ LANGUAGE plpgsql;


CREATE TRIGGER check_catalogo
BEFORE UPDATE OR INSERT ON FERRAMENTA
FOR EACH ROW EXECUTE PROCEDURE check_catalogo_fc();


CREATE TRIGGER check_catalogo
BEFORE UPDATE OR INSERT ON TONICO
FOR EACH ROW EXECUTE PROCEDURE check_catalogo_fc();


CREATE OR REPLACE FUNCTION check_inimigo_fc() RETURNS trigger AS $check_inimigo_fc$
BEGIN
    PERFORM * FROM INIMIGO WHERE idNPC = NEW.idNPC;
    IF FOUND THEN
    RAISE EXCEPTION 'Este NPC já existe na tabela de inimigos';
    END IF;
    RETURN NEW; 
END;
$check_inimigo_fc$ LANGUAGE plpgsql;


CREATE TRIGGER check_inimigo
BEFORE UPDATE OR INSERT ON TREINADOR
FOR EACH ROW EXECUTE PROCEDURE check_inimigo_fc();


CREATE OR REPLACE FUNCTION update_area() RETURNS trigger AS $update_area$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET NArea = NArea - 1 WHERE idArea = old.idArea;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET NArea = NArea + 1 WHERE idArea = old.idArea;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idArea <> OLD.idArea) THEN
            UPDATE AREA SET NArea = NArea - 1 WHERE idArea = old.idArea;
            UPDATE AREA SET NArea = NArea + 1 WHERE idArea = new.idArea;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_area$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeAreas
AFTER DELETE OR UPDATE OR INSERT ON JOGADOR
FOR EACH ROW EXECUTE PROCEDURE update_area();

CREATE OR REPLACE FUNCTION update_arsenal() RETURNS trigger AS $update_arsenal$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET Narsenal = Narsenal - 1 WHERE idArsenal = old.idArsenal;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET Narsenal = Narsenal + 1 WHERE idArsenal = old.idArsenal;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idArsenal <> OLD.idArsenal) THEN
            UPDATE AREA SET Narsenal = Narsenal - 1 WHERE idArsenal = old.idArsenal;
            UPDATE AREA SET Narsenal = Narsenal + 1 WHERE idArsenal = new.idArsenal;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_arsenal$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeArsenais
AFTER DELETE OR UPDATE OR INSERT ON JOGADOR
FOR EACH ROW EXECUTE PROCEDURE update_arsenal();


CREATE OR REPLACE FUNCTION update_npc() RETURNS trigger AS $update_npc$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET N_NPC = N_NPC - 1 WHERE idNPC = old.idNPC;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET N_NPC = N_NPC + 1 WHERE idNPC = old.idNPC;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idNPC <> OLD.idNPC) THEN
            UPDATE AREA SET N_NPC = N_NPC - 1 WHERE idNPC = old.idNPC;
            UPDATE AREA SET N_NPC = N_NPC + 1 WHERE idNPC = new.idNPC;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_npc$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeNPC
AFTER DELETE OR UPDATE OR INSERT ON TREINAMENTO
FOR EACH ROW EXECUTE PROCEDURE update_npc();


CREATE TRIGGER NroDeNPC
AFTER DELETE OR UPDATE OR INSERT ON LOJA
FOR EACH ROW EXECUTE PROCEDURE update_npc();


CREATE OR REPLACE FUNCTION update_arma() RETURNS trigger AS $update_arma$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET NArma = NArma - 1 WHERE idArma = old.idArma;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET NArma = NArma + 1 WHERE idArma = old.idArma;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idArma <> OLD.idArma) THEN
            UPDATE AREA SET NArma = NArma - 1 WHERE idArma = old.idArma;
            UPDATE AREA SET NArma = NArma + 1 WHERE idArma = new.idArma;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_arma$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeArma
AFTER DELETE OR UPDATE OR INSERT ON ARSENAL
FOR EACH ROW EXECUTE PROCEDURE update_arma();


CREATE TRIGGER NroDeArma
AFTER DELETE OR UPDATE OR INSERT ON TREINAMENTO
FOR EACH ROW EXECUTE PROCEDURE update_arma();


CREATE OR REPLACE FUNCTION update_item() RETURNS trigger AS $update_item$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET NItem = NItem - 1 WHERE idItem = old.idItem;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET NItem = NItem + 1 WHERE idItem = old.idItem;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idItem <> OLD.idItem) THEN
            UPDATE AREA SET NItem = NItem - 1 WHERE idItem = old.idItem;
            UPDATE AREA SET NItem = NItem + 1 WHERE idItem = new.idItem;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_item$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeItem
AFTER DELETE OR UPDATE OR INSERT ON INSTANCIA_ITEM
FOR EACH ROW EXECUTE PROCEDURE update_item();


CREATE TRIGGER NroDeItem
AFTER DELETE OR UPDATE OR INSERT ON NPC
FOR EACH ROW EXECUTE PROCEDURE update_item();


CREATE OR REPLACE FUNCTION update_mapa() RETURNS trigger AS $update_mapa$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        UPDATE AREA SET NMapa = NMapa - 1 WHERE idMapa = old.idMapa;
    ELSIF (TG_OP = 'INSERT') then
        UPDATE AREA SET NMapa = NMapa + 1 WHERE idMapa = old.idMapa;
    ELSIF (TG_OP = 'UPDATE') THEN
        IF(NEW.idMapa <> OLD.idMapa) THEN
            UPDATE AREA SET NMapa = NMapa - 1 WHERE idMapa = old.idMapa;
            UPDATE AREA SET NMapa = NMapa + 1 WHERE idMapa = new.idMapa;
        END IF;
    END IF;
    RETURN NULL;
END;

$update_mapa$ LANGUAGE plpgsql;


CREATE TRIGGER NroDeMapa
AFTER DELETE OR UPDATE OR INSERT ON REGIAO
FOR EACH ROW EXECUTE PROCEDURE update_mapa();


CREATE OR REPLACE FUNCTION st_alteracoes_gangue() RETURNS trigger AS $st_alteracoes_gangue$
BEGIN
    RAISE NOTICE 'Statement - Tentou-se remover dados da tabela Gangue';
    RETURN NULL;
END;

$st_alteracoes_gangue$ LANGUAGE plpgsql;


CREATE TRIGGER st_alteracoes_gangue_aviso
AFTER DELETE ON JOGADOR
EXECUTE PROCEDURE st_alteracoes_gangue();


CREATE OR REPLACE FUNCTION st_respawn_enemy() RETURNS TRIGGER AS $st_respawn_enemy$
BEGIN
    PERFORM pg_sleep(10);
    UPDATE INSTANCIA_INIMIGO SET pontosvida = old.pontosvidamax WHERE idinstancia_inimigo = old.idinstancia_inimigo;
END;


$st_respawn_enemy$ LANGUAGE plpgsql;


CREATE TRIGGER respawn_enemy
AFTER UPDATE ON INSTANCIA_INIMIGO
EXECUTE PROCEDURE st_respawn_enemy();


SELECT  event_object_table AS table_name ,trigger_name         
FROM information_schema.triggers  
GROUP BY table_name , trigger_name 
ORDER BY table_name ,trigger_name 