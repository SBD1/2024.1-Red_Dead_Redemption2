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

for i in range(1, 5):
    driver.get(f"https://www.gtabase.com/red-dead-redemption-2/animals/#sort=attr.ct77.frontend_value&sortdir=asc&page={i}")
    driver.refresh()
    sleep(3)
    animals = driver.find_elements(By.CLASS_NAME, "product-item-link")
    for animal in animals:
        try:
            driver1.get(animal.get_attribute("href"))
            sleep(3)
            temp = driver1.find_element(By.CLASS_NAME, "fields-container").text.split("\n")
            
            nome = driver1.find_element(By.CLASS_NAME, "page-header").text
            descricao_div = driver1.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
            descricao = " ".join([p.text for p in descricao_div.find_elements(By.TAG_NAME, "p")])
            tamanho = temp[temp.index("SIZE") + 1] 
            habitatNatural = temp[temp.index("LOCATION") + 1] 
            especie = temp[temp.index("ANIMAL SPECIES") + 1] 
            velocidade = randint(1, 10)
            vidaMax = randint(1, 100)
            staminaMax = randint(1, 100)
            with open("output/animais.txt", "a") as f:
                f.write(f"('{filter(nome)}','{filter(descricao)}','{tamanho}','{filter(habitatNatural)}','{filter(especie)}', {velocidade}, {vidaMax}, {staminaMax})\n")
            print(f"{nome} done.")
        except: print("Error")
driver1.quit()
driver.quit()
