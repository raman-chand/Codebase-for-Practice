import yaml

def ymlReader(filepath):
    with open(filepath, "r") as ymlFile:
        data = yaml.load(ymlFile)
    return data

def ymlWriter(filepath, data):
    with open(filepath, "w") as ymlFile:
        yaml.dump(data, ymlFile) 

class YamlConfig(object):
    # def __init__(self, filepath, data):
        # self.filepath = filepath
        # self.data = data

    def yamlReader(self, filepath):
        with open(filepath, "r") as yamlFileR:
            data = yaml.load(yamlFileR)
        return data

    def yamlWriter(self):
        filepath = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\myBaseballConfig2.yaml"
        data = {
            "Database": {
                "host": "localhost",
                "username": "rootLikeNoOther",
                "password": "anUnbreakablePassword",
                "database": "someDatabaseNameThatIllNeverShare"
            }
        }
        with open(filepath, "w") as yamlFileW:
            yaml.dump(data, yamlFileW)
        yamlFileW.close()
        return filepath