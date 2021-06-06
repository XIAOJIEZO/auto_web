import json


class GetTestData(object):
    def get_json_data(self, filename,key):
        file = 'data/' + filename
        with open(file, 'r', encoding='utf8') as f:
            content = json.load(f)

        return content[key]

if __name__ == '__main__':
    s = GetTestData()
    a = s.get_json_data('AdminLogin.json', 'AdminLogin')
    print(a)