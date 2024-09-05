-- Tabela gangues
INSERT INTO GANGUE (nomegangue, simbologangue ) VALUES
('Van der Linde', 'VL'),
('ODriscoll Boys', 'Caveira'),
('The Del Lobo Gang', 'Chapéu Mexicano'),
('Lemoyne Raiders', 'Bandeira Confederada');

-- Tabela mapa
INSERT INTO MAPA (descricao) VALUES
('Valentine'),
('Estação de Trens de Valentine'),
('Saint Denis'),
('Strawberry'),
('Annesburg'),
('Rhodes');

-- Tabela Regiao
INSERT INTO REGIAO (idMapa, descricao, nome) VALUES
(1, 'Portão da cidade principal e movimentada', 'Entrada de Valentine'),
(2, 'Estação de trem movimentada que conecta várias cidades do Velho Oeste', 'Estação de Trens de Valentine'),
(3, 'Um saloon e hospedaria popular em Saint Denis', 'O Saloon de Saint Denis'),
(4, 'Casa de uma família local em Strawberry, situada nos arredores da cidade', 'Casa dos Cartwright'),
(5, 'Uma pequena casa nas bordas de Annesburg', 'Casa dos Gray'),
(6, 'Uma loja popular em Rhodes, conhecida por seus produtos exóticos e diversos', 'General Store de Rhodes');


-- Tabela Area
INSERT INTO AREA(idArea, idRegiao, nome, areaOeste, areaLeste, areaNorte, areaSul) VALUES
(1, 1, 'Nada', 1, 1, 1, 1),
(2, 1, 'Grizzlies West', 3, 4, 5, 6),
(3, 1, 'Mount Hagen', 1, 2, 1, 1),
(4, 1, 'Dakota River', 2, 1, 1, 1),
(5, 1, 'Cumberland Forest', 12, 11, 13, 2),
(6, 1, 'Flat Iron Lake', 9, 10, 2, 7),
(7, 1, 'Ambarino', 1, 1, 6, 8),
(8, 1, 'The Heartlands', 1, 1, 7, 1),
(9, 1, 'Roanoke Ridge', 1, 6, 1, 1),
(10, 1, 'Bayou Nwa', 6, 1, 1, 1),
(11, 1, 'Bluewater Marsh', 5, 1, 22, 23),
(12, 1, 'Big Valley', 1, 5, 20, 21),
(13, 1, 'Tall Trees', 14, 15, 16, 5),
(14, 1, 'Scarlett Meadows', 1, 13, 1, 1),
(15, 1, 'Lemoyne', 13, 1, 1, 1),
(16, 1, 'New Hanover', 17, 18, 19, 13),
(17, 1, 'Van Horn Trading Post', 1, 16, 1, 1),
(18, 1, 'Annesburg', 16, 1, 1, 1),
(19, 1, 'Valentine', 1, 1, 1, 16),
(20, 1, 'Strawberry', 1, 1, 1, 12),
(21, 1, 'Blackwater', 1, 1, 12, 1),
(22, 1, 'Saint Denis', 1, 1, 1, 11), 
(23, 1, 'Rhodes', 1, 1, 11, 1);


-- Tabela Arma
INSERT INTO ARMA (nome, efeito, ponto) VALUES
('Pistola Cattleman', 'tiro rápido e eficaz', 6),
('Faca de Caça', 'corte afiado', 5),
('Rifle de Longa Distância', 'tiro preciso a longa distância', 12),
('Pistola de Duas Mãos', 'tiro potente e preciso', 10);

-- Tabela Jogador
INSERT INTO JOGADOR (nome, idArea, pontosVida, idGangue) VALUES
('Arthur Morgan', 5, 100, 1),
('John Marston', 1, 100, 1),
('Dutch van der Linde', 2, 100, 2),
('Sadie Adler', 6, 100, 3),
('Javier Escuella', 7, 100, 4);

-- Tabela Arsenal
INSERT INTO ARSENAL (idArsenal, arma) VALUES
(1, 3),
(2, 4),
(2, 2),
(4, 2),
(5, 1);

-- Tabela LOJA
INSERT INTO LOJA(idArea, descricao) VALUES
(3, 'Smithfields Saloon'),
(3, 'Saint Denis General Store'),
(3, 'Gunsmith'),
(3, 'Trapper'),
(3, 'Taylor & Company General Store'),
(3, 'Saint Denis Tailor'),
(3, 'Wallace Station'),
(3, 'Riggs Station');

-- Tabela Item
INSERT INTO ITEM(IdLoja, nome, acao, valor, tipo, descricaoItem) VALUES
(2, 'Relógio de Bolso', 'Decora e permite verificar a hora', 25, 'DIVERSOS', 'Um elegante relógio de bolso com acabamento em prata.'),
(2, 'Cesta de Frutas', 'Alimenta e fornece energia', 15, 'DIVERSOS', 'Uma cesta cheia de frutas frescas do Velho Oeste, ideal para um lanche nutritivo.'),
(2, 'Mapa do Oeste', 'Auxilia na navegação', 30, 'DIVERSOS', 'Um detalhado mapa da região, essencial para explorar o Velho Oeste.'),
(3, 'Colar de Pérolas', 'Decorativo', 3, 'DIVERSOS', 'Um colar elegante e valioso, utilizado por damas de alta classe.'),
(3, 'Tabaco de Mascar', 'Deixa o jogador mais calmo', 10, 'DIVERSOS', 'Tabaco para mascar, usado para relaxar durante longas viagens.'),
(3, 'Garrafa de Whiskey', 'Bebida', 20, 'DIVERSOS', 'Whiskey forte, conhecido por seus efeitos intoxicantes.'),
(4, 'Whiskey', 'Bebida', 20, 'CURA', 'Whiskey destilado, ideal para curar ferimentos leves e aumentar a moral.'),
(5, 'Jornal do dia', 'Jornal para leitura', 2, 'DIVERSOS', 'Notícias frescas sobre o mundo do Velho Oeste.'),
(7, 'Guia de Armas', 'Explica ao leitor como usar armas', 50, 'ATAQUE', 'Um manual detalhado sobre o uso de armas de fogo.'),
(7, 'Guia de Sobrevivência', 'Explica ao leitor como sobreviver na selva', 70, 'DEFESA', 'Um manual sobre habilidades de sobrevivência no Oeste selvagem.'),
(7, 'Guia de Caça', 'Explica sobre a fauna selvagem', 50, 'ATAQUE', 'Um manual sobre as criaturas que habitam o Velho Oeste.'),
(6, 'Cavalo', 'Usado para se locomover', 50, 'DEFESA', 'O meio de transporte mais confiável no Velho Oeste.'),
(8, 'Pele de Lobo', 'Pode ser vendida ou usada como material', 3, 'DIVERSOS', 'Uma pele de lobo de alta qualidade.'),
(8, 'Planta Medicinal', 'Pode ser vendida ou usada como remédio', 3, 'DIVERSOS', 'Uma planta com propriedades medicinais valiosas.'),
(8, 'Raiz de Ginseng', 'Pode ser vendida ou usada como remédio', 3, 'DIVERSOS', 'Uma raiz poderosa usada para curar doenças.'),
(8, 'Garra de Urso', 'Pode ser vendida ou usada como talismã', 3, 'DIVERSOS', 'Garra retirada de um urso, considerada um amuleto de força.'),
(8, 'Ovo de Águia', 'Pode ser vendido ou usado como alimento', 3, 'DIVERSOS', 'Ovos de águia, um ingrediente raro e valioso.'),
(8, 'Chifre de Búfalo', 'Pode ser vendido ou usado como material', 3, 'DIVERSOS', 'Chifre de búfalo, usado em artesanato e medicina tradicional.'),
(1, 'Torta de Maçã', 'Traz felicidade', 5, 'CURA', 'Uma deliciosa torta de maçã caseira.'),
(1, 'Carne de Caça', 'Traz energia', 30, 'CURA', 'Carne de alta qualidade, perfeita para restaurar energia.'),
(1, 'Feijão Cozido', 'Traz energia', 10, 'CURA', 'Um prato de feijão cozido, ótimo para manter a resistência.');


-- Tabela ITEM que nao estao em lojas
INSERT INTO ITEM(nome, acao, valor, tipo, descricaoItem) VALUES
('Garrafa Quebrada', 'Pode causar cortes ou ferimentos', 0, 'LIXO', 'Uma garrafa quebrada, inútil e perigosa.'),
('Relógio de Bolso', 'Mostra a hora', 50, 'DEFESA', 'Um relógio de bolso antigo que mantém o tempo com precisão.'),
('Mapa da Região', 'Mostra a localização exata de cada cidade e área no mapa', 40, 'LOCOMOCAO', 'Indica pontos de interesse e caminhos pela região.'),
('Bandana', 'Esconde a identidade do usuário', 60, 'DEFESA', 'Uma bandana que ajuda a ocultar sua identidade durante crimes.'),
('Lanterna de Óleo', 'Remove a escuridão e ilumina o caminho', 10, 'DEFESA', 'Uma lanterna alimentada a óleo para iluminar ambientes escuros.');


-- Tabela NPC
INSERT INTO NPC(item, nome) VALUES
(5, 'Dutch van der Linde'), 
(6, 'Micah Bell'),
(7, 'John Marston'), 
(5, 'Hosea Matthews'),
(5, 'Bill Williamson'),
(5, 'Javier Escuella'),
(5, 'Arthur Morgan'), 
(1, 'Sadie Adler'),
(1, 'Charles Smith'),
(4, 'Mary-Beth Gaskill'),
(21, 'Colm ODriscoll'),
(8, 'Lobo Selvagem'),
(2, 'Caçador de Recompensas'),
(25, 'Angelo Bronte'),
(1, 'Jack Marston');


-- Tabela Instancia_NPC_Tipo
INSERT INTO INSTANCIA_NPC_TIPO(idNPC, tipo) VALUES
(1, 'Treinador'),
(2, 'Treinador'),
(3, 'Amigo'),
(4, 'Treinador'),
(5, 'Treinador'),
(6, 'Treinador'),
(7, 'Treinador'),
(8, 'Amigo'),
(9, 'Amigo'),
(10, 'Amigo'),
(11, 'Amigo'),
(12, 'Inimigo'),
(13, 'Inimigo'),
(14, 'Inimigo');

-- Tabela Falas
INSERT INTO FALAS(idNPC, idArea, momento, texto) VALUES
(1,5,1,'Bem-vindo a Valentine!'),
(9,6,2,'Caçador? Posso te mostrar alguns truques de sobrevivência...'),
(3,8,2,'Nesta região, sempre há perigos à espreita, cuidado com os predadores!'),
(7,10,2,'Para aprender novas habilidades, você precisa explorar e caçar!'),
(11,9,2,'Saia do meu caminho!'),
(2,17,2,'Hoje vou te mostrar como usar a lasso com eficácia.'),
(2,17,3,'Você já aprendeu tudo o que pode por aqui.'),
(4,18,2,'Você ainda não tem experiência suficiente para essa missão.'),
(4,18,3,'Hoje vou te mostrar como fazer uma armadilha para caçar.'),
(5,19,2,'Você ainda não tem experiência suficiente para essa missão.'),
(5,19,3,'Hoje vou te mostrar como rastrear animais com precisão.'),
(10,4,2,'Seria ótimo ter uma boa arma para caçar, talvez você encontre algo interessante em Rhodes.'),
(9,6,4,'Na região de Ambarino, há um grande perigo, procure o Arthur Morgan para derrotá-lo, ele normalmente fica em Strawberry!'),
(8,10,4,'Vejo que você precisa aprender mais sobre caçadas, mas cuidado, é um treinamento intenso!'),
(8,8,2,'Coma algo ou beba um whisky e recupere sua saúde, quanto mais você pagar, melhor será.'),
(9,8,3,'Coma algo ou beba um whisky e recupere sua saúde, quanto mais você pagar, melhor será.'),
(10,8,4,'Coma algo ou beba um whisky e recupere sua saúde, quanto mais você pagar, melhor será.'),
(13,16,2,'Eu ouvi que o caçador Pearson não ensina técnicas avançadas se você já souber rastrear, que confusão, né?! Se eu fosse você, começaria pelas aulas básicas...');

-- Tabela Falas
INSERT INTO FALAS(idNPC, idArea, momento, texto) VALUES
(1,5,1,'Bem-vindo a Valentine!'),
(7,8,2,'Caçador? Posso te mostrar alguns truques para sobreviver no deserto...'),
(8,9,2,'Nesta floresta, há sempre predadores à espreita, cuidado com os animais selvagens!'),
(5,12,2,'Se quiser aprender novas técnicas de caça, peça um conselho ao seu mentor!'),
(6,10,2,'Saia da minha frente!');

-- Tabela TREINAMENTO
INSERT INTO TREINAMENTO (NPC, nomeTreinamento, arma) VALUES
(1, 'TÁTICAS DE SOBREVIVÊNCIA', 1),
(2, 'TÉCNICAS DE CAÇA', 1),
(7, 'MANUSEIO DE ARMAS DE FOGO', 2),
(8, 'CUIDADOS COM ANIMAIS SELVAGENS', 2),
(6, 'FABRICAÇÃO DE POÇÕES E REMÉDIOS', 3),
(9, 'TÁTICAS DE ESTRATÉGIA', 4);

-- Tabela TREINADOR
INSERT INTO TREINADOR(idNPC, gangue, treinamento) VALUES
(1, 1, 1),
(2, 1, 1),
(5, 1, 2),
(6, 2, 5),
(7, 3, 3),
(8, 1, 4),
(9, 4, 6);

-- Tabela INSTANCIA_ITEM
INSERT INTO INSTANCIA_ITEM(idItem, idJogador) VALUES
(1, NULL),
(2, NULL),
(3, NULL),
(4, NULL),
(5, NULL),
(3, 1);

-- Tabela INVENTARIO
INSERT INTO INVENTARIO(idJogador, dinheiro) VALUES
(1, 2000),
(2, 2000),
(3, 2000),
(4, 2000),
(5, 200);

-- Tabela INSTANCIA_JOGADOR_TREINAMENTO
INSERT INTO INSTANCIA_JOGADOR_TREINAMENTO(idJogador, idTreinamento) VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6);

-- Tabela HABILIDADE
INSERT INTO HABILIDADE(nomeHabilidade, dano, descricao) VALUES
('Instinto de Caça', 3, 'Capacidade de rastrear e prever os movimentos de presas ou inimigos.'),
('Habilidade com Armas', 5, 'Capacidade aprimorada de manuseio e precisão com armas de fogo.'),
('Sobrevivência na Natureza', 0, 'Habilidade em adaptar-se e sobreviver em ambientes hostis.'),
('Intimidação', 7, 'Capacidade de dominar e influenciar outras pessoas através de força e persuasão.'),
('Resistência Mental', 0, 'Capacidade de manter o controle emocional e psicológico sob pressão.'),
('Comunicação com Animais', 5, 'Habilidade de interagir e entender animais selvagens.'),
('Artes de Sobrevivência', 5, 'Capacidade de realizar técnicas avançadas de combate e sobrevivência.'),
('Ataque de Lobo', 4, 'Um lobo ataca o jogador.'),
('Ambiente Hostil', 5, 'Cria um ambiente adverso e perigoso, dificultando a sobrevivência.');

-- Tabela INIMIGO
INSERT INTO INIMIGO(idNPC, idHabilidade, moedas) VALUES
(12, 8, 10),
(13, 9, 80),
(14, 4, 120);

-- Tabela INSTANCIA_INIMIGO
INSERT INTO INSTANCIA_INIMIGO(idNPC, idArea, idItem, pontosVida, pontosVidaMax, multiplicador) VALUES
(12, 6, 13, 10, 10, 1),
(13, 7, 2, 40, 40, 1),
(14, 8, 3, 400, 400, 3),
(12, 6, 13, 10, 10, 2),
(13, 7, 5, 40, 40, 2),
(14, 8, 6, 400, 400, 3),
(12, 6, 13, 10, 10, 3);

-- Tabela FERRAMENTA
INSERT INTO FERRAMENTA(idItem, forca) VALUES
(1, 1000),
(2, 0),
(3, 500),
(4, 0),
(8, 500),
(9, 500);

-- Tabela TONICO
INSERT INTO TONICO(idItem, ingrediente) VALUES
(6, 'Raiz de Ginseng'),
(6, 'Cabelo de Cougars'),
(6, 'Erva de Alcatrão'),
(6, 'Flor de Echinacea'),
(6, 'Óleo de Urso'),
(6, 'Folhas de Cardo');

-- Tabela CATALOGO
INSERT INTO CATALOGO(idItem, arma) VALUES
(9, 1),
(9, 2),
(9, 3),
(9, 4);

