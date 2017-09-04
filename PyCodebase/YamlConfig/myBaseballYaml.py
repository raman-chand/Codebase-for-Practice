import yaml

class YamlConfig(object):
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.data = data

    def yamlReader(self):
        with open(self.filepath, "r") as yamlFileR:
            data = yaml.load(yamlFileR)

    def yamlWriter(self):
        with open(self.filepath, "w") as yamlFileW:
            yaml.dump(self.data, yamlFileW)