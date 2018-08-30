from popuptranslator import main
from popuptranslator import gui


clipBoard = main.clipBoard
lang = main.detectLang(clipBoard)
translatedText = main.translateIt(clipBoard, lang)

if lang == 'fa':
    reshapedClipBoard = main.reshapeText(clipBoard)
    gui.mainWin(reshapedClipBoard, translatedText)
else:
    gui.mainWin(clipBoard, translatedText)
