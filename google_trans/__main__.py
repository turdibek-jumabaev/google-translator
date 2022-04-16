import requests


class Translator:

    def __init__(self):
        self.url = 'https://translate.google.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def translate(self, text: str, source_lang='auto', target_lang='uz'):
        """
        Translate text from source language to target language
        :param text: text to translate
        :param source_lang: source language
        :param target_lang: target language
        :return: translated text
        """
        params = {
            'hl': 'en',
            'ie': 'UTF-8',
            'text': text,
            'langpair': f'{source_lang}|{target_lang}'
        }

        if source_lang == 'auto':
            del params['langpair']
            return requests.get(
                self.url + f"translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}", params=params, headers=self.headers).json()[0][0][0]
        else:
            return requests.get(url=self.url + f"translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}", params=params, headers=self.headers).json()[0][0][0]
