 faceCascade=cv2.CascadeClassifier(r"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\cv2\\data\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\lenovo\Desktop\miner project face recognition\classifier.xml") 

        video_cap=cv2.VideoCapture(0)