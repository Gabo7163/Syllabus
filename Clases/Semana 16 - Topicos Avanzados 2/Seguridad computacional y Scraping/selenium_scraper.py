# Selenium Related Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains



# BS4
from bs4 import BeautifulSoup

# Other External Libraries
import json
from datetime import datetime
from copy import deepcopy
import re
import time
import random
import os

# Internal Libraries



class SelScraper:
    def __init__(self, browser='chrome', headless=True):
        self.browser = browser
        self.headless = headless
        self.driver = self._setup_driver()

    def _setup_driver(self):
        start_time = time.time()
        if self.browser == 'chrome':
            options = ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-extensions')
            options.add_argument('start-maximized')
            options.add_argument('enable-automation')
            options.add_argument('--disable-infobars')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument('--log-level=3') # Minimal logs in console (only fatal errors)
            options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
            if self.headless:
                options.add_argument('--headless')
            # Uncomment to Update ChromeDriver
            # service = ChromeService(ChromeDriverManager().install())
            service = ChromeService()
            driver = webdriver.Chrome(service=service, options=options)
        elif self.browser == 'firefox':
            options = FirefoxOptions()
            options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0')
            if self.headless:
                options.add_argument('--headless')
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Browser '{self.browser}' is not supported. Use 'chrome' or 'firefox'.")
        driver.set_page_load_timeout(360)
        end_time = time.time()
        return driver

    def get_request(self, url: str) -> None:
        self.driver.get(url)

    def wait_for_element(self, waiting_time: int, element_xpath: str) -> WebElement:
        element = WebDriverWait(self.driver, waiting_time).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        return element
    
    def find_element_by_element(self, element: WebElement, element_xpath: str) -> WebElement:
        element = element.find_element(By.XPATH, element_xpath)
        return element
    
    def find_elements_by_element(self, element: WebElement, element_xpath: str) -> WebElement:
        element = element.find_elements(By.XPATH, element_xpath)
        return element

    def make_selectable(self, selector_element: WebElement) -> WebElement:
        return Select(selector_element)

    def get_current_page_soup(self) -> BeautifulSoup:
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return soup

    def close(self):
        if self.driver:
            self.driver.quit()


def add_line_to_file(file_path, line):
    """
    Create a file if it doesn't exist and add a line to it if it exists.

    :param file_path: The name of the file.
    :param line: The line to add to the file.
    """
    folder_path = 'data'
    try:
        # Open the file in append mode; create it if it doesn't exist
        try:
            os.makedirs(folder_path, exist_ok=True)
        except Exception as e:
            print(f"An error occurred while creating the folder: {e}")
        with open(f'{folder_path}{os.sep}{file_path}', 'a') as file:
            file.write(line + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    sel_scraper = SelScraper(browser='chrome', headless=False)
    
    current_link = f'https://en.wikipedia.org/wiki/Computer_security'
    sel_scraper.get_request(current_link)


    # Get the current timestamp
    timestamp = datetime.now()
    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    filename = f'{formatted_timestamp}.txt'    
    try:
        # Find the <p> element without class or id
        p_elements = sel_scraper.driver.find_elements(By.XPATH, "//p[not(@class) and not(@id)]")
        while p_elements:
            page_title = sel_scraper.driver.find_element(By.XPATH, "//span[@class='mw-page-title-main']")
            print(page_title.text)
            p_elements = sel_scraper.driver.find_elements(By.XPATH, "//p[not(@class) and not(@id)]")
            
            for p_element in p_elements:
                try:
                    # Check if the <p> element contains a link (<a> tag)
                    links = p_element.find_elements(By.TAG_NAME, "a")
                    link = random.choice(links)
                    
                    add_line_to_file(filename, page_title.text)
                    add_line_to_file(filename, f'\t{p_element.text}')
                    print("Link clicked!")
                    # Click the first link found
                    ActionChains(sel_scraper.driver).move_to_element(link).click().perform()
                    time.sleep(random.randint(1, 2))
                    break  # Exit after clicking the first link
                except Exception as e:
                    # If no <a> tag is found in the current <p>, move to the next
                    continue
    except Exception as e:
        print("An error occurred:", e)
    sel_scraper.close()

