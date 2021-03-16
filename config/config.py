import json

with open('config/config.json') as config_file:
    config_data = json.load(config_file)
    for key in config_data:
        path = config_data[key]
        new_path = '/'.join(path.split('\\'))
        config_data[key] = new_path

with open('config/config.json', 'w') as config_file:
    json.dump(config_data, config_file, indent=4)