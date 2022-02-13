from selenium import webdriver
from env import EnvReader

class Driver:
    """ Driver """

    def __init__(self):
        self


    def getDriver(self) -> webdriver:
        """ Get driver
            Returns:
                Selenium WebDriver
        """
        driver_type = EnvReader.getDriverDefinition(self)

        if driver_type =='Firefox':
            driver = webdriver.Firefox()
        elif driver_type == 'Chrome':
            driver = webdriver.Chrome()
        elif driver_type == 'PhantomJS':
            driver = webdriver.PhantomJS()
        else:
            raise BaseException('Driver not defined')

        return driver