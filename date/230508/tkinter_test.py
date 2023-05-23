from tkinter import *

window = Tk()

window.title("my glossary")

# label = Label(window, text="This is the first label")
# label.grid(row=0, column=0, sticky=W)
#
# label2 = Label(window, text="This is the second label")
# label2.grid(row=1, column=0)
#
# button1 = Button(window, text="This text is very verrrrrrry long", bg="white", fg="Blue")
# button1.grid(row=0, column=0, sticky=W)
#
# button2 = Button(window, text="Click", bg="white", fg ="blue")
# button2.grid(row=4, column=0, sticky=W)

button3 = Button(window, text="Click", bg="white", fg ="blue")
button3.grid(row=0, column=1, sticky=W)

button4 = Button(window, text="Click", bg="white", fg ="blue")
button4.grid(row=0, column=2, sticky=W)

button5 = Button(window, text="Click", bg="white", fg ="blue")
button5.grid(row=0, column=3, sticky=W)

button6 = Button(window, text="Click", bg="white", fg ="blue")
button6.grid(row=0, column=4, sticky=W)

button7 = Button(window, text="Click", bg="white", fg ="blue")
button7.grid(row=1, column=2, columnspan=2, sticky=S)

window.mainloop()


