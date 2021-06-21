import yaml


class ReadConfig(object):
    def __init__(self):
        with open(r'config/GlobalGonfig.yaml', 'r', encoding='utf8') as f:
            self.__result = f.read()

    def get_test_host(self):
        return yaml.load(self.__result, Loader=yaml.FullLoader)["HOST"]["TEST"]
