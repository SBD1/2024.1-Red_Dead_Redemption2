
class Menu:
    def cmd(inp):
        
        if inp == 'ajuda' or inp == 'Ajuda':
            print("""
            Comandos Disponíveis:

            - informacao: Mostra as informações básicas do jogador, como vida e a sua gangue.
            - mapa: Mostra todo o mapa do jogo.
            - andar [N/S/L/O]: Desloca o personagem para o Norte, Sul, Leste ou Oeste, conforme possível no mapa.
            - loja [nome]: Abre a loja da área selecionada (digite o nome da loja sem os colchetes).
            - inventario: Mostra todos os itens que você carrega consigo.
            - usar: Permite consumir um item do inventário, como um whiskey ou cigarro, para restaurar vida.
            - [nome item]: Após usar o comando "usar", digite o nome do item que deseja usar.
            - arsenal: Exibe as armas disponíveis no seu inventário.
            - ataque: Inicia um confronto com o inimigo presente na área.
            - [nome arma]: Durante o ataque, use o nome da arma que deseja utilizar para atacar o inimigo. Consulte o arsenal para ver suas opções.
            - sair: Encerra o jogo e retorna ao mundo real.

            - Não utilize acentuação nos comandos!
            """)

            return 'ajuda'

        elif inp.lower() == 'sair':
            print("\nVocê tem certeza?\n")

            inp = ""
            while(inp.lower() not in ['sim', 'não', 'nao']):
                inp = input('> ').strip()  

                if inp.lower() == 'sim':
                    print("Até a próxima jornada, parceiro. Lembre-se, o Oeste sempre estará à sua espera!\n")
                    exit()
                elif inp.lower() in ['não', 'nao']:
                    print('\nContinuando ...')
                    return 'sair'
                else:
                    print('\nOpção Inválida! Digite "sim" ou "nao".')


        elif inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == 'arsenal':
            return True

        elif inp == 'usar':
            return True
        
        else:
            return False
