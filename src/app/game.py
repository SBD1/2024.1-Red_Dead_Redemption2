from database import DataBase
from classes import *
from commands import Commands
import sys
import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_digitando(texto, delay=0.0001):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_digitando_devagar(texto, delay=0.01):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Game:

    def __init__(self):
        self.connection = DataBase.create_connection()
        self.player = Player(-1, ' ', -1, -1, -1, -1)
        self.valid_cmd = 0
        pass

    def start(self):

        print_digitando('''
            -:-:::---:.........................:-.......................::........................::..................:::::::::::::::.....
    ----------:.........................::.....................:::......................................:------------:::--:--::...........
    ------:-----::::.....................................:--::-:::.............................       .:----------------:.............:...
    --------==--:.........................................:-------:.........................          ..:--------------.     ..........---
    -=--===-=:.............................................---------::::.................             ..---------------:.     ..........:-
    =:.:-=---.............................................:-::----:....................-.               .---------------.     ............
    .....:---:..........................::...............-::..:---:............:::...=-               .:-----------------.     ...........
    .......:-:.........................:-:......................:-:..............::=%#*=.              ..:--------------.      ..........-
    ........::................:::.....:--:.......................::...............+@@@@=                .:--------------..      .......:--
    ...........................::-:::----:........................................%@@%==+.              .:--------------:.       .........
    ............................::------:::.......................................%@@@@@:              ..:---------------:.       ........
    ..............................:------:::::::.................................:%@@@@*=:            ...:---:-::::-:::-:.        ........
    .............................:-----::::.......................................#@@@@@+:             ......:.::.....---:::..     .......
    ............................:--:::::-:........................................+@@@@@@+        ..   .::::::::. ...::::....       ..... 
    ........-:................:::.....::::......................:-................:@@@@@%.             ..:...:...:.:.......             ..
    ......:--:..........................--.....................:--.................@@@@@-        ..                                 ..:-:.
    :....:---:..........................................-----::---.................#@@@=..                               .     ..:--:...  
    :--------:...........................................:-::::---::..............            .             .........   ..:----::....     
    ::---:::-::...........................................:---:-----=--:=:.             ..      .:..............::::------::...-==..      
    :-----:::--:::.......................................:--------=#%#*##*++=-=--=+*+=-::::...:.......::-------:..::::.:.  ..----=-.      
    -:--::::::-:.........................:..............-----:--+%@%=:             ...... .......::.......--:::::::.::..  ..::-:--=:..   .
    ::::::.:::..........................-:.............::.....:#%+.  ...:.       .:..::..   :#@%=.:-:.....  ..:.:-==-..::--=====-=+=.   ..
    ::..::::...........................--:....................@*. :+****@*.     ..----... ..=%%%*==-:....:.....-=====-:-----==+*####... .:
    ......::..................:::::..:---:....................-*+%@@@@@@=.      :**#%%##+...@@**#+---===-:::::=====+**====++**######*...--
    ........:...................--:------:.....................:#@@@@@#:.       .-=--#*+.=:%@@======-------=======+*###**###########*.--::
    .............................:::-:::::----:...................*@@%#-::.     .:.:=:-:=:+@@@#============--==--==*###+-+####+++++**.:...
    .............................::::--:::--:..................:::..-+#%@@%*=:.  .:=*+::=:*@@@@#=====--=----=-:-+==+*#*+#==*###*+++#*::...
    ............................:-:--:::::.................+=:-:.#....-...:=#@@@%%:*#:-=*.=@@@@@*=+-------==-::==+=-:::++=:=+####+***.:...
    ...........................:--:...:--:...............:=+++++++++***=.......:..:=%+=**-.#@@@@@@+=----===-:.:=:::-:--:=+##++#####*=.-...
    .................................:#*+..........:=*#%@@@@#+=--:.:=-..............*==+:=:+#@@@@@%+--=====::==---::::---:-=*+###*#-.:-...
    .................................-#%+..--=*%@@@%%#*+-:. ...-=+*#*=...............*+=+::#%%@@@@@*=++====-==-...:.:-:::::--.:-+=--......
    ........::....................:-=*%%#=-#@%#++=::...    .:=***=::::................+#-###%%%%@@@@+#%+===:::.:...-=++==:..::..:+:.......
    .......:::....................*%%%%%%+=-::.      ..:=*%@@@@@*+=..::................*==#%*%%@#@@@%@@%***.....::::::.....:::...:..:.....
    -::..:::::......................:.. .-....:..:=*%@%#@@@@%*=--==-:==@@#.............-++==*%%%#@%#%@%*%*........::-=+*++*++**-:.:.......
    ---:-:::::......................*. .----:.=%@%**%@@@@#-..-==+=.. .:=*::..............:**+%%@@%#%%*#=*-...-===--=-.....::-=#+-..:..::::
    :-::---:::::::.................:%-.:==#%@*+*#@@@%#=:.:--=*%%#:     .=***.............*+-.*@@@@%%%%##=::::=-:::... .... .:==-..:.....::
    .-:------::::................:*@@@@@@@@@@@@@@#=:. .--=#@@*=..-.   .:+=%%%%#%#-......--::.*@@@@@#%#%*=::::--==:...::-=:::-+:-.:.......:
    -=---::::::.................*@@@%+==**%@@#+-....:-+#@%#=-:..-=-.:-==*-.+*++*###+..:-=-:..=@#%@@%###++:.:::.::..-+=--:-====............
    ---::::.::.................*@@*:      .+@@+-**#%@@#+=-===--=+*@+=-:.-++-=====++#=---=--.#-%==-#%%#*+::....:....===-=--==::.. .:.....::
    ......::::................=@@*.         *@#%@@%#=-:-+====+*%#%%+-   .=+=======+**===--=%%=:-==::+**=:.....::..:::....:===-...*-...::::
    ........::................%@@:          -@%@@@-..-==::--%@@%-+*%:   .+-======--+###+=----+*-..:-...-....:..::.:....:...:...:+#...:::..
    .........:................-@@:          =@#=-::==-::----#%+=:=+%-==++=-=+==--==*##%#-::-......-:.::.......... ............:+#=........
    ...........................#@%-.       .#@#:.-=-..----:.+*-..  =#===-:.-#==--==***:::*-:::=:...:....:......... .........::=##:........
    .........................::-#@@%:...:=#@@#--=*@%=----:.:-.  . .:#=:.. .-#*.:=++*+*. ..:.+#+:......:...:::.............:===##*.........
    .........................:----*@@@@@@@@%+*====+%%*==---------.:-@+=%=..:**:==+#*+*:.   ...:=*:::.........::::..:::::--===*##=.........
    .................................-+**+=%@%======%%--=..  ...::..===::. .=+.-=+#**+-:.     .:..-**::........-+-:::-======+#*#-.........
    ....................................:-:%@%*==----*=-=-:.--------=+-.:----:=+++***=---:.......::..--:-:.....=..-=+=+=====#*#*:.........
    .....................................:.:%#======::-+==-::--:..:-.=**==**++:..:==+--------:.:.....=#-:=--....:::..-===-=+*+#+.....:....
    .......:...............................::@%*=--==-::-+=--::::::---=+##+######***=---------:.-:...:-::=+=:.. ..=:.:.:....::++..:..:::..
    ......:.................................#@@%+++=-:.:::=+=::--::::-=-=#*+######**=----:.----..:-.......:::--.....::-: ..........:...:::
    .....:::.............................:.*@@@%++++++++=:...:::.   .-::-#+=*#####+=--:--:.----. .:-:......-*+-:....::-:+:. .:....:-...:::
    ....:::::...........................=:+@-*@#++++++++++==-:::.   :--:-=.::-:-=**#+-..-..---:.  .---..::....:-=+:....::-==..:.  .:.. .::
    ::-:::--::....................--...-==@*.*@%#============-==..---=::=+#########*+-..:..---.    :=--:.:...:-+:--...::.:-:=- .    .:...:
    :--:::---::::::..............:-:...%+@%-..+%*-:::::-===--::=-....:+=+*#######***+-. -...--.    ..----..:..:.:.=*=:....-+---.      ....
    ---::-.:::::........:...:...:---:.:*@@=..:%###+=--=======---==-----++-*########+--:.-. .-:     . .-=---...:-:--.::......:-=:.     .-:.
    ---::::::............:----------:.:%@=. .=@++%++++==::--====-:::::::=*####*+=-:...---. .-.        .-==--:.:....::-**=...:::=-.  ....=.
    :::::::::.............:--:-------.-@@-  :#@:-%+++++++++++=--:...:::::-::--=+*#*+: .:-. .:.         .:==---.::-==::....::...---.  .....
    .....::::...............:::-:-----+@@: .-@@:.=%====++++==+=========**#######+##:.  .-. :.            :==---::-=-.... ....::..-::-:..::
    ......:::...............--:::-----*@@+..-@@:  .:=::::--=-========-:#**#####+=##-   .:..:.            ..-=-==-::--::=..  ::..:=::=--=+=
    .......................::--------.#@@%: .%%:    ..:--==--:::::-=:-:.-+****++=+:     .:.:.              .:==----:-====-....=-....-+-.-+
    .......................:....:----:%%:.-=:#@:      ..::::---:-::::::::::----:..      ....                 .-------:-===-::+#:...:-.:--:
    .............................:----%%. .#=%@+       . .....:::.:..:::.    .          .:.                  ..-=---=-::---:-.:::*=...::=#
    ...............................--=%%-  :%%@%.               .....                   :-.                    .:------::-...:.-+:....-:.:
    .................................=#%=   .#@@#.                                      :-.                      .-------:-:::...:..=#:...
    .......:.........................-:.=:   .+@@*:.                                    --.                       .:------..:......-+:..::
    ......--..........................+.:%-.   .%@%-..                                 .-.                          .-----:..:---:....-*=.
    .....:::..........................-= :%+.   .+@@+..                               .::                          . .:----:...:-:  .-=-:.
    --::::--:..........................==.:%%:    *@@#-:..                           .:-.                          .. ..----....:..:.....=
    :::::::-:...........................*#.-%@+.  .#@@%*--:...                      .::.                            .   .:---....:...  .-=
    :---::::::.:...................-:....=%-.#@@*. .+@+:....:::::..............::..  .                             ...   .:---.  .:. . ...
    ::::::--:::::................:-=:......=-:#@@@+...%@+..         ....::--.                                       .:.   .:--:........  .
    ------:-:............::.....:==-:..........#@@@@%#*%@+.         .  .--...                                      ..::..  .:--:.......  .
    -:..:---:............::::::---=-:............=%@%+:  .+@@@@*-....::.--.:.                                      ..:-.    .:--... ...   
    .....:-::..............-:----=----:::...........-:-*%%@@@%:. .-:.. .::.-.                                      ..:-..    .--..........
    .......-:..............:---=------:-:::.......:---:.*@@@@-   :+.    ..::.                                      ..--...:.. ::..........
    ......................:---===---::................::-@@@*.  -@+.   .-.-:.                                      .:--::..::.-.......... 
    ......................---=---:--.................::::@@@= .+@%:    ::--:                                       .:--:......-:......... 
    .....................:..:....:-:....................:#@%..#@@%.   .----.                                      .::--:.   .:-...........
 ██▀███  ▓█████ ▓█████▄    ▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ██▀███  ▓█████ ▓█████▄ ▓█████  ███▄ ▄███▓ ██▓███  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █    
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █    
▓██ ░▄█ ▒▒███   ░██   █▌   ░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▓██ ░▄█ ▒▒███   ░██   █▌▒███   ▓██    ▓██░▓██░ ██▓▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒   
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒   
░██▓ ▒██▒░▒████▒░▒████▓    ░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░██▓ ▒██▒░▒████▒░▒████▓ ░▒████▒▒██▒   ░██▒▒██▒ ░  ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░   
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒     ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒     ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░ ░  ░░  ░      ░░▒ ░         ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   
  ░░   ░    ░    ░ ░  ░     ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░░   ░    ░    ░ ░  ░    ░   ░      ░   ░░         ░       ▒ ░░ ░ ░ ▒     ░   ░ ░    
   ░        ░  ░   ░          ░       ░  ░     ░  ░   ░          ░        ░  ░   ░       ░  ░       ░                      ░      ░ ░           ░    
                 ░          ░                       ░                          ░                                                                     
        ''')

        print_digitando("Bem-vindo ao Velho Oeste, forasteiro!\n")

        print_digitando('Escolha uma opção:\n')

        print_digitando('1 - Criar Novo Personagem\n' +
              '2 - Carregar Personagem\n' +
              '3 - Sair\n\n\n')

        print_digitando('Digite a opção desejada: \n')

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
                break

            else:
                print('\nOpção não disponível!')

    def create_new_character(self):
        clear()
        new_name = input('Digite o nome do seu personagem: ')
        if new_name == '':
            print("Seu nome não pode estar vazio!")
            self.start()
        self.player = DataBase.get_character(self.connection, new_name)
        while(self.player.idJogador != -1):
            new_name = input('Nome já está registrado, escolha outro nome:')
            self.player = DataBase.get_character(self.connection, new_name)

        print_digitando_devagar('Qual a Gangue que o seu personagem pertence?\n')
        print_digitando_devagar('1- Gangue Van der Linde')
        print_digitando_devagar('2- ODriscoll Boys')
        print_digitando_devagar('3- The Del Lobo Gang')
        print_digitando_devagar('4- Lemoyne Raiders')

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

        print_digitando_devagar(
            f'\nBem-vindo ao jogo cowboy! Você está chegando nas montanhas Grizzlies West durante um forte inverno.\nBoa sorte na sua jornada!\n')
        input('Aperte enter para continuar!')
       
        self.gameplay()

    def load_character(self):
        clear()
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
            clear()
            self.show_player_info()

            current_area = DataBase.get_area(
                self.connection, self.player.idArea)
            area_norte = DataBase.get_area(
                self.connection, current_area.areaNorte).nome
            
            area_oeste = DataBase.get_area(
                self.connection, current_area.areaOeste).nome
            while len((area_oeste)) < 25:
                area_oeste = area_oeste + ' '

            area_leste = DataBase.get_area(
                self.connection, current_area.areaLeste).nome
            area_sul = DataBase.get_area(
                self.connection, current_area.areaSul).nome

           
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

            print(f"\nArea atual: {current_area.nome}\n")

            print(f'                            N. {area_norte}\n')
            print(f'          O. {area_oeste}' + f'*         L. {area_leste}\n')
            print(f'                            S. {area_sul}\n')
            print('\n')

            print('(Digite "ajuda" para ver todos os comandos disponíveis)')

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
                Commands.cmd(inp)
                
                if inp == 'mover n':
                    if current_area.areaNorte != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.areaNorte)
                    break

                elif inp == 'mover o':
                    if current_area.areaOeste != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.areaOeste)
                    break

                elif inp == 'mover l':
                    if current_area.areaLeste != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.areaLeste)
                    break

                elif inp == 'mover s':
                    if current_area.areaSul != 1:
                        self.player = DataBase.update_player_area(
                            self.connection, self.player.idJogador, current_area.areaSul)
                    break

                elif inp == 'combate' and valid_inim == True:
                    self.combat(Inimigo)
                    break

                elif inp == 'loja Smithfields Saloon' and valid_loja == True:
                    self.store('Smithfields Saloon')
                    break

                elif inp == 'loja Saint Denis General Store' and valid_loja == True:
                    self.store('Saint Denis General Store')
                    break

                elif inp == 'loja Gunsmith' and valid_loja == True:
                    self.store('Gunsmith')
                    break

                elif inp == 'loja Trapper' and valid_loja == True:
                    self.store('Trapper')
                    break

                elif inp == 'loja Taylor & Company General Store' and valid_loja == True:
                    self.store('Taylor & Company General Store')
                    break

                elif inp == 'loja Saint Denis Tailor' and valid_loja == True:
                    self.store('Saint Denis Tailor')
                    break

                elif inp == 'loja Wallace Station' and valid_loja == True:
                    self.store('Wallace Station')
                    break
                
                elif inp == 'loja Riggs Station' and valid_loja == True:
                    self.store('Riggs Station')
                    break
                
                elif inp == 'mapa':
                    self.mapa()

                elif inp == 'inventario':
                    self.inventario()
                    break

                elif inp == 'arsenal':
                    self.arsenal()
                    break

                elif inp == False or (inp == 'combate' and valid_inim == False)or (inp == 'loja' and valid_loja == False):
                    print('\nOpção Inválida!')

                else: 
                    print('\nOpção Inválida!')
    def mapa(self):
        print("""
                                Valentine
                                    |
                                New Hanover --- Annesburg
                                    |
Strawberry     Scarlet Meadows -- Tall Trees --- Lemoyne           Saint Denis
    |                               |                                  |
Big Valley ---------------- Cumberland Forrest  ------------  BlueWater Marsh 
    |                               |                                  |  
Black Water                         |                                  | 
                                    |                                  |
               Mount Hagen --- Grizzlies West --- Dakota River       Rhodes
                                    |
              Roanoke Ridge --- Flat Iron Lake --- Bayou Nwa
                                    |
                                Ambarino
                                    |
                              The Heartland
        """)  

    def arsenal(self):
        clear()
        inp = 0
        while(inp != 'sair'):
            arsenal = DataBase.get_spells(self.connection, self.player.idJogador)
            if not arsenal:
                print("\n Arsenal vazio ;P \n")

            print(f'\n(Digite "sair" para voltar)')

            while(inp != 'sair' and inp != 'Sair'):
                inp = input('> ')

                if inp != 'sair' and inp != 'Sair':
                    print('\nOpção Inválida!')

    def inventario(self):
        clear()
        comidas = ['Whiskey', 'Torta de Maçã', 'Carne de Caça', 'Feijão Cozido']
        inp = 0
        while(inp != 'sair'):
            DataBase.get_view_inventory(self.connection, self.player.idJogador)

            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            print(f'\nDinheiro do Jogador: {dinheiro}')

            print(f'\n(Digite "sair" para voltar)')

            while(inp != 'sair' and inp != 'Sair'):
                inp = input('> ')

                if inp == 'sair' and inp == 'Sair':
                    self.gameplay()

                elif inp == 'tomar':
                    inp = input("\n> Digite oq deseja tomar: ")
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
                print_digitando_devagar("\n Sua vida está cheia!\n")
            else:
                DataBase.deleteItem(self.connection, idInstancia)
                print_digitando_devagar("\nSua saúde melhorou!")
                input('Aperte enter para tentar de novo')
                return
        
        self.inventario()


    def store(self, Loja):
        clear()
        inp = 0
        while(inp != 'sair'):
            n_items = DataBase.get_view_store(self.connection, Loja)

            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            print_digitando_devagar(f'\nDinheiro do Jogador: {dinheiro}')

            print_digitando_devagar(f'\n(Digite o id do item para comprar-lo, ou digite "sair" para voltar)')

            while(inp != 'sair'):
                inp = input('> ')

                if inp == 'sair':
                    break

                elif inp.isnumeric() == False:
                    print_digitando_devagar('\nOpção não disponível!')

                elif DataBase.ver_item_store(self.connection, inp, Loja) == False: 
                    print_digitando_devagar('\nNão há este item nesta loja!')

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
        clear()
        arsenal = DataBase.get_spells(self.connection, self.player.idJogador)
        if not arsenal:
            print_digitando_devagar("Você não tem armas para utilizar!")
            input('Aperte enter para voltar')
            self.gameplay()

        while(self.player.pontosVida > 0 and Inimigo.pontosVida > 0):
            Habilidade = DataBase.get_habi(self.connection, Inimigo.idNPC)
            
            inp = 0
            self.valid_cmd = True
            while(self.valid_cmd == True or self.valid_cmd == 'ajuda'):            
                self.show_player_info()
                print(f"\nInimigo: {Inimigo.nome}")
                print(f"Vida Inimigo: {Inimigo.pontosVida}\n")
                inp = input('Digite o id da arma\n>')
                self.valid_cmd = Commands.cmd(inp)

                if self.valid_cmd == False:
                    print_digitando_devagar('\nOpção Inválida!')
                else: 
                    
                    arma = DataBase.get_one_spell(self.connection, self.player.idJogador, int(inp))
                    if arma == False and arma != 'ajuda':
                        print_digitando_devagar('\nVocê não possui esta arma!\n')
                    elif(arma != 'ajuda'):
                        dano_player = random.randint(0, arma.ponto)
                        Inimigo.pontosVida = Inimigo.pontosVida - dano_player
                        print(f"\n{self.player.nome} usou {arma.nome} causando {dano_player} de dano!\n")

                    
                    if Inimigo.pontosVida <= 0 or self.player.pontosVida <= 0:
                        break

                    dano_inimigo = random.randint(0, Habilidade.dano)
                    self.player.pontosVida = self.player.pontosVida - dano_inimigo
                    print(f"{Inimigo.nome} usou {Habilidade.nomeHabilidade} causando {dano_inimigo} de dano!\n")



        if Inimigo.pontosVida <= 0:
            print(f'{Inimigo.nome} derrotado!')
            print(f'Moedas ganhas: {Inimigo.moedas}')
            print(f'Itens ganhos: {Inimigo.nomeItem}')


            self.player = DataBase.set_player_pv(self.connection, self.player.idJogador, self.player.pontosVida)
            DataBase.gen_new_item_instance(self.connection, Inimigo.idItem, self.player.idJogador)
            dinheiro = DataBase.get_money(self.connection, self.player.idJogador)
            dinheiro += Inimigo.moedas
            DataBase.update_player_money(self.connection, self.player.idJogador, dinheiro)
            DataBase.reset_enemy_pv(self.connection, Inimigo.idInstInim, Inimigo.pontosVidamax, Inimigo.idArea)            
            
            input('\nAperte enter para continuar')

        if self.player.pontosVida <= 0:
            print_digitando_devagar("Você morreu!")

            input('Aperte enter para renascer em Valentine')

            self.player = DataBase.set_player_pv(self.connection, self.player.idJogador, 20)
            self.player = DataBase.update_player_area(self.connection, self.player.idJogador, 2)
            DataBase.set_enemy_pv(self.connection, Inimigo.idInstInim, Inimigo.pontosVida)  


    def show_player_info(self):
        print(f'Nome: {self.player.nome}\n' +
              f'Gangue: {DataBase.get_gangue(self.connection, self.player.idGangue)}\n' +
              f'Vida: {self.player.pontosVida}'
              )


if __name__ == '__main__':
    game = Game()
    game.start()
