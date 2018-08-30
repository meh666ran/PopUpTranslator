import tkinter

def mainWin(clipBoard, translatedText):
    popUpWindow = tkinter.Tk()
    popUpWindow.title("Translate! ")
    popUpWindowWidth = popUpWindow.winfo_screenwidth()
    popUpWindowHeight = popUpWindow.winfo_screenheight()
    width = 250
    height = 150
    x = (popUpWindowWidth / 2) - (width / 2)
    y = (popUpWindowHeight / 2) - (height / 2)
    originalTextView = tkinter.Label(popUpWindow, font=(None, 15), text=clipBoard + " :")
    originalTextView.pack()
    translatedTextView = tkinter.Label(popUpWindow, font=(None, 20), text=translatedText)
    translatedTextView.place(relx=0.5, rely=0.5, anchor='center')
    exitButton = tkinter.Button(popUpWindow, text='Exit', command=popUpWindow.destroy)
    exitButton.pack(side='bottom')
    popUpWindow.geometry('%dx%d+%d+%d' % (width, height, x, y))
    popUpWindow.after(5000, lambda: popUpWindow.destroy())
    popUpWindow.mainloop()