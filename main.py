from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
import time


url = 'https://www.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/ukus-kleshcha/'
title_main = 'Абсолют Страхование'

class Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):


        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        self.assertIn(title_main, driver.title)
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/form/div/div/div[1]/div/div/div[1]/div['
                                            '2]/div[2]/ul/li[2]/label').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/form/div/div/div[1]/div/div/div[1]/div[8]/div/span').click()
        time.sleep(2)
        ActionChains(driver).move_to_element(driver.find_element(By.ID, 'region-button')).perform()
        driver.find_element(By.XPATH,
                            '/html/body/div[6]/ul/li[2]/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/main/div[2]/form/div/div/div[1]/div/div/div[1]/div[12]/button').click()

        time.sleep(2)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/form/div/div/div[2]/div/div[1]/div[3]/span"))

            )
            print('Номер расчета:' + driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/form/div/div/div[2]/div/div[1]/div[3]/span').text)
            print('Стоимость:' + driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/main/div[2]/form/div/div/div[2]/div/div[1]/div[2]/span').text)
            time.sleep(20)
        except:
            print('Время вышло, результаты не получены')


        assert "No results found." not in driver.page_source


    def Stop(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
