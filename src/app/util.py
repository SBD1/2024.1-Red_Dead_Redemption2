import os
import platform
from time import sleep

def clear_screen():
    if platform.system() == "Windows": os.system('cls')
    else: os.system('clear')

def go_back(msg = "\nPressione Enter para continuar"):
    input(msg)

def print_prompt(file):
    with open(f"app/prompts/{file}.txt", "r") as f:
       print(f.read())