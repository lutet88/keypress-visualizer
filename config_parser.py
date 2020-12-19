import json

def loadConfig():
    config = open("config.json")
    content = config.read()
    config.close()

    return json.loads(content)