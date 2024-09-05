

class Commands:
    def cmd(inp):
        
        if inp == 'help' or inp == 'Help':
            print("""
            Comandos Disponíveis:

            - help: Lista todos os comandos disponíveis.
            - mover [N/S/L/O]: Desloca o personagem para o Norte, Sul, Leste ou Oeste, conforme possível no mapa.
            - loja [nome]: Abre a loja da área selecionada (digite o nome da loja sem os colchetes).
            - inventario: Mostra todos os itens que você carrega consigo.
            - tomar: Permite consumir um item do inventário, como um whiskey ou cigarro, para restaurar vida.
            - [nome comida]: Após usar o comando "tomar", digite o nome do alimento que deseja consumir.
            - arsenal: Exibe as armas disponíveis no seu inventário.
            - combate: Inicia um confronto com o inimigo presente na área.
            - [nome arma]: Durante o combate, use o nome da arma que deseja utilizar para atacar o inimigo. Consulte o arsenal para ver suas opções.
            - sair: Encerra o jogo e retorna ao mundo real.

            - Não utilize acentuação nos comandos!
            """)

            return 'help'

        elif inp == 'Sair' or inp == 'sair':
            print("\nVocê tem certeza?\n")
            print('1 [Sim]')
            print('2 [Não]')

            inp = 0
            while(inp not in [1, 2]):
                inp = input('> ')

                if inp == '1':
                    print("Até a próxima jornada, parceiro. Lembre-se, o Oeste sempre estará à sua espera!\n")
                    exit()
                elif inp == '2':
                    return 'sair'
                else:
                    print('\nOpção Inválida!')

        elif inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == 'arsenal':
            return True

        elif inp == 'tomar':
            return True
        
        else:
            return False
