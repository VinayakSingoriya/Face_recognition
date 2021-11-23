

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN  DATA  SET",font=("times new roman",30,"bold"),bg="white",fg="MAROON")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        img_top=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\IMG_20211117_100310.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=225)

        #Button
        b1=Button(self.root,text="TRAIN  DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="CRIMSON",fg="AQUA")
        b1.place(x=0,y=265,width=1360,height=55)

        img_bottom=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\kinship.png")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=315,width=1360,height=350)


    def train_classifier(self):
        data_dir=(r"C:\Users\lenovo\Desktop\miner project face recognition\DATA")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) 
        

        # ============ Train the classifires=================
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\lenovo\Desktop\miner project face recognition\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")
    





        







if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        
