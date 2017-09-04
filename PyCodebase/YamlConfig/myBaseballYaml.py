import yaml

def ymlReader(filepath):
    with open(filepath, "r") as ymlFile:
        data = yaml.load(ymlFile)
    return data

def ymlWriter(filepath, data):
    with open(filepath, "w") as ymlFile:
        yaml.dump(data, ymlFile) 

class YamlConfig(object):
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.data = data

    def yamlReader(self):
        with open(self.filepath, "r") as yamlFileR:
            data = yaml.load(yamlFileR)
        return data

    def yamlWriter(self):
        with open(self.filepath, "w") as yamlFileW:
            yaml.dump(self.data, yamlFileW)
