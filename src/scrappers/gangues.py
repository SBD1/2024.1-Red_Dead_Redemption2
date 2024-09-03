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
driver.get("https://www.gtabase.com/red-dead-redemption-2/gangs/")
sleep(3)
gangues = driver.find_elements(By.CLASS_NAME, "items-row")

for gangue in gangues:
    driver1.get(gangue.get_attribute("href"))
    sleep(3)
    name = driver1.find_element(By.CLASS_NAME, "page-header").text.title()
    description_div = driver1.find_element(By.XPATH, "//*[contains(@class, 'article-content') and contains(@class, 'com-content-article__body')]")
    description = " ".join([p.text for p in description_div.find_elements(By.TAG_NAME, "p")])
    with open("output/gangues.txt", "a") as f:
        name = name.replace("'", "''")
        f.write(f"('{name}', '{filter(description)}')\n")
    print(f"{name} done.")

driver1.quit()
driver.quit()