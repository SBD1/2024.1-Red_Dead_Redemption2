from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.gtabase.com/red-dead-redemption-2/weapons/#sort=name&sortdir=asc")    
sleep(3)
guns = []
guns_find = driver.find_elements(By.CLASS_NAME, "product-item-info ")
for g in guns_find: guns.append(g.text.strip())
with open("guns.txt", "w") as f:
    for g in guns:
        f.write(g + '\n')
driver.quit()
