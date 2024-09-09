from .database import DataBase
from .classes.Player import Player
from .menu import Menu
from .util import *
import sys
import random

class Game:
    def __init__(self):
        self.connection = DataBase.create_connection()
        self.player = Player(-1, ' ', -1, -1, -1, -1)
        self.valid_cmd = 0

    def start(self):
        prompt("title_ascii_art")
        type_effect("Bem-vindo ao Velho Oeste, forasteiro!\n")
        type_effect('Escolha uma opção:\n')
        type_effect('1 - Criar Novo Personagem\n' +
              '2 - Carregar Personagem\n' +
              '3 - Sair\n\n\n')
        type_effect('Digite a opção desejada: \n')

        inp = 0
        while(inp not in [1, 2, 3]):
            inp = input('> ')
            if inp == '1':
                self.create_new_character()
                break
            if inp == '2':
                self.load_character()
                break
            if inp == '3':
                sys.exit()
            else:
                print('\nOpção não disponível!')

    def create_new_character(self):
        clear_screen()
        new_name = input('Digite o nome do seu personagem: ')
        if new_name == '':
            print("Seu nome não pode estar vazio!")
            self.start()
        self.player = DataBase.get_character(self.connection, new_name)
        while(self.player.idJogador != -1):
            new_name = input('Nome já está registrado, escolha outro nome:')
            self.player = DataBase.get_character(self.connection, new_name)

        type_effect('Qual a Gangue que o seu personagem pertence?\n', delay=0.01)
        type_effect('1- Gangue Van der Linde', delay=0.01)
        type_effect('2- ODriscoll Boys', delay=0.01)
        type_effect('3- The Del Lobo Gang', delay=0.01)
        type_effect('4- Lemoyne Raiders', delay=0.01)

        inp = 0

        while(inp not in [1, 2, 3, 4]):
            inp = input('> ')

            if inp == '1':
                new_gangue = 1
                break

            if inp == '2':
                new_gangue = 2
                break

            if inp == '3':
                new_gangue = 3
                break

            if inp == '4':
                new_gangue = 4
                break

            else:
                print('\nOpção Inválida!')

        DataBase.create_new_character(self.connection, new_name, new_gangue)
        self.player = DataBase.get_character(self.connection, new_name)
        DataBase.create_new_inventory(self.connection, self.player.idJogador)
        DataBase.gen_new_item_instance(self.connection, 1, self.player.idJogador)

        type_effect(
            f'\nBem-vindo ao mundo selvagem do Velho Oeste, cowboy!\nVocê está prestes a embarcar em uma jornada épica pelas vastas e implacáveis terras do oeste.\nSua aventura começa nas gélidas montanhas dos Grizzlies West, onde o inverno mostra toda a sua fúria.\nO vento cortante uiva entre as árvores cobertas de neve, e cada passo seu faz ecoar o ranger do gelo sob suas botas.\nVocê está isolado, cercado por picos montanhosos que parecem tocar o céu, e o perigo espreita em cada sombra.\nSobreviver aqui não será fácil. As feras selvagens caçam pela floresta, e o frio implacável não perdoa os despreparados.\nMas, se conseguir superar esses desafios, encontrará oportunidades além da imaginação.\nPrepare-se para enfrentar os elementos, dominar a arte da caça, e escolher seus aliados com cuidado.\nSeu destino está em suas mãos. O Velho Oeste não é para os fracos!', delay=0.01)
        input('Aperte enter para continuar!')
       
        self.gameplay()

    def load_character(self):
        clear_screen()
        nome = input("Digite o nome do personagem ou sair: ")
        self.player = DataBase.get_character(self.connection, nome)
        while(self.player.idJogador == -1):
            if nome == 'sair':
                self.start()
            nome = input("Jogador não encontrado! digite outro ou sair: ")
            self.player = DataBase.get_character(self.connection, nome)
        self.gameplay()


    def gameplay(self):
        while(True):
            clear_screen()

            current_area = DataBase.get_area(
                self.connection, self.player.idArea)
            
            Loja, valid_loja = DataBase.search_store(self.connection, current_area.idArea)
            
            if valid_loja == True and current_area.idArea == 3:
                print("\nLojas na área: ")
                for i in Loja:
                    print(f"{i[2]}")

            
            Inimigo, valid_inim = DataBase.search_enemy(self.connection, current_area.idArea)
            
            texto = DataBase.getSpeech(self.connection, current_area.idArea, self.player.estado)
            if texto != None:
                print('\n')
                print(DataBase.getSpeech(self.connection, current_area.idArea, self.player.estado)) 
                print('\n')

                if self.player.estado == 1: 
                    DataBase.updateState(self.connection, self.player.idJogador, self.player.estado+1)
                else:
                    DataBase.updateState(self.connection, self.player.idJogador, self.player.estado)


            if valid_inim == True:
                print("\nInimigos na área: ")
                print(f"{Inimigo.nome}\n")

            prompt("ask_for_help", delay=0)
            print(f"\nArea atual: {current_area.nome}\n")
            

            if current_area.idArea == 17 and self.player.estado == 2:
                DataBase.addArma(self.connection, self.player.idJogador, 3, 1)
                print("\n Você aprendeu a usar a arma Pistola Cattleman, cheque o seu arsenal!\n")

            elif current_area.idArea == 18 and self.player.estado == 3:
                DataBase.addArma(self.connection, self.player.idJogador, 3, 2)
                print("\n Você aprendeu a usar a arma Faca de Caça, cheque o seu arsenal!\n")

            elif current_area.idArea == 19 and self.player.estado == 3:
                DataBase.addArma(self.connection, self.player.idJogador, 4, 3)
                print("\n Você aprendeu a usar a arma Rifle de Longa Distância, cheque o seu arsenal!\n")

            elif current_area.idArea == 15 and self.player.estado == 4:
                DataBase.addArma(self.connection, self.player.idJogador, 5, 4)
                print("\n Você aprendeu a usar a arma Pistola de Duas Mãos, cheque o seu arsenal!\n")
            

            inp = 0
            self.valid_cmd = 0
            while(self.valid_cmd == False or self.valid_cmd == 'ajuda' or valid_inim == True or  valid_loja == True):
                inp = input('> ')
                inp = inp.lower()
                Menu.cmd(inp)
                
                if inp == 'andar n':
                    if current_area.Norte != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.Norte)
                    break

                elif inp == 'andar o':
                    if current_area.Oeste != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.Oeste)
                    break

                elif inp == 'andar l':
                    if current_area.Leste != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.Leste)
                    break

                elif inp == 'andar s':
                    if current_area.Sul != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.Sul)
                    break

                elif inp == 'ataque' and valid_inim == True:
                    self.combat(Inimigo)
                    break

                elif inp == 'bar' and valid_loja == True:
                    self.store('bar')
                    break

                elif inp == 'cafeteria' and valid_loja == True:
                    self.store('cafeteria')
                    break

                elif inp == 'tabacaria' and valid_loja == True:
                    self.store('tabacaria')
                    break

                elif inp == 'farmacia' and valid_loja == True:
                    self.store('farmacia')
                    break

                elif inp == 'mercado' and valid_loja == True:
                    self.store('mercado')
                    break

                elif inp == 'estabulo' and valid_loja == True:
                    self.store('estabulo')
                    break

                elif inp == 'antiquario' and valid_loja == True:
                    self.store('antiquario')
                    break
                
                elif inp == 'bazar' and valid_loja == True:
                    self.store('bazar')
                    break
                
                elif inp == 'mapa':
                    self.mapa()
                
                elif inp == 'bussola':
                    self.bussola()

                elif inp == 'atual':
                    self.atual()

                elif inp == 'informacao':
                    self.show_player_info()

                elif inp == 'inventario':
                    self.inventario()
                    break

                elif inp == 'arsenal':
                    self.arsenal()
                    break

                elif inp == False or (inp == 'ataque' and valid_inim == False)or (inp == 'loja' and valid_loja == False):
                    print('\nOpção Inválida!')

                else: 
                    print('\nOpção Inválida!')
    def mapa(self):
        prompt("map")  

    def atual(self):
        current_area = DataBase.get_area(
        self.connection, self.player.idArea)
        print(f"\nArea atual: {current_area.nome}\n")

    def bussola(self):
        current_area = DataBase.get_area(
                self.connection, self.player.idArea)
        area_norte = DataBase.get_area(
        self.connection, current_area.Norte).nome
            
        area_oeste = DataBase.get_area(
        self.connection, current_area.Oeste).nome
        while len((area_oeste)) < 25:
            area_oeste = area_oeste + ' '

        area_leste = DataBase.get_area(
        self.connection, current_area.Leste).nome
        area_sul = DataBase.get_area(
        self.connection, current_area.Sul).nome

        print(f'                           ▲ N.\n')
        print(f'                       {area_norte}\n')
        print(f'         ◄ O. {area_oeste}' + f'*  L. {area_leste} ►\n')
        print(f'                       {area_sul}\n')
        print(f'                           ▼ S.\n')
        print('\n')

    def arsenal(self):
        clear_screen()
        inp = 0
        while(inp != 'sair'):
            arsenal = DataBase.get_spells(self.connection, self.player.idJogador)
            if not arsenal:
                print("\n Arsenal vazio! \n")

            print(f'\nDigite sair para voltar!')

            while(inp != 'sair' and inp != 'Sair'):
                inp = input('> ')

                if inp != 'sair' and inp != 'Sair':
                    print('\nOpção Inválida!')

    def inventario(self):
        clear_screen()
        inp = 0
        while(inp != 'sair'):
            DataBase.get_view_inventory(self.connection, self.player.idJogador)

            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            print(f'\nDinheiro do Jogador: {dinheiro}')

            print(f'\nDigite sair para voltar!')

            while(inp != 'sair' and inp != 'Sair'):
                inp = input('> ')

                if inp == 'sair' and inp == 'Sair':
                    self.gameplay()

                elif inp == 'usar':
                    inp = input("\n> Digite o nome do item: ")
                    self.curar(inp)

                else:
                    print('\nOpção Inválida!') 

    def curar(self, inp):
        idInstancia = DataBase.check_item_inventario(self.connection, self.player.idJogador, inp)
        if not idInstancia:
            input('Aperte enter para tentar de novo')
            return
        else:
            if not DataBase.healing(self.connection, self.player.idJogador, idInstancia):
                type_effect("\n Sua vida está cheia!\n", delay=0.01)
            else:
                DataBase.deleteItem(self.connection, idInstancia)
                type_effect("\nSua saúde melhorou!", delay=0.01)
                input('Aperte enter para tentar de novo')
                return
        
        self.inventario()


    def store(self, Loja):
        clear_screen()
        inp = 0
        while(inp != 'sair'):
            n_items = DataBase.get_view_store(self.connection, Loja)

            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            type_effect(f'\nDinheiro do Jogador: {dinheiro}', delay=0.01)

            type_effect(f'\n(Digite o id do item para comprar-lo, ou digite "sair" para voltar)', delay=0.01)

            while(inp != 'sair'):
                inp = input('> ')

                if inp == 'sair':
                    break

                elif inp.isnumeric() == False:
                    type_effect('\nOpção não disponível!', delay=0.01)

                elif DataBase.ver_item_store(self.connection, inp, Loja) == False: 
                    type_effect('\nNão há este item nesta loja!', delay=0.01)

                else:
                    val_item = DataBase.get_item_value(self.connection, inp)
                    if (dinheiro - int(val_item)) >= 0:
                        DataBase.gen_new_item_instance(self.connection, inp, self.player.idJogador)
                        dinheiro -= int(val_item)
                        DataBase.update_player_money(self.connection, self.player.idJogador, dinheiro)
                    else:
                        print("\nDinheiro insuficiente para compra ")
                    break


    def combat(self, Inimigo):
        clear_screen()
        arsenal = DataBase.get_spells(self.connection, self.player.idJogador)
        if not arsenal:
            type_effect("Você não tem armas para utilizar!", delay=0.01)
            input('Aperte enter para voltar')
            self.gameplay()

        while(self.player.pontosVida > 0 and Inimigo.pontosVida > 0):
            Habilidade = DataBase.get_habi(self.connection, Inimigo.idNPC)
            
            inp = 0
            self.valid_cmd = True
            while(self.valid_cmd == True or self.valid_cmd == 'ajuda'):            
                print(f"Nome do inimigo: {Inimigo.nome}\n")
                print(f"Vida do Inimigo: {Inimigo.pontosVida}\n")
                inp = input('Qual o id da arma que deseja usar?\n>')
                self.valid_cmd = Menu.cmd(inp)

                if self.valid_cmd == False:
                    type_effect('\nOpção Inválida!', delay=0.01)
                else: 
                    
                    arma = DataBase.get_one_spell(self.connection, self.player.idJogador, int(inp))
                    if arma == False and arma != 'ajuda':
                        type_effect('\nVocê não possui esta arma!\n', delay=0.01)
                    elif(arma != 'ajuda'):
                        dano_player = random.randint(0, arma.ponto)
                        Inimigo.pontosVida = Inimigo.pontosVida - dano_player
                        print(f"\n{self.player.nome} usou a arma {arma.nome}! Dano causado dano de:{dano_player}\n")

                    
                    if Inimigo.pontosVida <= 0 or self.player.pontosVida <= 0:
                        break

                    dano_inimigo = random.randint(0, Habilidade.dano)
                    self.player.pontosVida = self.player.pontosVida - dano_inimigo
                    print(f"{Inimigo.nome} usou a arma {Habilidade.nomeHabilidade}! Dano causado dano de: {dano_inimigo}\n")



        if Inimigo.pontosVida <= 0:
            print(f'{Inimigo.nome} foi derrotado')
            print(f'Moedas ganhas de {Inimigo.nome}: {Inimigo.moedas}')
            print(f'Itens ganhos de {Inimigo.nome}: {Inimigo.nomeItem}')


            self.player = DataBase.set_player_pv(self.connection, self.player.idJogador, self.player.pontosVida)
            DataBase.gen_new_item_instance(self.connection, Inimigo.idItem, self.player.idJogador)
            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            dinheiro += Inimigo.moedas
            DataBase.update_player_money(self.connection, self.player.idJogador, dinheiro)
            DataBase.reset_enemy_pv(self.connection, Inimigo.idInstInim, Inimigo.pontosVidamax, Inimigo.idArea)            
            
            input('\nAperte enter para continuar!')

        if self.player.pontosVida <= 0:
            type_effect("Você morreu!", delay=0.01)

            input('Aperte enter para renascer em Valentine')

            self.player = DataBase.set_player_pv(self.connection, self.player.idJogador, 20)
            self.player = DataBase.update_player_area(self.connection, self.player.idJogador, 2)
            DataBase.set_enemy_pv(self.connection, Inimigo.idInstInim, Inimigo.pontosVida)  


    def show_player_info(self):
        print(f'Nome: {self.player.nome}\n' +
              f'Gangue: {DataBase.get_gangue(self.connection, self.player.idGangue)}\n' +
              f'Simbolo da Gangue: {DataBase.get_simbolo_gangue(self.connection, self.player.idGangue)}\n' +
              f'Vida: {self.player.pontosVida}'
              )