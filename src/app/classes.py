class Jogador:
    def __init__(self, idPersonagem, XP, Dinheiro, VidaAtual, StaminaMax, Habilidades):
        self.idPersonagem = idPersonagem
        self.XP = XP
        self. Dinheiro = Dinheiro
        self.VidaAtual = VidaAtual
        self.idCasa = StaminaMax
        self.estado = Habilidades


class Mapa:
    def __init__(self, idMapa, nome):
        self.idMapa = idMapa
        self.nome = nome

class Regiao:
    def __init__(self, idRegiao, idMapa, nome, descricao):
        self.idRegiao = idRegiao
        self.idMapa = idMapa
        self.nome = nome
        self.descricao = descricao

class Sala:
    def __init__(self, idSala, idRegiao, nome, descricao):
        self.idSala = idSala
        self.idRegiao = idRegiao
        self.nome = nome
        self.descricao = descricao

class Estado:
    def __init__(self, id_estado, id_mapa, nome, sigla, descricao):
        self.id_estado = id_estado
        self.id_mapa = id_mapa
        self.nome = nome
        self.sigla = sigla
        self.descricao = descricao