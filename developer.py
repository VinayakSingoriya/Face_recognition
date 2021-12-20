from logging import exception
from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="MAROON")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        img_top=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=720)
         
         #FRAME
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=550)

        img_top1=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\IMG_20211205_194454.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=215,y=0,width=150,height=170)

        #DEVELOPER INFO
        dev_label=Label(main_frame,text="Hello My name is Sudhanshu",font=("times new roman",12,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=5)

        dev_label1=Label(main_frame,text="singoriya",font=("times new roman",12,"bold"),bg="white",fg="black")
        dev_label1.place(x=0,y=25)

        dev_label2=Label(main_frame,text=" I am  a fresher student.",font=("times new roman",12,"bold"),bg="white",fg="black")
        dev_label2.place(x=0,y=50)

        img2=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,399),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=180,width=500,height=399)

        

         



if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()