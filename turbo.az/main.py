from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from time import sleep

driver = webdriver.Chrome('/Users/nijatjafarov/Downloads/chromedriver')

driver.get('https://turbo.az/autos?utf8=%E2%9C%93&q%5Bsort%5D=&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=23&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=946')

with open('turbo.csv', 'w') as turbo_csv:
    csv_writer = writer(turbo_csv)
    csv_writer.writerow(['Price', 'Year', 'Engine', 'Distance'])
    while True:
        cars = driver.find_elements(By.CLASS_NAME, 'products-i__bottom')
        for car in cars:
            price = car.find_element(By.CLASS_NAME, 'product-price').text
            year, engine, distance = car.find_element(By.CLASS_NAME, 'products-i__attributes').text.split(', ')
            
            csv_writer.writerow([price, year, engine, distance])
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
            next_button.click()
            sleep(5)
        except NoSuchElementException:
            driver.quit()
#driver.quit()