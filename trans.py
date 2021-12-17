from logging import root
from tkinter import *
import tkinter
from PIL import Image,ImageTk
from googletrans import Translator
#TAO TK WINDOW
root=Tk()
root.title('SW TRANSLATE')
root.geometry('500x600')
root.iconbitmap('abc.ico')
load=Image.open('blue.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
#tao ten tieu de
name=Label(root,text='DESIGN BY STEVE',fg='#FFFFFF',bd=0,bg='#10A8FC')
name.config(font=('Transformer Movie',20))
name.pack(pady=30)
#tao o go van ban
box=Text(root,width=30,height=5,font=('ROBOTO',16))
box.pack(pady=15)
button_frame=Frame(root).pack(side=BOTTOM)
#dieu khien dich va xoa
def translate():
    INPUT=box.get(1.0,END)
    print(INPUT)
    t=Translator()
    a=t.translate(INPUT,src='vi',dest='zh-tw')
    b=a.text
    box1.insert(END,b)
    pass
def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
    pass
trans_button=Button(button_frame,text='translate text',font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=translate)
trans_button.place(x=130,y=280)
clear_button=Button(button_frame,text='clear text',font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=clear)
clear_button.place(x=290,y=280)
#tao o xuat ra ban dich
box1=Text(root,width=30,height=5,font=('ROBOTO',16))
box1.pack(pady=100)

root.mainloop()
