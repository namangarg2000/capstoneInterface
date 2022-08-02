from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import ttk
import csv

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

label1 = Label(screen, text="PLEASE COME CLOSER TO THE SYSTEM!", font=('Arial 20 bold'),pady=30,padx=15,bg="#EC994B")
canvas1.create_window(297, 270, window=label1)

#footer
footer = Label(screen, text="> Sin Contacto <", font=('Arial 10 bold'),fg="#000000", bg="#EC994B")
canvas1.create_window(290, 535, window=footer)

screen.mainloop()