from googletrans import Translator

text = input("What do you want to translate?\n")

language = input("To what language do you want to translate it?\n").capitalize()

destination_languages = {
    'Spanish': 'es',
    'Chinese': 'zh-CN',
    'Italian': 'it',
    'Hindi': 'hi',
    'Mongolian': 'mn',
    'Russian': 'ru',
    'Ukrainian': 'uk',
    'French': 'fr',
    'Indonesian': 'id',
    'Japanese': 'ja',
    'Slovak': 'sk'
}

if language in destination_languages:
    print("ok\n")
else:
    print("I dont speak that language.\n")
    language = input("To what language do you want to translate it?\n").capitalize()
    if language in destination_languages:
        print("ok\n")
    else:
        print("I dont speak that language.\n")
        language = input("To what language do you want to translate it?\n").capitalize()

translator = Translator()

print(translator.translate(text, dest=destination_languages[language]).text)
