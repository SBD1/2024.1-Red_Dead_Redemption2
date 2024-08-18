from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
from googletrans import Translator

def filter(string):
    translator = Translator()
    translation = translator.translate(string, dest='pt')
    return translation.text.replace("'","''")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.gtabase.com/red-dead-redemption-2/missions/")
sleep(3)
missions = driver.find_elements(By.CLASS_NAME, "items-row")
i = 1
for mission in missions:
    # try:
    driver1.get(mission.get_attribute("href"))
    sleep(3)

    titulo = driver1.find_element(By.CLASS_NAME, "page-header").text
    historia_div = driver1.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
    historia = " ".join([p.text for p in historia_div.find_elements(By.TAG_NAME, "p")])
    objetivos_div = driver1.find_element(By.CLASS_NAME, "gta5-gold-objectives")
    objetivos = [obj.text for obj in objetivos_div.find_elements(By.TAG_NAME, "li")]
    dificuldade = randint(1, 10)
    # print(titulo, historia, objetivos)
    with open("output/missoes.txt", "a") as f:
        f.write(f"('Missão {i}', {dificuldade}, {i}, null),\n")
    with open("output/historias.txt", "a") as f:
        f.write(f"('{filter(titulo)}', '{filter(historia)}'),\n")
    with open("output/objetivos.txt", "a") as f:
        for obj in objetivos:
            retornoXp = randint(1, 1000)
            retornoDinheiro = randint(1, 1000)
            f.write(f"('{filter(obj)}', {retornoXp}, {retornoDinheiro}, {i}),\n")
    print(f"{titulo} done.")
    i += 1
# except: print("Error")
driver1.quit()
driver.quit()
