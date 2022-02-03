import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from env import EnvReader
from baseScraper import BaseScraper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import json 


class ProductScraper(BaseScraper):
    """ ProductScraper """
    
    def __init__(self):
        self


    def getContent(self):
        """ Get products list with details

            Args:
            self: Self.

            Returns:
                Json

        """
        driver = webdriver.Firefox()
        driver.get(EnvReader.getProductPageUrl(self))

        # Wait for page to be loaded
        time.sleep(random.randrange(2, 4))
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, EnvReader.getProductsByClass(self))))
        except NoSuchElementException:
            pass

        # Create dictionary to keep response with key => val
        response = {}
        # Get products
        try:
            products =  driver.find_elements_by_class_name(EnvReader.getProductsByClass(self))

            for i, product in enumerate(products):
                title = ProductScraper.characterEncoder(product.find_element_by_tag_name(EnvReader.getTitle(self)).text)
                description = ProductScraper.characterEncoder(product.find_element_by_class_name(EnvReader.getDescription(self)).text)

                # Get discount
                discount = ''
                try:
                    discount = product.find_element_by_css_selector(EnvReader.getDiscount(self)).text
                except:
                    pass

                price = ProductScraper.characterEncoder(product.find_element_by_class_name(EnvReader.getPrice(self)).text)

                # Add elements to response dict
                response[i] = ProductScraper.cleanResponse(title, description, discount, price)

        except NoSuchElementException:
            driver.close()
            raise Exception('Element not found')

        driver.close()

        return json.dumps(response, indent = 4) 