import requests


class Translator:

    def __init__(self):
        self.url = 'https://translate.google.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def translate(self, text, dest='en', src='auto'):
        response = requests.get(self.url.format(
            src, dest, text), headers=self.headers)
        return response.json()[0][0][0]
