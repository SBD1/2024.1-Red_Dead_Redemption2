from database import DataBase
import time

class Game:
    def __init__(self):
        self.db = DataBase()
        self.connection = self.db.create_connection()
        self.current_sala = None
        self.current_regiao = None
        self.current_estado = None

    def write_slowly(self, texto, velocidade=0.05):  # Certifique-se de que o 'self' é o primeiro argumento
        for caractere in texto:
            print(caractere, end='', flush=True)
            time.sleep(velocidade)
        print() 

    def start(self):
        print("""
            
  ____          _   ____                 _   ____          _                      _   _               ____  
 |  _ \ ___  __| | |  _ \  ___  __ _  __| | |  _ \ ___  __| | ___ _ __ ___  _ __ | |_(_) ___  _ __   |___ \ 
 | |_) / _ \/ _` | | | | |/ _ \/ _` |/ _` | | |_) / _ \/ _` |/ _ \ '_ ` _ \| '_ \| __| |/ _ \| '_ \    __) |
 |  _ <  __/ (_| | | |_| |  __/ (_| | (_| | |  _ <  __/ (_| |  __/ | | | | | |_) | |_| | (_) | | | |  / __/ 
 |_| \_\___|\__,_| |____/ \___|\__,_|\__,_| |_| \_\___|\__,_|\___|_| |_| |_| .__/ \__|_|\___/|_| |_| |_____|
                                                                           |_|                              
                 
        """)
        self.write_slowly("Bem-vindo ao jogo Red Dead Redemption MUD!")

        while True:
            command = input("Escolha uma ação (1) Jogar Campanha (2) Sair do Jogo): ").strip().lower()
            if command == '1':
                self.capitulo1()
            elif command == '2':
                print("Saindo do jogo. Até mais!")
                break
            else:
                print("Comando desconhecido. Tente novamente.")

    def search_state(self): # Chamar a função para obter todos os estados
        results = self.db.get_all_states(self.connection) 
        if results:
            for result in results:
                print(f"ID: {result[0]}, Nome: {result[1]}, Sigla: {result[2]}, Descrição: {result[3]}")
        else:
            print("Nenhum estado encontrado.")

    def show_current_location(self):
        if self.current_sala:
            print(f"Você está na sala: {self.current_sala.nome}")
            print(f"Descrição: {self.current_sala.descricao}")
        elif self.current_regiao:
            print(f"Você está na região: {self.current_regiao.nome}")
            print(f"Descrição: {self.current_regiao.descricao}")
        elif self.current_estado:
            print(f"Você está no estado: {self.current_estado.nome}")
            print(f"Descrição: {self.current_estado.descricao}")
        else:
            print("Você está em um lugar desconhecido.")

    def capitulo1(self):
            self.write_slowly("\nVocê é Arthur Morgan, um dos membros da gangue de Dutch Van der Linde, lutando para sobreviver em uma tempestade de neve feroz nas Montanhas Grizzlies. O vento corta como lâminas e a visibilidade é praticamente inexistente. Seu objetivo é encontrar abrigo e garantir a segurança do seu bando.")
            
        
 

    def quit_game(self):
        self.connection.close()
        print("Saindo do jogo.")

if __name__ == '__main__':
    game = Game()
    game.start()
