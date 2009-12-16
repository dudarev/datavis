import yaml

def get_config():
    """get config from config.yaml"""
    f = open('config.yaml')
    c = yaml.load(f)
    f.close()
    return c
