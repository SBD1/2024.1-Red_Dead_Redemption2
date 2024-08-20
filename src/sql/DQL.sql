-- Selecionar jogadores com seus inventarios
SELECT j.nome AS jogador,
       c.nome AS cidade,
       i.totalItens AS itens_no_inventario
FROM jogador j
JOIN cidade c ON j.idCidade = c.idCidade
JOIN inventario i ON j.idInventario = i.idInventario;

-- Listar todas as cidades e seus estados
SELECT c.nome AS cidade,
       e.nome AS estado,
       e.sigla AS sigla_estado
FROM cidade c
JOIN estado e ON c.siglaEstado = e.sigla
ORDER BY estado, cidade;

-- Listar missoes de um historia especifica
SELECT m.titulo AS missao,
       m.nivelDificuldade AS dificuldade,
       h.titulo AS historia
FROM missao m
JOIN historia h ON m.idHistoria = h.idHistoria
WHERE h.titulo = 'Nome da História';

-- Listar Animais Doceis e Seus Donos
SELECT ic.nome AS item_consumivel,
       ic.descricao AS descricao,
       ic.preco AS preco
FROM item_consumivel ic;

-- Listar animais hostis e seus ataques
SELECT ah.especie AS animal_hostil,
       ah.habitatNatural AS habitat,
       atk.descricao AS tipo_ataque,
       atk.dano AS dano
FROM animal_hostil ah
JOIN animal_hostil_possui_ataque aha ON ah.idAnimal = aha.idAnimal
JOIN ataque atk ON aha.idAtaque = atk.idAtaque;

-- Itens consumíveis disponíveis no jogo
SELECT ic.nome AS item_consumivel,
       ic.descricao AS descricao,
       ic.preco AS preco
FROM item_consumivel ic;

-- Listar Missões Cumpridas por Jogadores
SELECT j.nome AS jogador,
       m.titulo AS missao,
       jc.retornoTotalXP AS experiencia_ganha,
       jc.retornoTotalDinheiro AS dinheiro_ganho
FROM jogador_cumpre_missao jc
JOIN jogador j ON jc.idJogador = j.idPersonagem
JOIN missao m ON jc.idMissao = m.idMissao;

-- Consultar uma historia em específico
SELECT *
FROM historia
WHERE idHistoria = 1;
