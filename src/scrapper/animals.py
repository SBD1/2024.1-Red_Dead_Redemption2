from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

animals = []
for i in range(1, 5):
    driver.get(f"https://www.gtabase.com/red-dead-redemption-2/animals/#sort=attr.ct77.frontend_value&sortdir=asc&page={i}")    
    driver.get(f"https://www.gtabase.com/red-dead-redemption-2/animals/#sort=attr.ct77.frontend_value&sortdir=asc&page={i}")    
    driver.refresh()
    sleep(7)
    animal_elements = driver.find_elements(By.CLASS_NAME, "product-item-info")
    for a in animal_elements:
        animals.append(a.text.strip())

with open("animals.txt", "w") as f:
    for animal in animals:
        f.write(animal + '\n')

driver.quit()
