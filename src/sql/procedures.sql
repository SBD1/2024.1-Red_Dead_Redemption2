create or replace procedure insere_jogador (
    nome varchar(30),
    email varchar(50),
    username varchar(15),
    senha varchar(50)
) as $$
declare
    idPersonagemTipo int;
    idInventario int;
begin
    insert into personagem_tipo (tipo) values ('JOG');
    select currval(pg_get_serial_sequence('personagem_tipo', 'idPersonagemTipo')) into idPersonagemTipo;
    
    insert into inventario (totalItens, capacidade) values (0, 20);
    select currval(pg_get_serial_sequence('inventario', 'idInventario')) into idInventario;

    insert into jogador
    (idPersonagem, idInventario, idCidade, nome, email, username, senha)
    values (idPersonagemTipo, idInventario, 1, nome, email, username, senha);

exception
    when others then
        raise notice 'Houve um erro durante a inserção do novo jogador: %', SQLERRM;
        rollback;
end;
$$ language plpgsql;

create or replace function check_jogador_existe (
    p_username varchar(15),
    p_senha varchar(50)
) returns boolean as $$
begin
    if exists (
        select 1
        from jogador
        where username = p_username and senha = p_senha
    ) then
        return true;
    else
        return false;
    end if;
end;
$$ language plpgsql;