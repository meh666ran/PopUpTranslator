from bidi.algorithm import get_display
from googletrans import Translator
import arabic_reshaper
import clipboard 

clipBoard = clipboard.paste()

def detectLang(clipBoard):
    detecter = Translator()
    result = detecter.detect(clipBoard)
    return result.lang


def reshapeText(textValue):
     reshaped = arabic_reshaper.reshape(textValue)
     reshaped = get_display(reshaped, upper_is_rtl=True)
     return reshaped



def translateIt(clipBoard, lang):
    translator = Translator()

    if lang == 'en':
        translated = translator.translate(clipBoard, dest='fa')
        translated = reshapeText(translated.text)
        return translated

    else:
        translated = translator.translate(clipBoard)
        return translated.text