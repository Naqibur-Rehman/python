# try:
#     import tkinter
# except ImportError:    # Python 2
#     import Tkinter as tkinter
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+10+400')
mainWindow.mainloop()
