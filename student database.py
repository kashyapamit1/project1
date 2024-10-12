import os
import sqlite3
import tkinter as tk
def students():
    os.system('python3 addstudents1.py')
def course():
    os.system('python3 ADDcourse.py')
def certificate():
    os.system('python3 addcertificate.py')
def employe():
    os.system('python3 addemploye.py')
def amit():
    HOME=Entry_HOME.get()
    addstudents1=Entry_addstudents1.get()
    ADDcourse=Entry_ADDcourse.get()
    addcertificate=Entry_addcertificate.get()
    addemploye=Entry_addemploye.get()
    connect=sqlite3.connect("munish.db")
    cursor=connect.cursor()
    cursor.execute('''create table if not exists class(addstudents1 text,ADDcourse text,addcertificate text,addemploye text_notnull)''')
    connect.commit()
    connect.close()
#TKINTER WINDOW
root=tk.Tk()
Label_home=tk.Label(root,text="HOME")
Label_home.grid(row=0,column=1)
Entry_HOME=tk.Entry(root)
Label_addstudents1=tk.Button(root,text="ADDSTUDENTS",command=students)
Label_addstudents1.grid(row=2,column=1)
Entry_addstudents1=tk.Entry(root)
Label_ADDcourse=tk.Button(root,text="ADDcourse",command=course)
Label_ADDcourse.grid(row=4,column=1)
Entry_ADDcourse=tk.Entry(root)
Label_addcertificate=tk.Button(root,text="ADDCERTIFICATE",command=certificate)
Label_addcertificate.grid(row=6,column=1)
Entry_addcertificate=tk.Entry(root)
Label_addemploye=tk.Button(root,text="ADDEMPLOYE",command=employe)
Label_addemploye.grid(row=8,column=1)
Entry_addemploye=tk.Entry(root)
root.mainloop()








