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
driver.get("https://www.gtabase.com/red-dead-redemption-2/locations/")
sleep(3)
cities = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/article/div/div[3]/div[2]/div')
cities = cities.find_elements(By.XPATH, '//a[@itemprop="url" and @aria-label]')

for city in cities:
    driver1.get(city.get_attribute("href"))
    sleep(3)
    name = driver1.find_element(By.CLASS_NAME, "page-header").text.title()
    description_div = driver1.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
    description = " ".join([p.text for p in description_div.find_elements(By.TAG_NAME, "p")])
    with open("output/cidades.txt", "a") as f:
        f.write(f"('{name}', '{filter(description)}')\n")
    print(f"{name} done.")

driver1.quit()
driver.quit()