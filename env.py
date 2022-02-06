import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from decouple import config

class EnvReader():
    """ Get runtime params from env """
    
    def __init__(self):
        self

    def getDriverDefinition(self):
        """ Get driver definition 

            Returns:
                Driver string
        """
        if os.environ.get('DRIVER') is not None:   
            self.value = os.environ['DRIVER']
        else:
            self.value = config('DRIVER')
        
        return self.value

    def getProductPageUrl(self):
        """ Get product page url from env 

            Returns:
                Url string
        """
        if os.environ.get('PRODUCT_PAGE_URL') is not None:   
            self.value = os.environ['PRODUCT_PAGE_URL']
        else:
            self.value = config('PRODUCT_PAGE_URL')
        
        return self.value

    def getProductsByClass(self):
        """ Get product page url from env 

            Returns:
                Url string
        """
        if os.environ.get('PRODUCT_BOX_DEFINITIONS') is not None:   
            self.value = os.environ['PRODUCT_BOX_DEFINITIONS']
        else:
            self.value = config('PRODUCT_BOX_DEFINITIONS')
        
        return self.value

    def getTitle(self):
        """ Get product title

            Returns:
                Title string
        """
        if os.environ.get('PRODUCT_TITLE') is not None:   
            self.value = os.environ['PRODUCT_TITLE']
        else:
            self.value = config('PRODUCT_TITLE')
        
        return self.value


    def getDescription(self):
        """ Get product description

            Returns:
                Description string
        """
        if os.environ.get('PRODUCT_DESCRIPTION') is not None:   
            self.value = os.environ['PRODUCT_DESCRIPTION']
        else:
            self.value = config('PRODUCT_DESCRIPTION')
        
        return self.value


    def getPrice(self):
        """ Get product price

            Returns:
                Price string
        """
        if os.environ.get('PRODUCT_PRICE') is not None:   
            self.value = os.environ['PRODUCT_PRICE']
        else:
            self.value = config('PRODUCT_PRICE')
        
        return self.value


    def getDiscount(self):
        """ Get product discount

            Returns:
                Discount string
        """
        if os.environ.get('PRODUCT_DISCOUNT') is not None:   
            self.value = os.environ['PRODUCT_DISCOUNT']
        else:
            self.value = config('PRODUCT_DISCOUNT')
        
        return self.value
