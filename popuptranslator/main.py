from googletrans import Translator
import clipboard 

clipBoard = clipboard.paste()

def detectlang(clipBoard):
    detecter = Translator()
    result = detecter.detect(clipBoard)
    return result.lang


def translateIt(clipBoard, lang):
    translator = Translator()

    if lang == 'en':
        translated = translator.translate(clipBoard, dest='fa')
        return translated.text
    else:
        translated = translator.translate(clipBoard)
        return translated.text

