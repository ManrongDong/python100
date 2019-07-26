import tkinter as tk
import tkinter.messagebox
# module 'tkinter.messagebox' has no attribute 'asktrycancel'

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
	print(tk.messagebox.asktrycancel(title='Hi',message='hahahaha'))
	print(tk.messagebox.askokcancel(title='Hi',message='hahahaha'))
	print(tk.messagebox.askyesnocancel(title='Hi',message='haha'))

tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()
