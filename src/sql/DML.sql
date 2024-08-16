INSERT INTO personagens (id_personagem, nome, papel, descricao) VALUES
(1, 'Arthur Morgan', 'Protagonista', 'Membro da gangue Van der Linde, habilidoso em combate e sobrevivência.'),
(2, 'Dutch van der Linde', 'Líder da Gangue', 'Líder carismático da gangue Van der Linde, com forte crença na liberdade.'),
(3, 'Sadie Adler', 'Fora da Lei', 'Mulher feroz e independente, se junta à gangue após uma tragédia pessoal.'),
(4, 'John Marston', 'Pistoleiro', 'Ex-fora da lei, tentando deixar o passado para trás e proteger sua família.');

INSERT INTO locais (id_local, nome, descricao, regiao) VALUES
(1, 'Valentine', 'Uma pequena cidade nas Terras Centrais com um saloon movimentado e uma loja geral.', 'Terras Centrais'),
(2, 'Saint Denis', 'Uma cidade vibrante com uma mistura de velho e novo, com mercados, mansões e favelas.', 'Lemoyne'),
(3, 'Annesburg', 'Uma cidade mineira com condições de trabalho precárias, localizada no nordeste do mapa.', 'Serra de Roanoke'),
(4, 'Fazenda Beecher', 'A fazenda de John Marston, símbolo de sua tentativa de começar uma nova vida.', 'Grandes Planícies');

INSERT INTO missoes (id_missao, titulo, objetivo, id_local) VALUES
(1, 'Fora da Lei até o Fim', 'Ajude a gangue a encontrar abrigo em uma tempestade de neve e enfrentar os ODriscolls.', 1),
(2, 'A Batalha de Shady Belle', 'Derrote os Raiders de Lemoyne e tome o controle de seu esconderijo.', 2),
(3, 'Adeus, Velho Amigo', 'Confronte Micah Bell e acabe com sua traição.', 3),
(4, 'Uma Nova Jerusalém', 'Ajude John Marston a construir sua fazenda na Fazenda Beecher.', 4);

INSERT INTO itens (id_item, nome, descricao, tipo) VALUES
(1, 'Revólver Schofield', 'Um revólver poderoso e preciso, preferido por fora da lei.', 'Arma'),
(2, 'Cura de Saúde', 'Um tônico que restaura a saúde instantaneamente.', 'Consumível'),
(3, 'Barra de Ouro', 'Um item valioso que pode ser vendido por um alto preço.', 'Valioso'),
(4, 'Cavalo', 'Um fiel cavalo, essencial para viajar pelas vastas paisagens.', 'Montaria');

INSERT INTO faccoes (id_faccao, nome, descricao) VALUES
(1, 'Gangue Van der Linde', 'Uma gangue de fora da lei que busca liberdade e vive à margem da sociedade.'),
(2, 'Lemoyne Raiders', 'Um grupo de ex-confederados que acredita na supremacia sulista e usa a violência para impor seus ideais.'),
(3, 'ODriscolls', 'Uma gangue rival que está em constante conflito com a Van der Linde.'),
(4, 'Exército dos Estados Unidos', 'A força militar oficial, frequentemente em conflito com os fora da lei.');

INSERT INTO animais (id_animal, nome, tipo, descricao) VALUES
(1, 'Lobo', 'Predador', 'Predador perigoso que caça em matilhas e ataca viajantes desavisados.'),
(2, 'Cervo', 'Presa', 'Animal comum nas florestas, frequentemente caçado por sua carne e couro.'),
(3, 'Urso Pardo', 'Predador', 'Um dos animais mais perigosos, capaz de matar com um único golpe.'),
(4, 'Águia', 'Ave', 'Uma ave majestosa que pode ser avistada nas montanhas, símbolo de liberdade.');

INSERT INTO veiculos (id_veiculo, nome, tipo, descricao) VALUES
(1, 'Diligência', 'Carruagem', 'Um veículo grande usado para transportar passageiros e mercadorias entre cidades.'),
(2, 'Carroça de Caça', 'Carroça', 'Uma carroça usada para transportar grandes quantidades de caça e peles.'),
(3, 'Barco a Remo', 'Barco', 'Um pequeno barco usado para atravessar rios e lagos.'),
(4, 'Trem', 'Ferrovia', 'O meio de transporte mais rápido disponível, usado para viagens de longa distância.');

INSERT INTO ataque (id_ataque, tipo, id_entidade_atacante, id_entidade_alvo, dano) VALUES
(1, 'Tiro', 1, 2, 35), 
(2, 'Facada', 3, 4, 20), 
(3, 'Explosão', 1, 2, 50), 
(4, 'Soco', 4, 1, 10);

INSERT INTO animal_hostil_possui_ataque (idAtaque, idAnimal) VALUES
(1, 1), 
(2, 2), 
(3, 3); 

INSERT INTO animal_amigavel (idAnimal, idRegiaoHabitatNatural, especie, velocidade, vidaMax, staminaMax, textura) VALUES
(1, 1, 'Cavalo', 75, 60, 70, 'Pelagem Marrom'), 
(2, 2, 'Cachorro', 60, 40, 50, 'Pelagem Preto e Branco'), 
(3, 3, 'Gato', 50, 30, 40, 'Pelagem Cinza');

INSERT INTO animal_hostil (idAnimal, idRegiaoHabitatNatural, especie, velocidade, vidaMax, staminaMax, textura) VALUES
(1, 4, 'Lobo', 65, 80, 70, 'Pelagem Cinza'), 
(2, 5, 'Urso Pardo', 50, 100, 60, 'Pelagem Marrom Escuro'), 
(3, 6, 'Jaguatirica', 80, 70, 80, 'Pelagem Manchada'); 

