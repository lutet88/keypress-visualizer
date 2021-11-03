import yaml
import os

def loadConfig(config):
    config = open(os.getcwd() + "/" + config)
    content = config.read().replace("\t", "")
    config.close()

    return yaml.load(content, Loader=yaml.SafeLoader)
