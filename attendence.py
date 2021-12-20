from logging import exception
from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        # FIRST IMAGE
        img=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\smart-attendance.jpg")
        img=img.resize((700,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=200)

        # second IMAGE
        img1=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\Sca01.jpg")
        img1=img1.resize((700,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=700,height=200)

        # Background IMAGE
        img3=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\0455.jpg_wh300.jpg")
        img3=img3.resize((1366,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1366,height=600)

        title_lbl=Label(bg_img,text="ATTENDENCE  MANAGEMENT  SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1345,height=680)

        # left lable side

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=10,width=665,height=600)

        img_left=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\school-attendance-1073x715.jpg")
        img_left=img_left.resize((655,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=655,height=120) 

        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=125,width=650,height=400)

        #LEBEL ENTRY
        attendenceID_label=Label(left_inside_frame,text="Attendence ID;",font=("times new roman",12,"bold"))
        attendenceID_label.grid(row=0,column=0,padx=10,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name
        rollID_label=Label(left_inside_frame,text="    Name",font=("times new roman",12,"bold"))
        rollID_label.grid(row=1,column=0,padx=10,sticky=W)

        atten_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        atten_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label=Label(left_inside_frame,text="    Roll",font=("times new roman",12,"bold"))
        roll_label.grid(row=0,column=2,padx=10,sticky=W)

        roll_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        roll_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #date
        name_label=Label(left_inside_frame,text="    Date",font=("times new roman",12,"bold"))
        name_label.grid(row=2,column=0,padx=10,sticky=W)

        atten_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        atten_name_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="  Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=3,column=0,padx=10,sticky=W)

        dep_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        dep_name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="    Time",font=("times new roman",12,"bold"))
        time_label.grid(row=4,column=0,padx=10,sticky=W)

        time_name_entry=ttk.Entry(left_inside_frame,width=22,font=("times new roman",12,"bold"))
        time_name_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #attendence
        attendence_label=Label(left_inside_frame,text="  Attendence",font=("times new roman",12,"bold"))
        attendence_label.grid(row=5,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=5,column=1,padx=10,pady=5)
        self.atten_status.current(0)


        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=715,height=33)

        save_btn=Button(btn_frame,text="Import csv",width=22,font=("times new roman",10,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)


        updae_btn=Button(btn_frame,text="Export csv",width=22,font=("times new roman",10,"bold"),bg="red",fg="white")
        updae_btn.grid(row=0,column=1)
    


        delete_btn=Button(btn_frame,text="Update",width=22,font=("times new roman",10,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",width=22,font=("times new roman",10,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)


        # right lable side

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence Details",font=("times new roman",15,"bold"),bg="white")
        Right_frame.place(x=675,y=10,width=665,height=500)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=650,height=425)

        #**********************scroll baar************************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_Y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
        








 

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)








if __name__== "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()  