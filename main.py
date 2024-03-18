from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
url = "https://gis.ris.gov.tw/dashboard.html?key=E04"
driver.get(url)
# 等待下拉選單元件出現
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(1)'))
)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(2)'))
)
# submit_button = driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[1]/div/div/select[1]').click()
year_selection = Select(driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[1]/div/div/select[1]'))
month_selection = Select(driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[1]/div/div/select[2]'))
for year in range(97, 114):
    year_selection.select_by_value(str(year))
    month_selection.select_by_value(str(12))
    time.sleep(0.01)
    
    time.sleep(1)
    for i in range(2,24):
        if i ==2:
            area = driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[2]/div/div/div/button').click()
            time.sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[2]/div/div/div/ul/li[' + str(i) + ']/a/label/input').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[3]/div/button').click()
            time.sleep(3)
        else:
            area = driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[2]/div/div/div/button').click()
            time.sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[2]/div/div/div/ul/li[' + str(i-1) + ']/a/label/input').click()
            driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[1]/div[2]/div/div/div/ul/li[' + str(i) + ']/a/label/input').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="searchPanel"]/div/div[3]/div/button').click()
            time.sleep()

