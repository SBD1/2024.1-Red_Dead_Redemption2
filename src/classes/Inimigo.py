class Inimigo:
    def __init__(self, idInstInim, idNPC, nome, idArea, idItem, nomeItem, moedas,pontosVidamax, pontosVida, multiplicador):
        self.idInstInim = idInstInim
        self.idNPC = idNPC
        self.nome = nome
        self.idArea = idArea
        self.idItem = idItem
        self.nomeItem = nomeItem
        self.moedas = moedas
        self.pontosVida = pontosVida
        self.pontosVidamax = pontosVidamax
        self.multiplicador = multiplicador 