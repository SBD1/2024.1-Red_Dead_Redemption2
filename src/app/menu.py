import os
import platform
from bullet import Bullet, Input, Password, YesNo

def clear_screen():
    if platform.system() == "Windows": os.system('cls')
    else: os.system('clear')

def main_menu():
    clear_screen()
    menu = Bullet(
        prompt="Escolha uma opção:",
        choices=["Login", "Cadastrar", "Sobre", "Sair"],
        bullet="→ ",
    )
    return menu.launch()

def cadastrar():
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
        print(f"\nUm link de confirmação foi enviado para o email {email}.")
    else:
        print("\nCadastro cancelado.")
    
    input("\nPressione Enter para continuar...")

def login():
    clear_screen()
    print("=== Login ===\n")
    
    username_input = Input(prompt="Username: ")
    username = username_input.launch()
    
    password_input = Password(prompt="Senha: ")
    password = password_input.launch()
    
    print(f"\nBem-vindo, {username}!")
    input("\nPressione Enter para continuar...")

def sobre():
    clear_screen()
    print("=== Sobre ===\n")
    print("Aplicação de Cadastro v1.0")
    print("Desenvolvido por [Seu Nome]")
    print("Este aplicativo permite que usuários se cadastrem e façam login.\n")
    input("Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == "Cadastrar":
            cadastrar()
        elif choice == "Login":
            login()
        elif choice == "Sobre":
            sobre()
        elif choice == "Sair":
            clear_screen()
            print("Até mais!")
            break
