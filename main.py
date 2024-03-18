from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://gis.ris.gov.tw/dashboard.html?key=E04")

# 等待下拉選單元件出現
select_year_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(1)'))
)
select_year = Select(select_year_element)

select_month_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select.input-sm.mb-md:nth-of-type(2)'))
)
select_month = Select(select_month_element)

# 依次選擇97到113的年份
for year in range(97, 114):
    select_year.select_by_value(str(year))
    time.sleep(1)
    select_month.select_by_value('12')
    time.sleep(1)

# 停留幾秒後關閉瀏覽器
time.sleep(5)
driver.quit()
