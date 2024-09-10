--Área

CREATE OR REPLACE PROCEDURE validar_jogador_area()
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM AREA WHERE idArea = NEW.idArea) THEN
        RAISE EXCEPTION 'A área % não existe', NEW.idArea;
    END IF;
END;
$$;

CREATE TRIGGER trg_validar_jogador_area
BEFORE INSERT OR UPDATE ON JOGADOR
FOR EACH ROW
EXECUTE PROCEDURE validar_jogador_area();

-- Inventário

CREATE OR REPLACE PROCEDURE gerenciar_inventario(
    p_idJogador INT, 
    p_idItem INT, 
    p_acao VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM JOGADOR WHERE idJogador = p_idJogador) THEN
        RAISE EXCEPTION 'O jogador % não existe', p_idJogador;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM ITEM WHERE idItem = p_idItem) THEN
        RAISE EXCEPTION 'O item % não existe', p_idItem;
    END IF;

    IF p_acao = 'adicionar' THEN
        INSERT INTO INSTANCIA_ITEM (idItem, idJogador)
        VALUES (p_idItem, p_idJogador);
    
    ELSIF p_acao = 'remover' THEN
        DELETE FROM INSTANCIA_ITEM 
        WHERE idItem = p_idItem AND idJogador = p_idJogador;
    
    ELSE
        RAISE EXCEPTION 'Ação % inválida. Use "adicionar" ou "remover"', p_acao;
    END IF;
END;
$$;

-- Instancia Inimigo

CREATE OR REPLACE PROCEDURE verificar_duplicidade_instancia_inimigo(
    p_idNPC INT, 
    p_idArea INT, 
    p_idItem INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM INSTANCIA_INIMIGO 
        WHERE idNPC = p_idNPC 
        AND idArea = p_idArea 
        AND idItem = p_idItem
    ) THEN
        RAISE EXCEPTION 'A instância do inimigo já existe na área % com o item %', p_idArea, p_idItem;
    END IF;
END;
$$;

CALL verificar_duplicidade_instancia_inimigo(1, 10, 5);

-- ataque

CREATE OR REPLACE PROCEDURE atualizar_vida_jogador(
    p_idJogador INT, 
    p_dano INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM JOGADOR WHERE idJogador = p_idJogador) THEN
        RAISE EXCEPTION 'O jogador % não existe', p_idJogador;
    END IF;

    UPDATE JOGADOR
    SET pontosVida = GREATEST(pontosVida - p_dano, 0)
    WHERE idJogador = p_idJogador;
END;
$$;

CALL atualizar_vida_jogador(1, 20);
