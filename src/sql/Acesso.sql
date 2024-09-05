create role administrator with superuser;
create user red_admin with password 'red123' in role administrator;

create role owners;
grant select, insert, update, delete on red.area, red.grimorio, red.item, red.jogador, red.loja to owners with grant option; 
create user red_game_owner with password 'red_owner123' in role owners;


create role jogadores;
grant select, insert, delete on red.grimorio_jogador to jogadores with grant option;
create user red_jogadores with password 'red_jogadores123' in role jogadores;