create table ataque (
	idAnimal serial,
	descricao varchar(100) not null,
	dano int default 50 check (dano between 1 and 100,
	constraint pk_ataque primary key(idAnimal)
);

create table animal_hostil_possui_ataque (
	idAtaque int not null,
	idAnimal int not null,
	constraint pk primary key(idAtaque, idAnimal),
	constraint fk_ataque foreign key(idAtaque) references ataque(idAtaque) on delete cascade,
	constraint fk_animal foreign key(idAnimal) references animal_hostil(idAnimal) on delete cascade on update cascade,
);

create table animal_amigavel (
	idAnimal int not null,
	idRegiaoHabitatNatural int not null,
	especie varchar(30) not null,
	velocidade int default 50 check(velocidade between 1 and 100),
	vidaMax int default 50 check(vidaMax between 1 and 100),
	staminaMax int default 50 check(velocidade between 1 and 100),
	textura varchar(30) not null,
	constraint pk_animal_amigavel primary key(idAnimal),
	constraint fk_animal_amigavel foreign key(idAnimal) references animal_tipo(idAnimal) on delete cascade on update cascade,
	constraint fk_regiao foreign key(idRegiaoHabitatNatural) references regiao(idRegiao) on delete cascade on update cascade,
);

create table animal_hostil (
	idAnimal int not null,
	idRegiaoHabitatNatural int not null,
	especie varchar(30) not null,
	velocidade int default 50 check(velocidade between 1 and 100),
	vidaMax int default 50 check(vidaMax between 1 and 100),
	staminaMax int default 50 check(velocidade between 1 and 100),
	textura varchar(30) not null,
	constraint pk_animal_hostil primary key(idAnimal),
	constraint fk_animal_amigavel foreign key(idAnimal) references animal_tipo(idAnimal) on delete cascade on update cascade,
	constraint fk_regiao foreign key(idRegiaoHabitatNatural) references regiao(idRegiao) on delete cascade on update cascade,
);

create table instancia_animal (
	idInstanciaAnimal serial,
	idAnimal int not null,
	vidaAtual int default 100,
	staminaAtual int default 100,
	idSala int not null,
	constraint pk_instancia_animal primary key(idInstanciaAnimal, idAnimal),
	constraint fk_animal foreign key(idAnimal) references animal_tipo(idAnimal) on delete cascade on update cascade,
	constrait fk_sala foreign key references sala(idSala) on delete cascade on update cascade,
);

create table animal_tipo (
	idAnimal serial,
	tipo int not null,
	constraint pk_animal_tipo primary key(idAnimal),
);

create table jogador_domou_animal_amigavel (
	idInstanciaAnimal int not null,
	idJogador int not null,
	constraint pks primary key (idInstanciaAnimal, idJogador),
	constraint fk_instancia foreign key(idInstanciaAnimal) references instancia_animal(idInstanciaAnimal) on delete cascade on update cascade,
	constraint fk_jogador foreign key(idJogador) references jogador(idPersonagem) on delete cascade on update cascade,
);

create table animal_hostil_ataca_jogador (
	idInstanciaAnimal int not null,
	idJogador int not null,
	constraint pks primary key (idInstanciaAnimal, idJogador),
	constraint fk_instancia foreign key(idInstanciaAnimal) references instancia_animal(idInstanciaAnimal) on delete cascade on update cascade,
	constraint fk_jogador foreign key(idJogador) references jogador(idPersonagem) on delete cascade on update cascade,
);

create table mapa (
	idMapa serial
	nome varchar(30) not null,
	constraint pk primary key(idMapa),
);

create table regiao (
	idRegiao serial,
	idMapa int not null,
	nome varchar(30) not null,
	descricao varchar(60) not null,
	constraint pk primary key(idRegiao),
	constraint fk_mapa foreign key idMapa references mapa(idMapa) on delete cascade on update cascade,
);

create table regiao_faz_fronteira_com_regiao (
	idRegiaoOrigem int not null,
	idRegiaoDestino int not null,
	constraint pks primary key(idRegiaoOrigem, idRegiaoDestino),
	constraint fk_origem_destino foreign key (idRegiaoOrigem, idRegiaoDestino) references regiao(idRegiao, idRegiao) on delete cascade on update cascade,
);

create table sala (
	idSala serial,
	idRegiao int not null,
	nome varchar(30) not null,
	descricao varchar(60) not null,
	constraint pk primary key(idSala),
	constraint fk_regiao foreign key idRegiao references regiao(idRegiao) on delete cascade on update cascade,
);

create table sala_conecta_com_sala (
	idSalaOrigem int not null,
	idSalaDestino int not null,
	constraint pks primary key(idSalaOrigem, idSalaDestino),
	constraint fks foreign key(idSalaOrigem, idSalaDestino) references sala(idSala, idSala) on delete cascade on update cascade,
);

create table estabelecimento (
	idEstab serial,
	nome varchar(30) not null,
	descricao varchar(60) not null,
	constraint pk primary key(idEstabelecimento),
);

-- Consertar isto depois
create table instancia_estabelecimento (
	idInstEstab serial,
	idEstab int not null,
	idSala int not null,
	idDono int not null,
	constraint pk(idInstEstab, idEstab),
	constraint fk_estab foreign key idEstab references estabelecimento (idEstab) on delete cascade on update cascade,
	constraint fk_sala foreign key idSala references sala(idSala) on delete cascade on update cascade,
	constraint fk_dono foreign key
);

create table objetivo (
	idObjetivo serial,
	titulo varchar(60) not null,
	retornoXP int not null check(retornoXP between 1 and 1000),
	retornoDinheiro int not null check(retornoDinheiro between 1 and 1000),
	idMissao int not null,
	constraint pk primary key(idObjetivo),
	constraint fk foreign key idMissao references missao(idMissao) on delete cascade on update cascade,
);

create table historia (
	idHistoria serial,
	titulo varchar(60) not null,
	enredo varchar(1000) not null,
	constraint pk primary key(idHistoria),
	
);

create table missao (
	idMissao serial,
	titulo varchar(60) not null,
	nivelDificuldade int not null check(nivelDificuldade between 1 and 10),
	idHistoria int not null,
	idRegiao int not null,
	status decimal(3,2) not null default 0.00,
	constraint pk primary key(idMissao),
	constraint fk_historia foreign key idHistoria references historia(idHistoria) on delete cascade on update cascade,
	constraint fk_regiao foreign key idRegiao references regiao(idRegiao) on delete cascade on update cascade
);

create table missao_depende_de_missao (
    idMissaoAtual int not null,
    idMissaoAnterior int not null,
    constraint pk primary key(idMissaoAtual, idMissaoAnterior),
    constraint fks foreign key (idMissaoAtual, idMissaoAnterior) references missao(idMissao, idMissao) on delete cascade on update cascade,    
);

create table classe (
    idClasse serial,
    nome varchar(20) not null,    
    constraint pk primary key(idClasse),
);

create table habilidade (
    idHabilidade serial,
    nome varchar(30) not null,
    porcentagem decimal(3,2) not null default 0.00 check(porcentagem between 0.00 and 1.00),
    constraint pk primary key(idHabilidade),
);

create table classe_possui_habilidade (
    idClasse int not null,
    idHabilidade int not null,
    constraint pk primary key(idClasse, idHabilidade),
    constraint fk_classe foreign key idClasse references classe(idClasse) on delete cascade on update cascade,
    constraint fk_habilidade foreign key idHabilidade references habilidade(idHabilidade) on delete cascade on update cascade,
);

create table gangue (
    idGangue serial,
    nome varchar(30) not null,
    descricao varchar(60) not null,
    idInstanciaNPCLider int not null,
    constraint pk primary key(idGangue),
    constraint fk_instancia_npc foreign key idInstanciaNPCLider references instancia_npc(idInstanciaNPC) on delete cascade on update cascade,
);

create table gangue_confronta_gangue (
    idGangueVencedora int not null,
    idGanguePerdedora int not null,
    dataConfronto date not null default current_date,
    constraint pk primary key(idGangueVencedora, idGanguePerdedora),
    constraint fk_vencedora foreign key idGangueVencedora references gangue(idGangue) on delete cascade on update cascade,
);

create table dialogo (
    idDialogo serial,
    idInstanciaNPCFalante int not null,
    descricao varchar(100) not null,
    constraint pk primary key(idDialogo),
    constraint fk_instancia_npc foreign key idInstanciaNPCFalante references instancia_npc(idInstanciaNPC) on delete cascade on update cascade,
);

create table linha_de_fala (
    idLinhaDeFala serial,
    idDialogo int not null,
    texto varchar(100) not null,
    constraint pk primary key(idLinhaDeFala),
    constraint fk_dialogo foreign key idDialogo references dialogo(idDialogo) on delete cascade on update cascade,
);

create table jogador (
	idPersonagem int not null,
	idInventario int not null,
	idSala int not null,
	idClasse int not null,
	idGangue int not null,
	nome varchar(30) not null,
	xp int not null default 0,
	dinheiro not null default 0,
	velocidade int not null default 7 check(velocidade between 1 and 10),
	vidaMax int not null default 100 check(vidaMax between 1 and 100),
	vidaAtual int not null default 100 check(vidaAtual between 1 and 100),
	staminaMax int not null default 1000 check(staminaMax between 1 and 1000),
	staminaAtual int not null default 1000 check(staminaAtual between 1 and 1000),
	username varchar(30) not null,
	senha_hash varchar(255) not null,
	constraint pk_jogador primary key(idPersonagem),
	constraint fk_jogador foreign key idPersonagem references personagem_tipo(idPersonagem) on delete cascade on update cascade,
	constraint fk_inventario foreign key idInventario references inventario(idInventario) on delete cascade on update cascade,
	constraint fk_sala foreign key idSala references sala(idSala) on delete cascade on update cascade,
	constraint fk_classe foreign key idClasse references classe(idClasse) on delete cascade on update cascade,
	constraint fk_gangue foreign key idGangue references gangue(idGangue) on delete cascade on update cascade,
);

create table npc (
	idPersonagem int not null,
	nome varchar(30) not null,
	velocidade int not null default 7 check(velocidade between 1 and 10),
	vidaMax int not null default 100 check(vidaMax between 1 and 100),
	staminaMax int not null default 1000 check(staminaMax between 1 and 1000),
	constraint pk_npc primary key(idPersonagem),
	constraint fk_npc foreign key idPersonagem references personagem_tipo(idPersonagem) on delete cascade on update cascade,
);

create table instancia_npc (
	idInstanciaNPC serial,
	idPersonagem int not null,
	idGangue int not null
	idInventario int not null,
	idMissao int not null,
	idSala int not null,
	constraint pk_instancia_npc primary key(idInstanciaNPC),
	constraint fk_personagem foreign key idPersonagem references npc(idPersonagem) on delete cascade on update cascade,
	constraint fk_gangue foreign key idGangue references gangue(idGangue) on delete cascade on update cascade,
	constraint fk_inventario foreign key idInventario references inventario(idInventario) on delete cascade on update cascade,
	constraint fk_missao foreign key idMissao references missao(idMissao) on delete cascade on update cascade,
	constraint fk_sala foreign key idSala references sala(idSala) on delete cascade on update cascade,
);

create table personagem_tipo (
	idPersonagem serial,
	tipo int not null,
	constraint pk_personagem primary key(idPersonagem)
);

create table jogador_cumpre_missao (
	idJogador int not null,
	idMissao int not null,
	dataMissao date not null,
	retornoTotalXP int not null,
	retornoTotalDinheiro int not null,
	constraint pk_jogador_missao primary key(idJogador, idMissao),
	constraint fk_jogador foreign key idJogador references jogador(idPersonagem) on delete cascade on update cascade,
);

create table inventario (
	idInventario serial,
	totalItens int not null default 0,
	capacidade int not null,
	constraint pk_inventario primary key(idInventario),
);