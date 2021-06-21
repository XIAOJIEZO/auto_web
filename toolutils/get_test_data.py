import json


class GetTestData(object):
    def get_json_data(self, filename, key):
        file = 'data/' + filename
        with open(file, 'r', encoding='utf8') as f:
            content = json.load(f)

        return content[key]
