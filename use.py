#============== Load predifiend data on face frontals from opencv=================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
                    faces=face_classifier.detectMultiScale(gray,1.3,5)    
                    #scaling factor=1.3
                    #minimumNeighbor=5

                    for(x,y,w,h) in faces:
                        return face_cropped
                        face_cropped=img[y:y+h,x:x+W]  
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450)) 
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Crooped Face",face)
                
    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()  
                messagebox.showinfo("Result","Generating datab sets compled!!!!") 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   






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

def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
                
                
    
                    

                
                   
 


                
                   

                   

   
                
 
            
            
            
    






                
                    
