from tkinter import *
from tkinter import filedialog
from PIL import Image
import cv2
r=Tk()
a = StringVar()
r.geometry('300x300')
r.title('Face detection')
def file():
    try:
        i=filedialog.askopenfile(initialdir="/",title='Select a file',filetypes=(("Image files","*.jpg*"or"*.png*"),("all files","*.*")))
        s=str(i)
        f=s.find("'")
        s=s[f+1:]
        g=s.find("'")
        s=s[:g]
        s=s.replace("/","//")
        a.set(s)
    except:
        pass
def detect_face():
    try:
        cv2.destroyAllWindows()
        img = cv2.imread(a.get())
        face_cascade = cv2.CascadeClassifier('lbp_face.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if not faces == []:
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
                img = cv2.resize(img,(780,540),interpolation=cv2.INTER_NEAREST)
                l,k,j = img.shape
                if l>1800 and k>1800:
                    img=cv2.resize(img,(0,0),fy=0.1,fx=0.1)
                cv2.imshow('image',img)
        else:
            cv2.imshow('Image',img)
    except:
        print("error above")
        pass
    
l=Label(r,bg='yellow').place(x=0,y=0,height=300,width=300)
l1=Label(r,text='Select file:',bg='yellow',font=('Times New Roman',10),fg='blue').place(x=0,y=10)
d=Entry(r,fg='red',textvariable=a,font=('Times New Roman',10)).place(x=60,y=10,width=180)
b=Button(r,text='browse',command=file,fg='blue',font=('Times New Roman',10)).place(x=250,y=10,height=20)
b1=Button(r,text='Detect',command=detect_face,fg='blue',font=('Times New Roman',10)).place(x=125,y=40,height=30)
r.mainloop()
