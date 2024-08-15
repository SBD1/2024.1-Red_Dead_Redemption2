from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

def filter(string):
    return string.replace("'", "''")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.gtabase.com/red-dead-redemption-2/characters/")
sleep(3)
npcs = driver.find_elements(By.CLASS_NAME, "roster_name")
for npc in npcs:
    try:
        nome = npc.text
        velocidade = 7
        vidaMax = 100
        staminaMax = 1000
        with open("npcs_new.txt", "a") as f:
            f.write(f"('{filter(nome.title())}', {velocidade}, {vidaMax}, {staminaMax})\n")
        print(f"{nome} done.")
    except: print("Error")
driver.quit()
