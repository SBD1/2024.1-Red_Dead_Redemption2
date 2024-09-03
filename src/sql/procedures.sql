create or replace procedure insere_jogador (
    nome varchar(30),
    email varchar(50),
    username varchar(15),
    senha_hash varchar(255)
) as $$
declare
    idPersonagemTipo int;
    idInventario int;
begin
    -- Insert new personagem_tipo and get its ID
    insert into personagem_tipo (tipo) values ('JOG');
    select currval(pg_get_serial_sequence('personagem_tipo', 'idPersonagemTipo')) into idPersonagemTipo;
    
    -- Insert new inventario and get its ID
    insert into inventario (totalItens, capacidade) values (0, 20);
    select currval(pg_get_serial_sequence('inventario', 'idInventario')) into idInventario;

    -- Insert new jogador
    insert into jogador
    (idPersonagem, idInventario, idCidade, nome, email, username, senha_hash)
    values (idPersonagemTipo, idInventario, 1, nome, email, username, senha_hash);

exception
    when others then
        -- Handle exceptions
        raise notice 'Houve um erro durante a inserção do novo jogador: %', SQLERRM;
        -- Rollback the transaction if an error occurs
        rollback;
end;
$$ language plpgsql;
