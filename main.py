from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://gis.ris.gov.tw/dashboard.html?key=E04")

county_values = [
    "65000000", "63000000", "68000000", "66000000", "67000000",
    "64000000", "10002000", "10004000", "10005000", "10007000",
    "10008000", "10009000", "10010000", "10013000", "10014000",
    "10015000", "10016000", "10017000", "10018000", "10020000",
    "09020000", "09007000"
]

# 等待下拉選單元件出現
select_year_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(1)'))
)
select_year = Select(select_year_element)

select_month_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(2)'))
)
select_month = Select(select_month_element)

select_county_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='multiselect dropdown-toggle btn btn-default']"))
)

checkbox_elements = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//label[@class="checkbox"]/input[@type="checkbox"]'))
)

#依次選擇97到113的年份
for year in range(97, 114):
    select_year.select_by_value(str(year))
    time.sleep(0.1)
    select_month.select_by_value('12')
    time.sleep(0.1)
    select_county_element.click()
    time.sleep(0.1)
    checkbox_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//label[@class="checkbox"]/input[@type="checkbox"]'))
    )
    for checkbox in checkbox_elements:
        if checkbox.get_attribute('value') == '0':
            checkbox.click()
            time.sleep(0.1)
    for value in county_values:
        for checkbox in checkbox_elements:
            if checkbox.get_attribute('value') == value:
                checkbox.click()
                time.sleep(0.1)
                checkbox.click()

# 停留幾秒後關閉瀏覽器
time.sleep(5)
driver.quit()
