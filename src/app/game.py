from bullet import Bullet, Input, Password, YesNo
# from database import DataBase
# from util import clear_screen
from .util import *

class Game:
    def __init__(self):
        # self.db = DataBase()
        # self.connection = self.db.create_connection()
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
        
        name_input = Input(prompt="Nome: ")
        name = name_input.launch()
        username_input = Input(prompt="Username: ")
        username = username_input.launch()
        email_input = Input(prompt="Email: ")
        email = email_input.launch()
        password_input = Password(prompt="Senha: ")
        password = password_input.launch()


        clear_screen()
        print("=== Confirmação de Cadastro ===\n")
        print(f"Nome: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}\n")
        
        confirm = YesNo(prompt="Confirma? ")
        if confirm.launch():
            send_email(email, generate_token(8), name)
            print(f"\nCódigo de confirmação enviado para {email}. Confira sua caixa de entrada!")
        else:
            print("\nCadastro cancelado.")
        go_back()

    def login(self):
        clear_screen()
        print("=== Login ===\n")
        
        username_input = Input(prompt="Username: ")
        username = username_input.launch()
        password_input = Password(prompt="Senha: ")
        password = password_input.launch()
        
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