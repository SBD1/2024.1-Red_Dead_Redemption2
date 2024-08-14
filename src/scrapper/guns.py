from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.gtabase.com/red-dead-redemption-2/weapons/#sort=name&sortdir=asc&attr.ct55.value=pistols%2Crevolvers%2Cshotguns%2Csniper-rifles%2Crifles%2Crepeaters&page=1")    
sleep(3)
guns = []
elements = driver.find_elements(By.CLASS_NAME, "product-item-link")
for e in elements:
    href = e.get_attribute("href")
    print("Accessing", href)
    driver1.get(href)
    sleep(3)
    gun = {
        "name": driver1.find_element(By.CLASS_NAME, "page-header").text,
        "description": "".join([p.text for p in driver1.find_elements(By.TAG_NAME, "p")]),
        "statistics": {item[0]:item[1] for item in [stat.text.split("\n") for stat in driver1.find_elements(By.XPATH, "//*[starts-with(@class, 'field-entry')]")][:9]}
    }
    with open("guns_new.txt", "a") as f:
        name, description = gun["name"], gun["description"]
        f.write(f"('{name}', '{description}', ")
        for key in ['DAMAGE', 'FIRE RATE', 'ACCURACY', 'RANGE','RELOAD', 'OVERALL', 'AMMO CAPACITY', 'MANUFACTURER']:
            try:
                value = gun['statistics'][key]
                f.write(f"'{value}', ")
            except KeyError: f.write(f"'0', ")
        f.write(")\n")
    print(f"{name} done. ")

driver1.quit()
driver.quit()
