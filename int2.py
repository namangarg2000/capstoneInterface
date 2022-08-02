from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import ttk
import csv

filepath = 'capstone.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

screen = Tk()
title = screen.title("Sin Contacto")
screen.geometry("800x650")
screen.resizable(False,False)
screen['background']='#000000'

canvas1 = Canvas(screen, bg="#EC994B", width=600,height=550)
canvas1.place(x=100,y=50)

#heading
headingFrame1 = Frame(screen,bg="#15133C",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Nava Nalanda Library", bg='#F1EEE9', fg='black', font=('Courier 15 bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

label1 = Label(screen, text="Marked", font=('Arial 30 bold'),pady=24,padx=17,bg="#EC994B",fg="#15133C")
#label3 = Label(screen, text=" ", font=('Arial', 23),pady=30,padx=15,bg="saddle brown")
label2 = Label(screen, text=Data[3][3], font=('Arial 30 bold'),pady=24,padx=25,bg="#EC994B",fg="#15133C")
label1.grid(row=3, column=1,sticky="w")
label2.grid(row=3, column=3,sticky="w")
canvas1.create_window(230,310,window=label1)
canvas1.create_window(375,310,window=label2)

F1 = Frame(screen,bg="#15133C",bd=5)
F1.place(relx=0.2,rely=0.65,relwidth=0.6,relheight=0.22)

namelabel = Label(F1, text="Name", font=('Arial 15 bold'), bg='#F1EEE9')
namelabel.grid(row=1, column=0,sticky="w")
rolllabel = Label(F1, text="Roll Number", font=('Arial 15 bold'), bg='#F1EEE9')
rolllabel.grid(row=2, column=0,sticky="w")

namelabel2 = Label(F1, text=Data[-1][2], font=('Arial 15 bold'), bg='#F1EEE9')
namelabel2.grid(row=1, column=1,sticky="w")
rolllabel2 = Label(F1, text=Data[-1][1], font=('Arial 15 bold'), bg='#F1EEE9')
rolllabel2.grid(row=2, column=1,sticky="w")

namelabel.place(relx=0.03,rely=0.1, relwidth=0.39, relheight=0.35)
rolllabel.place(relx=0.03,rely=0.6, relwidth=0.4, relheight=0.35)
namelabel2.place(relx=0.42,rely=0.1, relwidth=0.55, relheight=0.35)
rolllabel2.place(relx=0.43,rely=0.6, relwidth=0.55, relheight=0.35)

#footer
footer = Label(screen, text="> Sin Contacto <", font=('Arial 10 bold'),fg="#000000", bg="#EC994B")
canvas1.create_window(290, 535, window=footer)

screen.mainloop()