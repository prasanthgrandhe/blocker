import tkinter as tk
from tkinter import simpledialog



ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
tk.messagebox.showinfo(title="message", message="Welcome to website blocker using python")
l=[]
link = simpledialog.askstring(title="input",prompt="Enter link of the site to unblocked or enter 0")

while(link!="0"):
    l.append(link+"\n")
    link = simpledialog.askstring(title="input",prompt="Enter link of the site to unblocked or enter 0")

file = open("Employees.txt", "r")
s = file.readlines()
file.close()

for i in l:
    if(i in s):
        s.remove(i)
file = open("Employees.txt", "w+")
file.writelines(s)
	
file.close()