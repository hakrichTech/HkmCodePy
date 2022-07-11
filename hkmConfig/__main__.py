

from hkmConfig.Config import ConfigSystem

        
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
    coff = config.Config('App')
    print(coff.port)
    pass