from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import openpyxl

def scrape_panel_data(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start;height:100%;"]')))

        data_list = []

        elements = driver.find_elements(By.CSS_SELECTOR, 'div[style="display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start;height:100%;"]')
        for element in elements:
            title = element.find_element(By.CSS_SELECTOR, 'span.price-item-title').text.strip()
            price = element.find_element(By.CSS_SELECTOR, 'span.price-item-price').text.strip()
            unit = element.find_element(By.CSS_SELECTOR, 'span.price-item-per').text.strip()

            data_list.append((title, price, unit))

        driver.quit()
        return data_list

    except Exception as e:
        print("An error occurred:", str(e))
        return []

# def excellsave(data_list, file_name):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active

#     # Add headers
#     sheet.append(["Title", "Price", "Unit"])

#     for data in data_list:
#         sheet.append(data)

#     workbook.save(file_name)
#     print("Berhasil get data", file_name)

url = "https://panelharga.badanpangan.go.id/"
data_list = scrape_panel_data(url)
print(data_list)
# excellsave(data_list, "haragagaga.xlsx")
