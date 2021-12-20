from logging import exception
from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP desk",font=("times new roman",30,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        img_top=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=650)

        dev_label=Label(f_lbl,text="EMAIL: en19ca502024@medicaps.ac.in",font=("times new roman",14,"bold"),bg="white",fg="black")
        dev_label.place(x=525,y=150)



if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()  
         