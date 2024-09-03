from bullet import Bullet, Input, Password, YesNo
from .database import DataBase
from .util import *

class Game:
    def __init__(self):
        self.connection = DataBase()
        self.loggedIn = False

    def run(self):
        print_prompt("welcome")
        while True:
            if not self.loggedIn:
                choice = self.main_menu(clear_before = False)
                if choice == "Cadastrar": self.cadastrar()
                elif choice == "Login": self.login()
                elif choice == "Sobre": self.sobre()
                elif choice == "Sair": self.sair()
            else:
                print("Game is running")
                # Implementar o restante da lógica do jogo aqui
                break

    def main_menu(self, clear_before = True):
        if clear_before: clear_screen()
        menu = Bullet(
            prompt="Escolha uma opção:",
            choices=["Login", "Cadastrar", "Sobre", "Sair"],
            bullet="→ "
        )
        return menu.launch()

    def cadastrar(self):
        clear_screen()
        print("=== Cadastro de Jogador ===\n")
        
        name = Input(prompt="Nome: ").launch()
        username = Input(prompt="Username: ").launch()
        email = Input(prompt="Email: ").launch()
        password = Password(prompt="Senha: ").launch()

        clear_screen()
        print("=== Confirmação de Cadastro ===\n")
        print(f"Nome: {name}\nUsername: {username}\nEmail: {email}\n")
        
        confirm = YesNo(prompt="Confirma? ")
        if confirm.launch():
            clear_screen()
            original_token = generate_token(8)
            send_email(email, original_token, name)
            print(f"\nCódigo de confirmação enviado para {email}. Confira sua caixa de entrada!")
            
            while True:
                token_input = Input(prompt="Token: ").launch()
                if token_input == original_token:
                    self.connection.insert_player(name, username, email, password)
                    print("\nToken confirmado.\nConta criada! Agora basta fazer login.")
                    break
                else:
                    try_again = YesNo("O token que você digitou não confere. Deseja tentar novamente?")
                    if not try_again.launch():
                        print("Operação cancelada! Conta não cadastrada")
                        break
        else:
            print("\nCadastro cancelado.")
        go_back()

    def login(self):
        clear_screen()
        print("=== Login ===\n")
        
        username = Input(prompt="Username: ").launch()
        password = Password(prompt="Senha: ").launch()
        self.connection.login(username, password)
        
        print(f"\nBem-vindo, {username}!")
        go_back()

    def sobre(self):
        clear_screen()
        print_prompt("about")
        go_back()
    
    def sair(self):
        clear_screen()
        print("Até a próxima!")
        exit()