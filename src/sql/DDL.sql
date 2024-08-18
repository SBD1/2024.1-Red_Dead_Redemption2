create type tipo_personagem as enum('JOG', 'NPC'); 
create type tipo_animal as enum('AMG', 'HST');
-- Consumível, Equipável, Arma Fogo, Arma Melee
create type tipo_item as enum('CON', 'EQP', 'AFG', 'AML');

create table if not exists mapa (
	idMapa serial primary key,
	nome varchar(30) not null
);

create table if not exists estado (
	idEstado serial primary key,
	idMapa int not null,
	nome varchar(30) not null,
	sigla char(2) not null unique,
	descricao varchar(1000) not null,
	constraint fk_mapa foreign key(idMapa) references mapa(idMapa) on delete restrict on update cascade
);

create table if not exists estado_faz_fronteira_com_estado (
	siglaEstadoOrigem char(2) not null,
	siglaEstadoDestino char(2) not null,
	primary key(siglaEstadoOrigem, siglaEstadoDestino),
	constraint fk_origem foreign key (siglaEstadoOrigem) references estado(sigla) on delete restrict on update cascade,
	constraint fk_destino foreign key (siglaEstadoDestino) references estado(sigla) on delete restrict on update cascade
);

create table if not exists cidade (
	idCidade serial primary key,
	nome varchar(30) not null unique,
	siglaEstado char(2) not null,
	descricao varchar(1000) not null,
	constraint fk_estado foreign key(siglaEstado) references estado(sigla) on delete restrict on update cascade
);

create table if not exists cidade_conecta_com_cidade (
	idCidadeOrigem int,
	idCidadeDestino int,
	primary key(idCidadeOrigem, idCidadeDestino),
	constraint fk_origem foreign key(idCidadeOrigem) references cidade(idCidade) on delete restrict on update cascade,
	constraint fk_destino foreign key(idCidadeDestino) references cidade(idCidade) on delete restrict on update cascade
);

create table if not exists estabelecimento (
	idEstab serial primary key,
	nome varchar(30) not null,
	descricao varchar(1000) not null
);

create table if not exists personagem_tipo (
	idPersonagem int primary key,
	tipo tipo_personagem not null
);

create table if not exists inventario (
	idInventario serial primary key,
	totalItens int not null default 0,
	capacidade int not null
);

create table if not exists classe (
    idClasse serial primary key,
    nome varchar(20) not null    
);

create table if not exists historia (
	idHistoria serial primary key,
	titulo varchar(60) not null,
	enredo varchar(2000) not null
);

create table if not exists missao (
	idMissao serial primary key,
	titulo varchar(60) not null,
	nivelDificuldade int not null check(nivelDificuldade between 1 and 10),
	idHistoria int not null,
	idEstado int,
	constraint fk_historia foreign key(idHistoria) references historia(idHistoria) on delete restrict on update cascade,
	constraint fk_estado foreign key(idEstado) references estado(idEstado) on delete restrict on update cascade
);

create table if not exists missao_depende_de_missao (
    idMissaoAtual int,
    idMissaoAnterior int,
	primary key(idMissaoAtual, idMissaoAnterior),
    constraint fk_atual foreign key(idMissaoAtual) references missao(idMissao) on delete restrict on update cascade,
	constraint fk_anterior foreign key(idMissaoAnterior) references missao(idMissao) on delete restrict on update cascade   
);

create table if not exists jogador (
	idPersonagem int primary key,
	idInventario int not null,
	idCidade int not null,
	idClasse int not null,
	idGangue int not null,
	nome varchar(30) not null,
	xp int not null default 0,
	dinheiro int not null default 0,
	velocidade int not null default 7 check(velocidade between 1 and 10),
	vidaMax int not null default 100 check(vidaMax between 1 and 100),
	vidaAtual int not null default 100 check(vidaAtual between 1 and 100),
	staminaMax int not null default 1000 check(staminaMax between 1 and 1000),
	staminaAtual int not null default 1000 check(staminaAtual between 1 and 1000),
	username varchar(30) not null,
	senha_hash varchar(255) not null,
	constraint fk_jogador foreign key(idPersonagem) references personagem_tipo(idPersonagem) on delete restrict on update cascade,
	constraint fk_inventario foreign key(idInventario) references inventario(idInventario) on delete restrict on update cascade,
	constraint fk_cidade foreign key(idCidade) references cidade(idCidade) on delete restrict on update cascade,
	constraint fk_classe foreign key(idClasse) references classe(idClasse) on delete restrict on update cascade
);

create table if not exists npc (
	idPersonagem int primary key,
	nome varchar(30) not null,
	velocidade int not null default 7 check(velocidade between 1 and 10),
	vidaMax int not null default 100 check(vidaMax between 1 and 100),
	staminaMax int not null default 1000 check(staminaMax between 1 and 1000),
	constraint fk_npc foreign key(idPersonagem) references personagem_tipo(idPersonagem) on delete restrict on update cascade
);

create table if not exists instancia_npc (
	idInstanciaNPC serial primary key,
	idPersonagem int not null,
	idGangue int,
	idInventario int not null,
	idMissao int,
	idCidade int not null,
	constraint fk_personagem foreign key(idPersonagem) references npc(idPersonagem) on delete restrict on update cascade,
	constraint fk_inventario foreign key(idInventario) references inventario(idInventario) on delete restrict on update cascade,
	constraint fk_missao foreign key(idMissao) references missao(idMissao) on delete restrict on update cascade,
	constraint fk_cidade foreign key(idCidade) references cidade(idCidade) on delete restrict on update cascade
);

create table if not exists instancia_estabelecimento (
	idInstEstab serial,
	idEstab int,
	idCidade int not null,
	idDono int not null,
	primary key(idInstEstab, idEstab),
	constraint fk_cidade foreign key(idCidade) references cidade(idCidade) on delete restrict on update cascade,
	constraint fk_dono foreign key(idDono) references instancia_npc(idInstanciaNPC) on delete restrict on update cascade 
);

create table if not exists ataque (
	idAtaque serial primary key,
	descricao varchar(1000) not null,
	dano int default 50 check (dano between 1 and 100)
);

create table if not exists animal_tipo (
	idAnimal serial primary key,
	tipo int not null
);

create table if not exists animal_hostil (
	idAnimal int primary key,
	habitatNatural varchar(100) not null,
	especie varchar(30) not null,
	velocidade int default 50 check(velocidade between 1 and 10),
	vidaMax int default 50 check(vidaMax between 1 and 100),
	staminaMax int default 50 check(staminaMax between 1 and 100),
	textura varchar(30) not null,
	constraint fk_animal_amigavel foreign key(idAnimal) references animal_tipo(idAnimal) on delete restrict on update cascade
);

create table if not exists animal_amigavel (
	idAnimal int primary key,
	habitatNatural varchar(100) not null,
	especie varchar(30) not null,
	velocidade int default 50 check(velocidade between 1 and 10),
	vidaMax int default 50 check(vidaMax between 1 and 100),
	staminaMax int default 50 check(staminaMax between 1 and 100),
	textura varchar(30) not null,
	constraint fk_animal_amigavel foreign key(idAnimal) references animal_tipo(idAnimal) on delete restrict on update cascade
);

CREATE table if not exists animal_hostil_possui_ataque (
    idAtaque int,
    idAnimal int,
	primary key(idAtaque, idAnimal),
    constraint fk_ataque foreign key(idAtaque) references ataque(idAtaque) on delete restrict,
    constraint fk_animal foreign key(idAnimal) references animal_hostil(idAnimal) on delete restrict on update cascade
);

create table if not exists instancia_animal (
	idInstanciaAnimal serial primary key,
	idAnimal int not null,
	vidaAtual int default 100,
	staminaAtual int default 100,
	idCidade int not null,
	constraint fk_animal foreign key(idAnimal) references animal_tipo(idAnimal) on delete restrict on update cascade,
	constraint fk_cidade foreign key(idCidade) references cidade(idCidade) on delete restrict on update cascade
);

create table if not exists jogador_domou_animal_amigavel (
	idInstanciaAnimal int not null,
	idJogador int not null,
	constraint pks primary key (idInstanciaAnimal, idJogador),
	constraint fk_instancia foreign key(idInstanciaAnimal) references instancia_animal(idInstanciaAnimal) on delete restrict on update cascade,
	constraint fk_jogador foreign key(idJogador) references jogador(idPersonagem) on delete restrict on update cascade
);

create table if not exists animal_hostil_ataca_jogador (
	idInstanciaAnimal int not null,
	idJogador int not null,
	primary key (idInstanciaAnimal, idJogador),
	constraint fk_instancia foreign key(idInstanciaAnimal) references instancia_animal(idInstanciaAnimal) on delete restrict on update cascade,
	constraint fk_jogador foreign key(idJogador) references jogador(idPersonagem) on delete restrict on update cascade
);

create table if not exists objetivo (
	idObjetivo serial primary key,
	titulo varchar(100) not null,
	retornoXP int not null check(retornoXP between 1 and 1000),
	retornoDinheiro int not null check(retornoDinheiro between 1 and 1000),
	idMissao int not null,
	constraint fk_missao foreign key(idMissao) references missao(idMissao) on delete restrict on update cascade
);

create table if not exists habilidade (
    idHabilidade serial primary key,
    nome varchar(30) not null,
    porcentagem decimal(3,2) not null default 0.00 check(porcentagem between 0.00 and 1.00)
);

create table if not exists classe_possui_habilidade (
    idClasse int,
    idHabilidade int,
	primary key(idClasse, idHabilidade),
    constraint fk_classe foreign key(idClasse) references classe(idClasse) on delete restrict on update cascade,
    constraint fk_habilidade foreign key(idHabilidade) references habilidade(idHabilidade) on delete restrict on update cascade
);

create table if not exists gangue (
    idGangue serial primary key,
    nome varchar(50) not null,
    idInstanciaNPCLider int not null,
    descricao varchar(2000) not null,
    constraint fk_instancia_npc foreign key(idInstanciaNPCLider) references instancia_npc(idInstanciaNPC) on delete restrict on update cascade
);

create table if not exists gangue_confronta_gangue (
    idGangueVencedora int,
    idGanguePerdedora int,
	primary key(idGangueVencedora, idGanguePerdedora),
    dataConfronto date not null default current_date,
    constraint fk_vencedora foreign key(idGangueVencedora) references gangue(idGangue) on delete restrict on update cascade
);

create table if not exists dialogo (
    idDialogo serial primary key,
    idInstanciaNPCFalante int not null,
    descricao varchar(1000) not null,
    constraint fk_instancia_npc foreign key(idInstanciaNPCFalante) references instancia_npc(idInstanciaNPC) on delete restrict on update cascade
);

create table if not exists linha_de_fala (
    idLinhaDeFala serial primary key,
    idDialogo int not null,
    texto varchar(100) not null,
    constraint fk_dialogo foreign key(idDialogo) references dialogo(idDialogo) on delete restrict on update cascade
);

create table if not exists jogador_cumpre_missao (
	idJogador int,
	idMissao int,
	dataMissao date not null,
	retornoTotalXP int not null,
	retornoTotalDinheiro int not null,
	primary key(idJogador, idMissao),
	constraint fk_jogador foreign key(idJogador) references jogador(idPersonagem) on delete restrict on update cascade
);

create table if not exists item_tipo (
	idItem int primary key,
	tipo tipo_item not null
);

create table if not exists item_consumivel (
	idItem int primary key,
	nome varchar(30) not null unique,
	descricao varchar(1000) not null,
	peso int not null check(peso between 1 and 8),
	preco decimal(3, 2) not null,
	durabilidadeMaxima int,
	qtdReparacaoStamina int not null,
	qtdReparacaovida int not null,
	constraint fk_item_tipo foreign key(idItem) references item_tipo(idItem) on delete restrict on update cascade
);

create table if not exists item_equipavel (
	idItem int primary key,
	nome varchar(30) not null unique,
	descricao varchar(1000) not null,
	peso int not null check(peso between 1 and 8),
	preco decimal(4, 2) not null,
	durabilidadeMaxima int not null,
	parteDoCorpo varchar(30) not null,
	constraint fk_item_tipo foreign key(idItem) references item_tipo(idItem) on delete restrict on update cascade
);

create table if not exists arma_fogo (
	idItem int primary key,
	nome varchar(100) not null,
	descricao varchar(2000) not null,
	peso int not null check(peso between 1 and 8),
	preco decimal(5, 3) not null,
	durabilidadeMaxima int not null,
	danoPorAtaque decimal(4, 2) not null,
	velocidadeDisparo decimal(4, 2) not null,
	velocidadeReload decimal(4, 2) not null,
	constraint fk_item_tipo foreign key(idItem) references item_tipo(idItem) on delete restrict on update cascade
);

create table if not exists arma_melee (
	idItem int primary key,
	nome varchar(100) not null,
	descricao varchar(2000) not null,
	peso int not null check(peso between 1 and 8),
	preco decimal(5, 3) not null,
	durabilidadeMaxima int not null,
	danoPorAtaque decimal(4, 2) not null,
	nivelAfiacaoMaxima int not null default 1 check(nivelAfiacaoMaxima between 1 and 10),
	constraint fk_item_tipo foreign key(idItem) references item_tipo(idItem) on delete restrict on update cascade
);

create table if not exists instancia_item (
	idInstanciaItem serial primary key,
	idItem int not null,
	idInventario int not null,
	durabilidadeAtual int not null,
	constraint fk_item foreign key(idItem) references item_tipo(idItem) on delete restrict on update cascade,
	constraint fk_inventario foreign key(idInventario) references inventario(idInventario) on delete restrict on update cascade
);

create table if not exists projetil (
	idProjetil serial primary key,
	idInstanciaItem int not null,
	colidiu boolean not null,
	velocidade int not null check(velocidade between 1 and 1000), 
	constraint fk_instancia_item foreign key(idInstanciaItem) references instancia_item(idInstanciaItem) on delete restrict on update cascade
);

alter table jogador add constraint fk_gangue foreign key(idGangue) references gangue(idGangue) on delete restrict on update cascade;

alter table instancia_npc add constraint fk_gangue foreign key(idGangue) references gangue(idGangue) on delete restrict on update cascade;