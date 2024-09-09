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
states = ["ambarino", "lemoyne", "new-austin", "new-hanover", "west-elizabeth", "guarma"]
for state in states:
    driver.get(f"https://www.gtabase.com/red-dead-redemption-2/locations/{state}")
    sleep(3)
    name = driver.find_element(By.CLASS_NAME, "page-header").text.title()
    description_div = driver.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
    description = " ".join([p.text for p in description_div.find_elements(By.TAG_NAME, "p")])
    with open("output/estados.txt", "a") as f:
        f.write(f"('{name}', '{filter(description)}')\n")
    print(f"{name} done.")
driver.quit()