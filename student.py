from logging import exception
from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")

        #===================== variable decreation===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_class_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()




        # FIRST IMAGE
        img=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\1578728506 (1).jpg")
        img=img.resize((460,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=460,height=150)

        # second IMAGE
        img1=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\aFKQWJF.jpg")
        img1=img1.resize((460,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=1,width=460,height=150)


        # third IMAGE
        img2=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\safjqew (1).jpg")
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

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1345,height=680)

        # left lable side

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=5,y=10,width=665,height=500)


        img_left=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\images.jpg")
        img_left=img_left.resize((655,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=655,height=120) 

        # current course 
        Current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course ",font=("times new roman",13,"bold"),bg="white")
        Current_course_frame.place(x=5,y=120,width=660,height=96)
         
        # Dpartment
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"), width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer science","IT","Civil","Mechnical", "MCA","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=1,pady=10)

        # Course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=15,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"), width=20,state="readonly")
        course_combo["values"]=("Select course","FE","ME","TE","BE", "MCA","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"), width=20,state="readonly")
        year_combo["values"]=("Select Year","2018-19","2019-20","2020-21","2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=1,sticky=W)

        # semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"), width=20,state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6" )
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=1,sticky=W) 


        # class student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",13,"bold"),bg="white")
        Class_Student_frame.place(x=5,y=220,width=660,height=250)

        StudentID_label=Label(Class_Student_frame,text="Student ID;",font=("times new roman",12,"bold"))
        StudentID_label.grid(row=0,column=0,padx=10,sticky=W)

        StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=22,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #StudentName
        StudentName_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        StudentName_label.grid(row=0,column=2,padx=10,sticky=W)

        StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=22,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,sticky=W)


        # class division
        Class_div_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"))
        Class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        class_div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_class_div,font=("times new roman",11,"bold"), width=20,state="readonly")
        class_div_combo["values"]=("A","B","C","Other")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=3,sticky=W)

        

        # ROLL NO
        roll_no_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=22,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=3,sticky=W)


        # Gender
        gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"), width=20,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=3,sticky=W) 

        


        # dob
        dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=22,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

       


        # email
        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=22,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)


        # phon no
        phon_label=Label(Class_Student_frame,text="Phon no:",font=("times new roman",12,"bold"))
        phon_label.grid(row=3,column=2,padx=10,sticky=W)

        phon_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=22,font=("times new roman",12,"bold"))
        phon_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)


        # Address
        address_label=Label(Class_Student_frame,text="Address:",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=22,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)


        # Teacher name
        teacher_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=22,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)

        #redio button
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text="Take photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0)


        Radiobutton2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        Radiobutton2.grid(row=5,column=1,padx=2,pady=5)

        #bbuttons frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=165,width=715,height=33)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=22,font=("times new roman",10,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)


        updae_btn=Button(btn_frame,text="Update",command=self.update_data,width=22,font=("times new roman",10,"bold"),bg="green",fg="white")
        updae_btn.grid(row=0,column=1)
    


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",10,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",width=22,command=self.reset_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=715,height=25)

        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=46,font=("times new roman",10,"bold"),bg="green",fg="white")
        take_photo_sample_btn.grid(row=0,column=0)

        update_photo_sample_btn=Button(btn_frame1,text="Update Photo Sample",width=46,font=("times new roman",10,"bold"),bg="green",fg="white")
        update_photo_sample_btn.grid(row=0,column=1)


        


        # right lable side

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"),bg="white")
        Right_frame.place(x=675,y=10,width=665,height=500)


        img_right=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\keyword-search-tips-blog-image-780.jpg")
        img_right=img_right.resize((655,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=655,height=120) 

        #             *****************searching ystem*******************


        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold"),bg="white")
        search_frame.place(x=5,y=125,width=660,height=55)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",11,"bold"), width=15,state="readonly")
        search_combo["values"]=("Select ","Roll_No","Phon_No" )
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W) 

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=4)

        search_photo_sample_btn=Button(search_frame,text="Search",width=14,font=("times new roman",11,"bold"),bg="silver",fg="black")
        search_photo_sample_btn.grid(row=0,column=3,padx=5,pady=4)

        showAll_photo_sample_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",11,"bold"),bg="silver",fg="black")
        showAll_photo_sample_btn.grid(row=0,column=4)


        #  ========= table frame===========
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=190,width=660,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","classdiv","rollno","gender","dob","email","Phoneno","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Rollno")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("classdiv",text="Classdivision")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phoneno",text="Phoneno")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("classdiv",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("Phoneno",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #==========================Function Decration==========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_class_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)                                                                                   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # =================== Fetch data======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    #========== get cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        contant=self.student_table.item(cursor_focus)
        data=contant['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_class_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #=================UPDATYE DETAILS==================    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this students details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_class_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)         
                
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                                                                      
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=================delete function==================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

 #================= Reset Function==========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_class_div.set("Selec Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #========== generate data set or take photo sample=================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosamole=%s where student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_class_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                   ))     
                conn.commit()
                self.fetch_data()  
                self.reset_data()   
                conn.close()

                #==================load predefined data on face frontals feom opencv==================
                face_classifier=cv2.CascadeClassifier("C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\cv2\\data\\haarcascade_frontalface_default.xml")
                

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
                    faces=face_classifier.detectMultiScale(gray,1.3,5)    
                    #scaling factor=1.3
                    #minimumNeighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)    
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450)) 
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path=r"C:\Users\lenovo\Desktop\miner project face recognition\DATA/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0))
                        cv2.imshow("face_croppede",face)  
    
                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()  
                messagebox.showinfo("Result","Generating data sets compled!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    




                    
                    




                  

                
                                                                                                                                                                                                                                                                                                                                                

        
               
    
                    

                
                   

                   

   
                
 
            
            
            
    






                
                    




                                                                                                                                                    



                    


        



    
    
                
            
                




     


                                                                                                                                                                                     






        


                                                                                                                 

                                                                                                                 




                
                    
               

            


               
                                                                                                      

            
             
                      
                                                                                                        
                                                                                                         

    
     
        
 



    

    

    






if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




        






      



