from popuptranslator import main
from popuptranslator import gui

clipBoard = main.clipBoard
lang = main.detectlang(clipBoard)
translatedText = main.translateIt(clipBoard, lang)

gui.mainWin(clipBoard, translatedText)
