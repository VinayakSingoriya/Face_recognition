from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        # FIRST IMAGE
        img=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\images.jpeg")
        img=img.resize((460,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=460,height=150)

        # second IMAGE
        img1=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\smart-attendance.jpg")
        img1=img1.resize((460,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=1,width=460,height=150)


        # third IMAGE
        img2=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\images (2).jpeg")
        img2=img2.resize((460,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=460,height=150)


        # Background IMAGE
        img3=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\0455.jpg_wh300.jpg")
        img3=img3.resize((1366,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=600)

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM ",font=("times new roman",30,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        # student button
        img4=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\safjqew.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=215,y=100,width=150,height=150)

        b1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=215,y=250,width=150,height=25)


        # Detect Face button
        img5=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\download.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=455,y=100,width=150,height=150)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=455,y=250,width=150,height=25)


        # Attendence Face button
        img6=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\World-water-day-1.png")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=695,y=100,width=150,height=150)

        b1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=695,y=250,width=150,height=25)


        # Help Face button
        img7=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\help.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=935,y=100,width=150,height=150)

        b1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=935,y=250,width=150,height=25)


        # Train Face button
        img8=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\c5b10e79-2344-4893-beac-2ee0b32dd789.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=215,y=320,width=150,height=150)

        b1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=215,y=450,width=150,height=25)


        # photo Face button
        img9=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\photo.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=455,y=320,width=150,height=150)

        b1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=455,y=450,width=150,height=25)


        # Developer Face button
        img10=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\web-developer-mobile-developer.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=695,y=320,width=150,height=150)

        b1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=695,y=450,width=150,height=25)


        # exit Face button
        img11=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\blue-exit-icon-25.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=935,y=320,width=150,height=150)

        b1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=935,y=450,width=150,height=25)




        
 
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
