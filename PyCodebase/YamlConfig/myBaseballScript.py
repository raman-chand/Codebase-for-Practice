import yaml
from myBaseballYaml import YamlConfig, ymlReader, ymlWriter

# Class and instance creation
filepath = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\myBaseballConfig.yaml"
data = {
    'source': 'Hello World',
    'destination': 'Goodbye Life'
}
objYaml = YamlConfig()
# objYaml.yamlWriter(filepath, data)

# Function Call
filepath2 = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\config.yaml"
print(ymlReader(filepath2))

# Refactor code = moved filepath and data to yaml script
file = objYaml.yamlWriter()
print(file)

data = objYaml.yamlReader(file)
print(data)