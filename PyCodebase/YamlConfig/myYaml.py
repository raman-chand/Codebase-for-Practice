#YAML Configuration:
import yaml

## Loads a .yaml
def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

## Dumps data to a .yaml
def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    filepath = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\config.yaml"
    data = yaml_loader(filepath)
    print(data)

    weaponary = data.get('weaponary')
    for item_name, item_value in weaponary.items():
        print("%s = %s" %(item_name, item_value))

    imperialLegion = data.get('imperial legion')
    for item_name, item_value in imperialLegion.items():
        print ("%s :: %s"  %(item_name, item_value))

    filepath2 = "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\config2.yaml"
    data2 = {
        "directories": {
            "source": "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\\",
            "destination": "C:\Workspace\Codebase-for-Practice\PyCodebase\YamlConfig\config\\",
            "environment": "Research"
        }
    }

    yaml_dump(filepath2, data2)