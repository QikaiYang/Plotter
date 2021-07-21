'''New interface'''
from tkinter import *
import tkinter as tk
#from calculate.calculator_normal import CalculatorNormal
from plotter.interface_output import plotting,deriv_plotting
def delete():
    '''function for clear button'''
    my_entry.delete(0, 'end')
    x_range_entry.delete(0,'end')
    y_range_entry.delete(0,'end')
def confirm_func():
    '''function for confirm button'''
    func_string = my_entry.get()
    x_range = x_range_entry.get()
    y_range = y_range_entry.get()
    x_vec = x_range.split(",")
    y_vec = y_range.split(",")
    x_vec[0] = int(x_vec[0])
    x_vec[1] = int(x_vec[1])
    y_vec[0] = int(y_vec[0])
    y_vec[1] = int(y_vec[1])
    if x_vec[0] < x_vec[1] and y_vec[0] < y_vec[1]:
        plotting(func_string,[x_vec[0],x_vec[1]],[y_vec[0],y_vec[1]])
        deriv_plotting(func_string,[x_vec[0],x_vec[1]],[y_vec[0],y_vec[1]])
    else:
        print("Not valid range")

root = Tk()
root.title("Function plotter")
root.geometry('400x290')
tk.Label(root,
         text="Insert your function here",
         fg = "black",
         font = "Times").pack()
my_entry = Entry(root, width = 35)
my_entry.pack(pady = 10)
tk.Label(root,
         text="x-axis coordinate range on output",
         fg = "black",
         font = "Times").pack()
x_range_entry = Entry(root,width = 10)
x_range_entry.pack(pady = 5)
tk.Label(root,
         text="y-axis coordinate range on output",
         fg = "black",
         font = "Times").pack()
y_range_entry = Entry(root,width = 10)
y_range_entry.pack(pady = 5)
my_button = Button(root, text = "Clear", command = delete)
my_button.pack(pady = 10)
my_button = Button(root, text = "Confirm", command = confirm_func)
my_button.pack(pady = 10)
root.mainloop()
