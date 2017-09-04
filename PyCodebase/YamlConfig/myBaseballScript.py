from myBaseballYaml import YamlConfig
filepath = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\myBaseballConfig.yaml"
data = {
    'source': 'Hello',
    'destination': 'Goodbye'
}
objYaml = YamlConfig(filepath, data)
objYaml.yamlWriter()