        clf=cv2.faces.LBPHFaceREcognizer_create()
        clf.train(faces,id)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")
        cv2.face.