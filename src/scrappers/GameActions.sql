SELECT * FROM JOGADOR;

SELECT J.nome, C.nomeGangue from JOGADOR 
AS J INNER JOIN GANGUE AS C 
ON (J.idjogador = C.idgangue);


SELECT D.nomeMissao, N.nome FROM missao d 
INNER JOIN NPC N 
ON (D.NPC = N.idNPC);


create or REPLACE VIEW dados_inimigos AS
    select N.nome as "Nome Inimigo", ITM.nome as "Nome do Item", I.moedas, 
    II.pontosvida as "Pontos de Vida", II.multiplicador, H.nomehabilidade as "Nome da habilidade", H.dano, 
    H.descricao as "Descrição da Habilidade", ITM.acao as "Ação da Habilidade", 
    R.nome as "Região"  
    from npc N
    inner join inimigo I on  (N.idnpc = I.idnpc)
    inner join instancia_inimigo II on (I.idnpc = II.idnpc)
    inner join habilidade H on (I.idhabilidade = H.idhabilidade)
    inner join item ITM on (ITM.iditem = N.item)
    inner join area A on (A.idArea = II.idarea)
    inner join regiao R on (R.idregiao = A.idRegiao);
  
select * from dados_inimigos;

create view armas_coldre as
  select I.nome as "Nome Coldre", F.nome as "Armas" 
  from item I
  inner join Coldre L on(I.iditem = L.iditem)
  inner join Arma F on (L.arma = F.idarma);

select * from armas_coldre;


create OR REPLACE view inventario_jogador as
    select I.idjogador as "idjogador", ITM.nome as "Itens", ITM.valor as "Dinheiro"
    from inventario I
    inner join instancia_item II on (II.idjogador  = I.idjogador)
    inner join item ITM on (II.iditem = ITM.iditem);

select * from inventario_jogador;

create OR REPLACE view produtos_loja as
    select i.idItem as "iditem",  i.nome as "Item",  i.descricaoitem as "Descricao", i.valor as "Valor", i.idloja as "idloja"
    from loja l
    inner join item i on(i.idLoja = l.idloja);

select * from produtos_loja;


create OR REPLACE view arma_jogador as
    select l.idarsenal as "idarsenal", i.idArma as "idArma", i.nome as "nome", i.efeito as "descricao", i.ponto as "dano" 
    from arsenal l
    inner join arma i on(i.idArma = l.arma);

select * from arma_jogador;
