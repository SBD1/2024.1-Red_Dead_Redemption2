from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.gtabase.com/red-dead-redemption-2/characters")

temp = driver.find_elements(By.XPATH, "//a[contains(@href, '/red-dead-redemption-2/characters/') and @itemprop='url' and contains(@aria-label, 'Read more:')]")
elements = []
for item in temp:
    elements.append({"href": item.get_attribute("href"), "roster_name": item.find_element(By.CLASS_NAME, "roster_name").text})
for e in elements:
    driver1.get(e["href"])
    sleep(2)
    text = driver1.find_elements(By.TAG_NAME, "p")
    with open("npcs.txt", "a") as f:
        f.write(e["href"] + '\n')
        f.write(e["roster_name"] + '\n')
        for t in text: f.write(t.text + '\n')
        f.write("-" * 50 + '\n')
driver.quit()
