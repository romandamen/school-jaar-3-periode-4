from googletrans import Translator

text = input("What do you want to translate?\n")

languagetrans = input("To what language do you want to translate it?\n").capitalize()

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

if languagetrans in destination_languages:
    print("ok\n")
else:
    print("I dont speak that language.\n")
    languagetrans = input("To what language do you want to translate it?\n").capitalize()
    if languagetrans in destination_languages:
        print("ok\n")
    else:
        print("I dont speak that language.\n")
        languagetrans = input("To what language do you want to translate it?\n").capitalize()

translator = Translator()

print(translator.translate(text, dest=destination_languages[languagetrans]).text)
