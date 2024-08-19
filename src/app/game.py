from database import DataBase
from classes import *

class Game:
    def __init__(self):
        self.db = DataBase()
        self.connection = self.db.create_connection()
        self.current_sala = None
        self.current_regiao = None
        self.current_estado = None

    def start(self):
        print("""
            
  ____          _   ____                 _   ____          _                      _   _               ____  
 |  _ \ ___  __| | |  _ \  ___  __ _  __| | |  _ \ ___  __| | ___ _ __ ___  _ __ | |_(_) ___  _ __   |___ \ 
 | |_) / _ \/ _` | | | | |/ _ \/ _` |/ _` | | |_) / _ \/ _` |/ _ \ '_ ` _ \| '_ \| __| |/ _ \| '_ \    __) |
 |  _ <  __/ (_| | | |_| |  __/ (_| | (_| | |  _ <  __/ (_| |  __/ | | | | | |_) | |_| | (_) | | | |  / __/ 
 |_| \_\___|\__,_| |____/ \___|\__,_|\__,_| |_| \_\___|\__,_|\___|_| |_| |_| .__/ \__|_|\___/|_| |_| |_____|
                                                                           |_|                              
                 
        """)
        print("Bem-vindo ao jogo Red Dead Redemption MUD!")
        while True:
            self.show_current_location()
            command = input("Escolha uma ação (ir_para, sair, sair_jogo): ").strip().lower()
            if command == "ir_para":
                self.move()
            elif command == "sair":
                self.quit_game()
            elif command == "sair_jogo":
                print("Saindo do jogo. Até mais!")
                break
            else:
                print("Comando desconhecido. Tente novamente.")

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

    def move(self):
        if self.current_sala:
            print("Você pode ir para essas salas:")
            new_sala_id = input("Digite o ID da sala para a qual deseja ir: ")
            new_sala = self.db.get_sala(int(new_sala_id))
            if new_sala:
                self.current_sala = new_sala
            else:
                print("Sala não encontrada.")
        elif self.current_regiao:
            print("Você pode ir para essas salas:")
            new_sala_id = input("Digite o ID da sala para a qual deseja ir: ")
            new_sala = self.db.get_sala(int(new_sala_id))
            if new_sala:
                self.current_sala = new_sala
                self.current_regiao = None
            else:
                print("Sala não encontrada.")
        else:
            print("Você não pode se mover porque está em um lugar desconhecido.")

    def quit_game(self):
        self.connection.close()
        print("Saindo do jogo.")

if __name__ == '__main__':
    game = Game()
    game.start()
