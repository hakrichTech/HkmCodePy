

from hkmConfig.Config import ConfigSystem
from hkmConfig.NamespaceHelpers import hkmConfig

        
if __name__ == "__main__":
    # Examples:
    #  1  coff = hkmConfig('App')
    #     print(coff.baseURL)
    # 
    # 
    #  2  config = ConfigSystem()
    #     coff = config.Config('App')
    #     print(coff.baseURL)
    config = ConfigSystem()
    coff = hkmConfig('App')
    coff = config.Config('App')
    print(coff.port)
    pass