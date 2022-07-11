

from hkmConfig.ConfigSystemInterfaces import ConfigSystemInterface
from hkmConfig.NamespaceHelpers import hkmConfig


class ConfigSystem(ConfigSystemInterface):
    def __init__(self) -> None:
        self.currentConfig = None
        
    def Config(self,config):
        self.currentConfig = hkmConfig(config)
        return self.currentConfig
    def GetCurrentConfig(self):
        return self.currentConfig

