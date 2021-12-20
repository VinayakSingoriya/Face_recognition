from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from dns.resolver import query
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_page(win)
    win.mainloop()



class Login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Login")

        


        # Background IMAGE
        img3=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\photo-1513530534585-c7b1394c6d51.jpg")
        img3=img3.resize((1366,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=700)

       

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=125,width=320,height=465)

        img1=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=460,y=125,width=95,height=95)

        get_str=Label(frame,text="Get Started",font=("times new roman",17,"bold"),fg="white",bg="black")
        get_str.place(x=96,y=95)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=170,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=210)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=30,y=240,width=270)

        #icon image
        img2=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=390,y=266,width=25,height=25)

        img4=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\lock-512.png")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg4.place(x=390,y=336,width=25,height=25)

        #LOGIN BUTTON
        loginbtn=Button(frame,command=self.login,text="Login",font=("tomes new roman",14,"bold"),bd=4,relief=RIDGE,fg="WHITE",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=102,y=300,width=120,height=35)

        #REGISTRATION NUTTON
        register=Button(frame,text="New User Register",command=self.sidd_sing,font=("tomes new roman",10,"bold"),borderwidth=0,fg="WHITE",bg="Black",activeforeground="white",activebackground="black")
        register.place(x=25,y=360,width=120)

        #forget password
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("tomes new roman",10,"bold"),borderwidth=0,fg="WHITE",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=20,y=385,width=120)


    def sidd_sing(self):
        self.new_window=Toplevel(self.root)   
        self.app=Register(self.new_window) 

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")

        elif self.txtuser.get()=="angali" and  self.txtpass.get()=="sharma":
            messagebox.showinfo("Success","Successfully login")

        else:
            try:
             conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        

                                                                                     ))
             row=my_cursor.fetchone()
             
             if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
             else:
                open_main=messagebox.askyesno("YesNo","access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
        
                conn.close()                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #********************************* reset password***************************
    def reset_password(self):
        if self.combo_security_Q.get()=="":
            messagebox.showerror("Error","select security question",parent=self.root2)
        elif self.txt_security_ans.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="" :
            messagebox.showerror("Error","Please enter the new the password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and security_Q=%s and security_ans=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_ans.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)

            else:
                query=("update register set password=%s where email=%s")   
                value=(self.txt_new_password.get(),self.txtuser.get(),)
                my_cursor.execute(query,value)
                conn.commit() 
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password ",parent=self.root2)
                self.root2.destroy()



    

    #***************************forget password

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password " )
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
              messagebox.showerror("My Error","Please enter the valid username")

            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")  
                self.root2.geometry("340x450+350+155")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,'bold'),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question ",font=("times new roman",13,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","what are your nationalities","your DOB")
                self.combo_security_Q.place(x=50,y=110,width=230)
                self.combo_security_Q.current(0)

                security_ans=Label(self.root2,text="Sequrity Answer",font=("times new roman",13,"bold"),bg="white")
                security_ans.place(x=50,y=150)

                self.txt_security_ans=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_security_ans.place(x=50,y=180,width=230)

                new_password=Label(self.root2,text="New Password",font=("times new roman",13,"bold"),bg="white")
                new_password.place(x=50,y=210)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_new_password.place(x=50,y=240,width=230)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",13,"bold"),fg="white",bg="green")
                btn.place(x=135,y=285)





                
                
                       
            


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
             
        
        

    


        




        
        




if __name__== "__main__":
   main()      


