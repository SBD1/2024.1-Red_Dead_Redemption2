from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

def filter(string):
    return string.replace("'", "''")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.gtabase.com/red-dead-redemption-2/weapons/#sort=name&sortdir=asc&attr.ct55.value=pistols%2Crevolvers%2Cshotguns%2Csniper-rifles%2Crifles%2Crepeaters&page=1")
sleep(3)
guns = driver.find_elements(By.CLASS_NAME, "product-item-link")
for gun in guns:
    try:
        driver1.get(gun.get_attribute("href"))
        sleep(3)
        temp = driver1.find_element(By.CLASS_NAME, "rdr2-stats").text.split("\n")
        nome = driver1.find_element(By.CLASS_NAME, "page-header").text
        descricao_div = driver1.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
        descricao = " ".join([p.text for p in descricao_div.find_elements(By.TAG_NAME, "p")])
        peso = randint(1, 8)
        preco = randint(100, 1000)/1000
        durabilidadeMaxima = randint(50, 100)
        danoPorAtaque = temp[temp.index("DAMAGE") + 1]
        velocidadeDisparo = temp[temp.index("FIRE RATE") + 1]
        velocidadeReload = temp[temp.index("RELOAD") + 1]
        acuracia = temp[temp.index("ACCURACY") + 1]
        
        with open("guns_new.txt", "a") as f:
            f.write(f"('{filter(nome)}','{filter(descricao)}', {peso}, {preco}, {durabilidadeMaxima}, {danoPorAtaque}, {velocidadeDisparo}, {velocidadeReload}, {acuracia})\n")
        print(f"{nome} done.")
    except: print("Error")
driver1.quit()
driver.quit()
