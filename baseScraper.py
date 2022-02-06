from tokenize import String
from typing import List


class BaseScraper:
    """ BaseScraper """
    
    def __init__(self):
        self

    def characterEncoder(string):
        """ Transform uft character

            Args:
            string: String.

            Returns:
                String

        """
        return string.encode('utf-8','ignore').decode("utf-8")


    def clearResponse(title: String, description: String, discount: String, price: String) -> List:
        """ Clean response from duplicates prepare dictionary for json

            Args:
            string: title
            string: description
            string: discount
            string: price

            Returns:
                dictionary

        """

        list = [title, description, discount, price]

        return {'Option title': BaseScraper.__removeDupes(list, title), 
                'Description': BaseScraper.__removeDupes(list, description), 
                'Price': BaseScraper.__removeDupes(list, price), 
                'Discount:': BaseScraper.__removeDupes(list, discount)}


    def __removeDupes(list, item):
        """ Remove duplicated occurences of subsrtring in string

            Args:
            list: list
            string: item

            Returns:
                string

        """
        for element in list:
            # Get index of duplicate
            index = item.find(element)
            # Remove substring if index is greater than 0
            # This will remove substring from string not a full string from another string
            if index > 0:
                item = item.replace(str(element), '')
        
        return item

