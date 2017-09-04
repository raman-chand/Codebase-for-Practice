from myBaseballYaml import YamlConfig, ymlReader, ymlWriter

filepath = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\myBaseballConfig.yaml"
data = {
    'source': 'Hello',
    'destination': 'Goodbye'
}
objYaml = YamlConfig(filepath, data)
objYaml.yamlWriter()

filepath2 = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\config.yaml"
print(ymlReader(filepath2))