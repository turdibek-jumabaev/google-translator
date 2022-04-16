from google_trans import Translator

translator = Translator()
print(translator.translate(text="Salom yaxshimisiz?", dest='en', src='uz'))
