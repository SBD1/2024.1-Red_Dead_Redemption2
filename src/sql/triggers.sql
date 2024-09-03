begin;

create or replace function atualiza_qtd_itens_inventario() 
returns trigger as $$
begin
    if tg_op = 'INSERT' then
        update inventario set totalItens = totalItens + 1
        where idInventario = new.idInventario;
    elsif tg_op = 'DELETE' then
        update inventario set totalItens = totalItens - 1
        where idInventario = old.idInventario;
    elsif tg_op = 'UPDATE' then
        if old.idInventario <> new.idInventario then
            update inventario set totalItens = totalItens + 1
            where idInventario = new.idInventario;
            update inventario set totalItens = totalItens - 1
            where idInventario = old.idInventario;
        end if;
    end if;
    return NEW;
end;
$$ language plpgsql;

create trigger atualiza_inventario
after insert or update or delete on instancia_item
for each row execute procedure atualiza_qtd_itens_inventario();

create or replace function atualiza_qtd_habitantes() 
returns trigger as $$
begin
    if tg_op = 'INSERT' then
        update cidade set qtdHabitantes = qtdHabitantes + 1
        where idCidade = new.idCidade;
    elsif tg_op = 'DELETE' then
        update cidade set qtdHabitantes = qtdHabitantes - 1
        where idCidade = old.idCidade;
    elsif tg_op = 'UPDATE' then
        if new.idCidade <> old.idCidade then
            update cidade set qtdHabitantes = qtdHabitantes + 1
            where idCidade = new.idCidade;
            update cidade set qtdHabitantes = qtdHabitantes - 1
            where idCidade = old.idCidade;
        end if;
    end if;
    return NEW;
end;
$$ language plpgsql;

create trigger atualiza_instancias_animais
after insert or update or delete on instancia_animal
for each row execute procedure atualiza_qtd_habitantes();

create trigger atualiza_instancias_npcs
after insert or update or delete on instancia_npc
for each row execute procedure atualiza_qtd_habitantes();

create trigger atualiza_jogadores
after insert or update or delete on jogador
for each row execute procedure atualiza_qtd_habitantes();


create or replace function calcula_retorno_xp_total() 
returns trigger as $$
begin
    update jogador_cumpre_missao
    set retornoTotalXP = (select sum(retornoXP) from objetivo where idMissao = old.idMissao)
    where idMissao = old.idMissao;

    if old.idMissao <> new.idMissao then
        update jogador_cumpre_missao
        set retornoTotalXP = (select sum(retornoXP) from objetivo where idMissao = new.idMissao)
        where idMissao = new.idMissao;
    end if;
    return NEW;
end;
$$ language plpgsql;

create trigger calcula_total_xp
after insert or update or delete on objetivo
for each row execute procedure calcula_retorno_xp_total();

create or replace function calcula_retorno_dinheiro_total() 
returns trigger as $$
begin
    update jogador_cumpre_missao
    set retornoTotalDinheiro = (select sum(retornoDinheiro) from objetivo where idMissao = old.idMissao)
    where idMissao = old.idMissao;

    if old.idMissao <> new.idMissao then
        update jogador_cumpre_missao
        set retornoTotalDinheiro = (select sum(retornoDinheiro) from objetivo where idMissao = new.idMissao)
        where idMissao = new.idMissao;
    end if;
    return NEW;
end;
$$ language plpgsql;

create trigger calcula_total_dinheiro
after insert or update or delete on objetivo
for each row execute procedure calcula_retorno_dinheiro_total();

create or replace function calcula_status() 
returns trigger as $$
declare
    objetivos_feitos integer;
    total_objetivos integer;
begin
    select count(*) into objetivos_feitos 
    from jogador_cumpre_objetivo 
    where idJogador = new.idJogador and idObjetivo = new.idObjetivo;

    select count(*) into total_objetivos 
    from objetivo 
    where idMissao = new.idMissao;

    update jogador_cumpre_missao
    set status = round((objetivos_feitos::float / total_objetivos::float) * 100, 2)
    where idJogador = new.idJogador and idMissao = new.idMissao;

    return NEW;
end;
$$ language plpgsql;

create trigger calcula_status
after insert or update or delete on jogador_cumpre_objetivo
for each row execute procedure calcula_status();

commit;