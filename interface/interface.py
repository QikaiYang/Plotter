'''interface for user'''
import tkinter as tk
from functools import partial


class Application(tk.Frame):
    '''application class'''
    def __init__(self, master=None):
        '''init'''
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def input_clear(self,textWindown):
        '''to be implement'''
        my_entry.clear()
    def create_widgets(self):
        '''create windows'''
        my_canvas = tk.Canvas(root, width = 400, height = 300)
        my_canvas.pack()
        my_entry = tk.Entry(root)
        my_canvas.create_window(200, 40, window=my_entry)
        clear_button = tk.Button(text='Clear', command=my_entry.delete(0, 100))
        my_canvas.create_window(200, 70, window=clear_button)
        #self.confirmButton = tk.Button(self)
        #self.confirmButton["text"] = "Confirm"
        #self.confirmButton["command"] = self.confirm
        #self.confirmButton.pack(side="bottom")
        confirm_button = tk.Button(text='Confirm', command=partial(self.get_string, my_entry))
        my_canvas.create_window(200, 100, window=confirm_button)
        quit_button = tk.Button(text="QUIT", fg="red",
                              command=self.master.destroy)
        my_canvas.create_window(200, 130, window=quit_button)
    def get_string(self,arg):
        '''get input'''
        t_arg = arg.get()
        print(t_arg)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
