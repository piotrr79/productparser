from scraper import ProductScraper
        
class Command:
    """ Command line command execution  """
    
    def __init__(self):
        pass

    def runCommand(self):
        """ Run command """
        return ProductScraper.getContent(self)

     
""" Command line call """       
x = Command()
output = x.runCommand()
print(output)