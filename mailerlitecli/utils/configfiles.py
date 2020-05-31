import yaml

def importYAML(yaml_file):
    _config_file = open(yaml_file, "r")
    _config = yaml.full_load(_config_file)

    return(_config)
