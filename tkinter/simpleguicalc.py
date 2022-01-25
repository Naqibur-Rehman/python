# import tkinter
#
# mainWindow = tkinter.Tk()
# mainWindow.title("Calculator")
# mainWindow.geometry("240x220+8+20")
# mainWindow['padx'] = 8
# mainWindow['pady'] = 8
#
# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)
# mainWindow.rowconfigure(0, weight=1)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(5, weight=1)
#
# # Textbox
# resultLabel = tkinter.Entry(mainWindow)
# resultLabel.grid(row=0, column=0, columnspan=4, sticky='news')
#
# # Buttons
# cancelButton = tkinter.Button(mainWindow, text='C', command=quit)
# cancelButton.grid(row=1, column=0, sticky='news')
# clearButton = tkinter.Button(mainWindow, text='CE')
# clearButton.grid(row=1, column=1, sticky='news')
# button7 = tkinter.Button(mainWindow, text='7')
# button7.grid(row=2, column=0, sticky='news')
# button8 = tkinter.Button(mainWindow, text='8')
# button8.grid(row=2, column=1, sticky='news')
# button9 = tkinter.Button(mainWindow, text='9')
# button9.grid(row=2, column=2, sticky='news')
# buttonAdd = tkinter.Button(mainWindow, text='+')
# buttonAdd.grid(row=2, column=3, sticky='news')
# button4 = tkinter.Button(mainWindow, text='4')
# button4.grid(row=3, column=0, sticky='news')
# button5 = tkinter.Button(mainWindow, text='5')
# button5.grid(row=3, column=1, sticky='news')
# button6 = tkinter.Button(mainWindow, text='6')
# button6.grid(row=3, column=2, sticky='news')
# buttonMinus = tkinter.Button(mainWindow, text='-')
# buttonMinus.grid(row=3, column=3, sticky='news')
# button1 = tkinter.Button(mainWindow, text='1')
# button1.grid(row=4, column=0, sticky='news')
# button2 = tkinter.Button(mainWindow, text='2')
# button2.grid(row=4, column=1, sticky='news')
# button3 = tkinter.Button(mainWindow, text='3')
# button3.grid(row=4, column=2, sticky='news')
# buttonMul = tkinter.Button(mainWindow, text='*')
# buttonMul.grid(row=4, column=3, sticky='news')
# button0 = tkinter.Button(mainWindow, text='0')
# button0.grid(row=5, column=0, sticky='news')
# buttonEqual = tkinter.Button(mainWindow, text='=')
# buttonEqual.grid(row=5, column=1, columnspan=2, sticky='news')
# buttonDiv = tkinter.Button(mainWindow, text='/')
# buttonDiv.grid(row=5, column=3, sticky='news')
#
# mainWindow.mainloop()

#  ***************************************** Professional code **************************
import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]
        ]
mainWindowPadding = 8
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480+20+0")
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='news')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, + result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())

mainWindow.mainloop()
