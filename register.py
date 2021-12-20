
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector




class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Register")

        #***********************variable**************************
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contect=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_ans=StringVar()
        self.var_password=StringVar()
        self.var_confirm_p=StringVar()





    


        img3=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\images (1).jpg")
        img3=img3.resize((1366,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=700)

        img4=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\experiment-5594881_1280.jpg")
        img4=img4.resize((350,400),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=60,y=150,width=350,height=400)

        frame=Frame(self.root,bg="white")
        frame.place(x=410,y=150,width=800,height=400)

        register=lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="navy",bg="white")
        register.place(x=15,y=15)

        #########################label##############################
        #*********************row 1 **********************
        fname=Label(frame,text="First Name",font=("times new roman",13,"bold"),bg="white")
        fname.place(x=30,y=60)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=30,y=95,width=230)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=400,y=60)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        self.txt_lname.place(x=400,y=95,width=230)

        #**************row 2**********************
        contect=Label(frame,text="Contect No",font=("times new roman",13,"bold"),bg="white")
        contect.place(x=30,y=130)

        contect_entry=ttk.Entry(frame,textvariable=self.var_contect,font=("times new roman",13,"bold"))
        contect_entry.place(x=30,y=160,width=230)

        email=Label(frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        email.place(x=400,y=130)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txt_email.place(x=400,y=160,width=230)

        #**********row3*****************
        security_Q=Label(frame,text="Select Security Question ",font=("times new roman",13,"bold"),bg="white")
        security_Q.place(x=30,y=190)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","what are your nationalities","your DOB")
        self.combo_security_Q.place(x=30,y=220,width=230)
        self.combo_security_Q.current(0)

        security_ans=Label(frame,text="Sequrity Answer",font=("times new roman",13,"bold"),bg="white")
        security_ans.place(x=400,y=190)

        self.txt_security_ans=ttk.Entry(frame,textvariable=self.var_security_ans,font=("times new roman",13,"bold"))
        self.txt_security_ans.place(x=400,y=220,width=230)

        #************row4*****************************
        password=Label(frame,text="Password",font=("times new roman",13,"bold"),bg="white")
        password.place(x=30,y=250)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",13,"bold"))
        self.txt_password.place(x=30,y=280,width=230)

        confirm_p=Label(frame,text=" Confirm Password",font=("times new roman",13,"bold"),bg="white")
        confirm_p.place(x=400,y=250)

        self.txt_confirm_p=ttk.Entry(frame,textvariable=self.var_confirm_p,font=("times new roman",13,"bold"))
        self.txt_confirm_p.place(x=400,y=280,width=230)

        #********************check button*************************
        self.var_checkbtn=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_checkbtn,text="I Agree Term and Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        Checkbtn.place(x=30,y=320)

        #****************************button***************
        img6=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\register-now-button1.jpg")
        img6=img6.resize((200,50),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(frame,image=self.photoimg6,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",font=("times new roman",15,"bold"))
        b1.place(x=10,y=350,width=200)

        img7=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\loginpng.png")
        img7=img7.resize((180,45),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(frame,image=self.photoimg7,borderwidth=0,cursor="hand2",bg="white",font=("times new roman",15,"bold"))
        b1.place(x=250,y=353,width=180)

        #****************funcion declartion*******************************
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select": 
         messagebox.showerror("Error","All fields are required")
        
        elif self.var_password.get()!=self.var_confirm_p.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition") 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select *from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist please try another email ")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contect.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security_Q.get(),
                                                                                        self.var_security_ans.get(),
                                                                                        self.var_password.get()
                                                                                      ))
            conn.commit()
            conn.close()      
            messagebox.showinfo("Success","Register successfully") 
             








        
        

       







        



4

        

if __name__== "__main__":
   root=Tk()
   obj=Register(root)
   root.mainloop()        
