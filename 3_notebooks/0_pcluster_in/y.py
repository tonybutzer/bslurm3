
import yaml

def read_config(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

config_dict = read_config('cluster.yaml')

print(config_dict)
