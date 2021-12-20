from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np





class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE  RECOGITION ",font=("times new roman",30,"bold"),bg="SILVER",fg="PURPLE")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        #first image
        img_top=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\face_detector1.jpg")
        img_top=img_top.resize((650,660),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=36,width=650,height=660)

        #second image
        img_bottom=Image.open(r"C:\Users\lenovo\Desktop\miner project face recognition\college_image\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((800,660),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb2=Label(self.root,image=self.photoimg_bottom)
        f_lb2.place(x=650,y=36,width=800,height=660)

        #Button
        b1=Button(f_lb2,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",16,"bold"),bg="red",fg="white")
        b1.place(x=310,y=582,width=180,height=35)

        
    #====================== face recognition==============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])  
                confidence=int((100*(1-predict/300)))

            try:

                   conn=mysql.connector.connect(host="localhost",username="root",password="vinayak",database="face_recognizer")
                   my_cursor=conn.cursor() 


                   my_cursor.execute("select name from student  where student_id="+str(id))
                   n=my_cursor.fetchone()
                   n="+".join(n)

                   my_cursor.execute("select roll_no from student where student_id="+str(id))
                   r=my_cursor.fetchone()
                   r="+".join(r)        

                   my_cursor.execute("select  Dep from student where student_id="+str(id))
                   d=my_cursor.fetchone()
                   d="+".join(d)

                   my_cursor.execute("select student_id from student where student_id="+str(id))
                   id=my_cursor.fetchone()
                   id="+".join(id)


                
                   if confidence>77:
                       cv2.putText(img,f"Roll_no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"name:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"Department:{d}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"StudentId:{id}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                   else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(255,255,255),3)
                                        
                     coord=[x,y,w,h]  
                    return coord 
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,2.1,10,(255,25,255),"Face",clf)   
            return img

        faceCascade=cv2.CascadeClassifier("C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\cv2\\data\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\lenovo\Desktop\miner project face recognition\classifier.xml") 

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img= recognize(img,clf,faceCascade)
            cv2.imshow("welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
              break
  
        video_cap.release()
        cv2.destroyAllWindows()    


            


        























if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()     