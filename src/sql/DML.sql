insert into mapa
(nome)
values ('Mapa Padrão');

insert into estado
(idMapa, nome, sigla, descricao)
values
(1, 'Ambarino', 'AM', 'Ambarino é um dos cinco estados americanos em Red Dead Redemption 2. É o estado mais elevado.Lute contra os elementos e encontre as montanhas de frente na vasta e acidentada paisagem de Ambarino.Viaje pela neve, veja geleiras e gêiseres poderosos, ursos de caça que vagam pelos Grizzlies ou apreciam as águas azuis do ravino de Calumet.O estado de Ambarino está localizado na parte norte do mapa em Red Dead Redemption 2. É dividido em duas regiões: Grizzlies East e Grizzlies West.Abaixo, você encontra a lista de animais, cavalos, armas, personagens e gangues que você pode encontrar no Red Dead Redemption 2 no estado de Ambarino, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.Vida selvagem: urso marrom norte -americano (Grizzly)'),
(1, 'Lemoyne', 'LE', 'Lemoyne é um dos cinco estados americanos em Red Dead Redemption 2. Aproveite os prados exuberantes e o clima do sul do campo de Lemoyne, ou aprecie as luzes da cidade cultural de São Denis.Isso é se você passar pelo pântano agourento e Bayou NWA.O estado de Lemoyne está localizado na parte sudeste do mapa em Red Dead Redemption 2. É dividido em três regiões: Scarlett Meadows, Bayou Nwa e Bluewater Marsh.Abaixo, você encontra a lista de animais, cavalos, armas, personagens e gangues que você pode encontrar no Red Dead Redemption 2 no estado de Lemoyne, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.'),
(1, 'New Austin', 'NA', 'New Austin é um dos cinco estados americanos em Red Dead Redemption 2. Experimente o calor do deserto implacável de Austin em uma paisagem de rocha vermelha e sol alto.Somente os viajantes mais difíceis sobrevivem ao deserto árido.Então esfrie nos riachos e na terra de pastagem do lugar de Hennigan.O estado de New Austin está localizado na parte sudoeste do mapa em Red Dead Redemption 2. É dividido em quatro regiões: Cholla Springs, Gaptooth Ridge, Hennigan''s Stead e Rio Bravo.No modo de história de Red Dead Redemption 2, New Austin não pode ser acessado até o epílogo.Abaixo, você encontra a lista de animais, cavalos, armas, personagens e gangues que você pode encontrar no Red Dead Redemption 2 no estado de New Austin, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.'),
(1, 'New Hanover', 'NH', 'New Hanover é um dos cinco estados americanos em Red Dead Redemption 2. É o maior território do jogo.O estado diverso de New Hanover é uma terra de planícies e florestas extensas, perfeitas para caçadores e herbalistas.Fora das cidades e campos de petróleo da mineração, a natureza inexplorada espera.O estado de New Hanover está localizado na parte leste do mapa em Red Dead Redemption 2. É dividido em três regiões: os Heartlands, Cumberland Forest e Roanoke Ridge.Abaixo, você encontra a lista de animais, cavalos, armas, personagens e gangues que você pode encontrar no Red Dead Redemption 2 no estado de New Hanover, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.'),
(1, 'West Elizabeth', 'WE', 'West Elizabeth é um dos cinco estados americanos em Red Dead Redemption 2. Se você está caçando bisonte nas grandes planícies, apreciando as vistas de Big Valley ou enfrentando a região sinistra de árvores altas, o oeste de Elizabeth é rico e cheio deoportunidade.O estado de West Elizabeth está localizado na parte oeste do mapa em Red Dead Redemption 2. É dividido em três regiões: árvores altas, grandes planícies e Big Valley.Abaixo, você encontra a lista de animais, cavalos, armas, personagens e gangues que você pode encontrar no Red Dead Redemption 2 no estado de West Elizabeth, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.'),
(1, 'Guarma', 'GA', 'Guarma é uma ilha tropical apresentada em Red Dead Redemption 2. Este é um local especial que não faz parte do mapa principal do jogo, pois é acessado apenas durante o capítulo 5 do modo de história.Guarma é uma ilha de plantação de cana -de -açúcar e é descrita como a segunda ilha a leste de Cuba.É o lar de espécies de aves exóticas e outros animais que podem ser encontrados exclusivamente no Guarma.A ilha é dominada pelo coronel Fussar, um tirano local, mantido no poder pelas empresas de açúcar.O Guarma normalmente pode ser acessado apenas durante o capítulo 5 da história do RDR2.No entanto, é possível alcançá -lo a qualquer momento usando uma falha (consulte o vídeo abaixo).Abaixo, você encontra a lista de animais e personagens que você pode encontrar na ilha de Guarma, bem como as missões que ocorrem no território, fotos, vídeos e muito mais.');

-- AM = Ambarino, LE = Lemoyne, NA = New Austin, NH = New Hanover, WE = West Elizabeth, GA = Guarma.
insert into estado_faz_fronteira_com_estado
(siglaEstadoOrigem, siglaEstadoFronteira)
values
('AM', 'NH'),  -- Ambarino faz fronteira com New Hanover
('AM', 'WE'),  -- Ambarino faz fronteira com West Elizabeth
('NH', 'WE'),  -- New Hanover faz fronteira com West Elizabeth
('NH', 'LE'),  -- New Hanover faz fronteira com Lemoyne
('WE', 'NA'),  -- West Elizabeth faz fronteira com New Austin
('NH', 'AM'),  -- New Hanover faz fronteira com Ambarino
('WE', 'AM'),  -- West Elizabeth faz fronteira com Ambarino
('WE', 'NH'),  -- West Elizabeth faz fronteira com New Hanover
('LE', 'NH'),  -- Lemoyne faz fronteira com New Hanover
('NA', 'WE');  -- New Austin faz fronteira com West Elizabeth

insert into cidade
(nome, siglaEstado, descricao)
values
('Annesburg', 'NH', 'A vida não é fácil para os mineiros e suas famílias em Annesburg, que fornecem carvão para o rio Lannahechee há quase um século.As condições de trabalho são terríveis para pouco salário, e muitos homens perderam a vida no poço.'),
('Armadillo', 'NA', 'Armadillo é um assentamento encontrado no mundo de Red Dead Redemption e Red Dead Redemption 2. Está localizado na região de Cholla Springs do novo território de Austin.Armadillo sofria de muitos surtos de doenças.A cidade é descrita como sendo uma "cidade fantasma" e os viajantes são dissuadidos de visitar.A cidade recebeu o nome do animal do tatu, que também é encontrado no jogo.'),
('Blackwater', 'WE', 'Blackwater é um local apresentado no mundo da redenção de Red Dead e na Red Dead Redemption 2. Está localizado na região de Great Plains, no território de West Elizabeth.Blackwater e sua área circundante foram colocados em bloqueio pelos Pinkertons, seguindo o assalto executado pela gangue van der Linde que resultou em um enorme tiroteio entre as duas facções (antes dos eventos de Red Dead Redemption 2).'),
('Colter', 'AM', 'Colter é um assentamento encontrado no mundo de Red Dead Redemption 2. Está localizado na região oeste do Grizzlies, do território de Ambarino.Serve como a localização do acampamento durante o primeiro capítulo do jogo.Em breve.'),
('Lagras', 'LE', 'Um pequeno assentamento remoto nos pântanos de Bayou Nwa, LeMoyne, o povo de Lagras ao vivo auto-suficientemente suficientemente suficientes, ganhando um pouco de dinheiro aqui e ali, de pescar e agir como guias para os viajantes que desejam navegar pela região.Em breve.'),
('Mount Hagen', 'AM', 'Um dos picos mais conhecidos nos Grizzlies nevados de Ambarino, Mount Hagen Torres acima do lago Isabella, a oeste e o Beartooth Beck, a leste, que fornece o passe principal pela cordilheira ocidental e se junta ao rio Dakota mais ao sul.'),
('Rhodes', 'LE', 'Prime e adequado na superfície, tensões e corrupção correm profundamente na cidade de Rhodes, que durante anos foi pego no fogo cruzado entre os Braithwaites e os Grays, duas famílias de plantação em guerra.'),
('Saint Denis', 'LE', 'Uma porta -chave para a América do Norte com uma rota comercial que percorre toda a extensão do país, a movimentada cidade de São Denis é um caldeirão de culturas e pessoas onde homens, socialites, marinheiros, trabalhadores, mendigos e ladrões vivem lado a lado.'),
('Strawberry', 'WE', 'O Strawberry era pouco mais que uma pequena cidade de madeireira até a chegada de seu novo prefeito, um excêntrico da costa leste, que é obcecado em transformá -lo em um farol cultural para turistas ricos, para grande parte dos moradores dos habitantes locais.Em breve.'),
('Tumbleweed', 'NA', 'Tumbleweed é um assentamento encontrado no mundo de Red Dead Redemption e Red Dead Redemption 2. Está localizado na região de Gaptooth Ridge do novo território de Austin.A cidade é assediada pela gangue Del Lobos.Em breve.'),
('Valentine', 'NH', 'Uma cidade estridente e desgastada no Heartlands, os leilões de gado dos namorados atraem comerciantes, fazendeiros, cowboys, jogadores, bandidos e prostitutas de toda a parte, todos querendo ganhar dinheiro, levantar um pouco e se divertir.');

-- Assumindo IDs: 
-- Annesburg = 1, Armadillo = 2, Blackwater = 3, Colter = 4, Lagras = 5, 
-- Mount Hagen = 6, Rhodes = 7, Saint Denis = 8, Strawberry = 9, Tumbleweed = 10, Valentine = 11
insert into cidade_conecta_com_cidade
(idCidadeOrigem, idCidadeDestino)
values
(1, 11),  -- Annesburg conecta com Valentine (ambas estão em New Hanover)
(2, 10),  -- Armadillo conecta com Tumbleweed (ambas estão em New Austin)
(3, 9),   -- Blackwater conecta com Strawberry (ambas estão em West Elizabeth)
(4, 6),   -- Colter conecta com Mount Hagen (ambas estão em Ambarino)
(5, 8),   -- Lagras conecta com Saint Denis (ambas estão em Lemoyne)
(7, 8),   -- Rhodes conecta com Saint Denis (ambas estão em Lemoyne)
(9, 3),   -- Strawberry conecta com Blackwater (ambas estão em West Elizabeth)
(11, 7),  -- Valentine conecta com Rhodes (NH com LE)
(11, 1),  -- Valentine conecta com Annesburg
(10, 2),  -- Tumbleweed conecta com Armadillo
(9, 3),   -- Strawberry conecta com Blackwater
(6, 4),   -- Mount Hagen conecta com Colter
(8, 5),   -- Saint Denis conecta com Lagras
(8, 7),   -- Saint Denis conecta com Rhodes
(3, 9),   -- Blackwater conecta com Strawberry
(7, 11);  -- Rhodes conecta com Valentine

insert into estabelecimento
(nome, descricao)
values
('Salão', 'Local para beber, jogar e, às vezes, iniciar uma briga.'),
('Loja de Variedades', 'Vendendo uma ampla gama de mercadorias, incluindo alimentos, munição e roupas.'),
('Loja de Armas', 'Vendendo armas, munição e serviços de personalização de armas.'),
('Barbeiro', 'Oferece cortes de cabelo e serviços de barbear.'),
('Médico', 'Vendendo suprimentos médicos e tônicos.'),
('Hotel', 'Fornece hospedagem e um lugar para trocar de roupa ou tomar um banho.'),
('Estação de Trem', 'Serve como ponto de viagem rápida e local para enviar/receber correspondências ou pacotes.'),
('Agência dos Correios', 'Onde os jogadores podem coletar ou enviar correspondências e pagar recompensas.'),
('Banco', 'Local seguro para armazenar valores ou roubar.'),
('Açougue', 'Onde os jogadores podem vender carcaças de animais e carne.'),
('Alfaiate', 'Vendendo roupas e trajes.'),
('Estábulo', 'Local para comprar, vender ou cuidar de cavalos.'),
('Mercador de Contrabando', 'Compra e vende mercadorias roubadas, itens raros e armas especiais.'),
('Loja de Iscas', 'Vendendo iscas, anzóis e suprimentos de pesca.'),
('Acampamento', 'Local onde você pode descansar, fabricar e interagir com sua gangue.'),
('Igreja', 'Edifício religioso encontrado em algumas cidades.'),
('Cabana e Casa', 'Diversas casas e cabanas espalhadas pelo mundo, muitas vezes ligadas a missões secundárias ou segredos escondidos.'),
('Fábrica', 'Local industrial, frequentemente envolvido em missões da história.'),
('Pátio de Trem', 'Local associado ao transporte ferroviário e logística.'),
('Cidade e Vilarejo', 'Área geral com vários estabelecimentos e residentes.'),
('Delegacia do Xerife', 'Centro de aplicação da lei onde as recompensas são coletadas.'),
('Ferreiro', 'Encontrado em algumas cidades, tipicamente como parte da ambientação ou eventos da história.'),
('Plantação', 'Grande propriedade frequentemente ligada à narrativa do jogo.'),
('Acampamento de Fora da Lei', 'Acampamento de gangues rivais que pode ser atacado.'),
('Cemitério', 'Local de importância histórica ou narrativa.'),
('Cabine e Sítio', 'Residência remota, muitas vezes ligada a encontros aleatórios ou histórias secundárias.'),
('Corretor', 'Vendendo imóveis, como casas ou propriedades (relacionado ao modo história).');

insert into personagem_tipo
(tipo)
values
('JOG'),
('NPC');

insert into inventario
(totalItens, capacidade)
values
();

insert into classe
(nome),
values
();

insert into historia
(titulo, enredo)
values
();

insert into missao
(titulo, nivelDificuldade, idHistoria, idEstado)
values
();

insert into missao_depende_de_missao
(idMissaoAtual, idMissaoAnterior)
values
();

-- insert into jogador

insert into npc
(idPersonagem, nome, velocidade, vidaMax, staminaMax)
values
();

insert into instancia_npc
(idPersonagem, idGangue, idInventario, idMissao, idCidade)
values
();

insert into instancia_estabelecimento
(idEstab, idCidade, idDono)
values
();

insert into ataque
(descricao, dano)
values
();

insert into animal_tipo
(tipo)
values
('AMG'),
('HST');

--Parei aqui

-- insert into item_tipo
-- (tipo)
-- values
-- ('CON'),
-- ('EQP'),
-- ('AFG'),
-- ('AML');

-- Inserindo os itens consumíveis com nomes em português
INSERT INTO item_consumivel (idItem, nome, descricao, peso, preco, durabilidadeMaxima, qtdReparacaoStamina, qtdReparacaoVida)
VALUES 
(1, 'Feijão Assado', 'Lata de feijão assado', 2, 1.50, NULL, 25, 10),
(2, 'Pêssegos em Calda', 'Lata de pêssegos', 2, 1.75, NULL, 15, 10),
(3, 'Milho Doce em Lata', 'Lata de milho doce', 2, 1.50, NULL, 20, 10),
(4, 'Tabaco de Mascar', 'Tabaco de mascar', 1, 0.50, NULL, 15, 5),
(5, 'Cura de Saúde', 'Tônico de saúde', 1, 3.00, NULL, 0, 100),
(6, 'Cura Potente de Saúde', 'Tônico potente de saúde', 1, 4.50, NULL, 0, 150),
(7, 'Tônico Milagroso', 'Tônico milagroso', 2, 5.00, NULL, 50, 50),
(8, 'Tônico Milagroso Potente', 'Tônico potente milagroso', 2, 6.00, NULL, 75, 75),
(9, 'Bolachas de Aveia', 'Bolachas de aveia', 1, 1.00, NULL, 10, 5),
(10, 'Cigarros Premium', 'Cigarros premium', 1, 2.50, NULL, 20, 0),
(11, 'Conhaque Fino', 'Conhaque fino', 3, 7.50, NULL, 30, 30),
(12, 'Gim', 'Gim', 3, 3.00, NULL, 25, 25),
(13, 'Rum', 'Rum', 3, 4.00, NULL, 20, 20),
(14, 'Óleo de Cobra', 'Óleo de cobra', 1, 2.00, NULL, 10, 10),
(15, 'Óleo de Cobra Potente', 'Óleo de cobra potente', 1, 3.00, NULL, 15, 15),
(16, 'Uísque', 'Uísque', 3, 3.50, NULL, 25, 25);

insert into item_equipavel
(idItem, nome, descricao, peso, preco, durabilidadeMaxima, parteDoCorpo)
values
(17, 'Chapéu de Couro', 'Chapéu feito de couro durável.', 2, 10.00, 100, 'Cabeça'),
(18, 'Colete de Couro', 'Colete resistente para proteção extra.', 3, 15.00, 120, 'Tronco'),
(19, 'Botas de Couro', 'Botas robustas feitas de couro.', 4, 12.00, 100, 'Pés'),
(20, 'Luvas de Couro', 'Luvas que oferecem boa proteção e aderência.', 1, 5.00, 80, 'Mãos'),
(21, 'Jaqueta de Peles', 'Jaqueta feita de peles para proteção contra o frio.', 5, 25.00, 150, 'Tronco'),
(22, 'Cinto de Munição', 'Cinto para carregar munição extra.', 2, 8.00, 90, 'Cintura'),
(23, 'Esporas de Metal', 'Esporas que aumentam a eficácia ao montar.', 1, 7.00, 60, 'Pés');

