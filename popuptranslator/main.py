from bidi.algorithm import get_display
from googletrans import Translator
import arabic_reshaper
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
        result = arabic_reshaper.reshape( translated.text )
        result = get_display(result, upper_is_rtl=True)
        return result

    else:
        translated = translator.translate(clipBoard)
        return translated.text

