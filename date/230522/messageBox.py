import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showinfo("showinfo", "This is an info message")
tkinter.messagebox.showwarning("showwarning", "This is a warning")
tkinter.messagebox.showerror("showerror", "This is an error")

isYes = tkinter.messagebox.askyesno("ashyesno", "Continue?")
print(isYes)
