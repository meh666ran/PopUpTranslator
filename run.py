from popuptranslator import main
from  popuptranslator import gui
import argparse

# make a parser to parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="set show mode (notify/popup)")
parser.add_argument("-c", "--clipboard", help="Clip Board Mode (primary/secondary)")
args = parser.parse_args()

# store argument's value into a variable
modeArgumentValue = args.mode
clipboardArgumentValue = args.clipboard

# get primary clipbard text (just for linux)
if main.osName == "linux":
    primaryClipBoard = main.primaryClipBoard
    primaryLang = main.detectLang(primaryClipBoard)
    primaryTranslatedText = main.translateIt(primaryClipBoard, primaryLang)

# get secondary clipboard text
secondaryClipBoard = main.secondaryClipBoard
lang = main.detectLang(secondaryClipBoard)
secondaryTranslatedText = main.translateIt(secondaryClipBoard, lang)

# a function to show translation as popup
def popupTranslation(clipBoard, translatedText):
    if lang == 'fa':
        reshapedClipBoard = main.reshapeText(clipBoard)
        gui.mainWin(reshapedClipBoard, translatedText)
    elif lang == 'en':
        reshapedTranslated = main.reshapeText(translatedText)
        gui.mainWin(clipBoard, reshapedTranslated)
    else:
        gui.mainWin(clipBoard, translatedText)


if modeArgumentValue == "notify":
    if main.osName == "linux":
        if clipboardArgumentValue == "primary":
            gui.sendNotify(primaryTranslatedText)

        elif clipboardArgumentValue == "secondary":
            gui.sendNotify(secondaryTranslatedText)
    else:
        print("Sorry! This feature is Just for Gnu/Linux !")

elif modeArgumentValue == "popup":
    if clipboardArgumentValue == "primary":
        if main.osName == "linux":
            popupTranslation(primaryClipBoard, primaryTranslatedText)
        else:
            print("sorry this abillity is just for linux! install linux :))")
    elif clipboardArgumentValue == "secondary":
        popupTranslation(secondaryClipBoard, secondaryTranslatedText)
else:
    print("argument isn't defined")
        