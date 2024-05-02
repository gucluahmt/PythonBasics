import yaml
# config = {'qa_environment': {'URL': "www.google.com", 'username': 'ahmet123', 'password': '1565434'}}
config_path = './../data/config_yml'
with open(config_path, 'r') as file:
    configuration = yaml.safe_load(file)
    print(configuration)