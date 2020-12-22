import yaml

def loadConfig(config):
    config = open(config)
    content = config.read().replace("\t", "")
    config.close()

    return yaml.load(content, Loader=yaml.SafeLoader)