from tkinter import *
import tkinter.font as font
import random

def password_generate():
    paswrd_length=int(user_entry.get())
    if paswrd_length<=1:
        password_label.config(text="valid input!",fg="red")
        return
    char1='qwertyuiopasdfghjklzcxvbnm1234567890-=[\]/,QWERTYUIOPASDFGHJKLZXCVBNM'
    password_generate=''.join(random.choice(char1) for _ in range(paswrd_length))
    password_label.config(text=f'{password_generate}',font=('times',20,))
            

pasrd=Tk()
pasrd.title("Password Generator")
pasrd.geometry('350x350')
pasrd.config(bg='#ADD8E6')

lab=Label(pasrd,text='Password Generator',font=('time',20),fg='black',bg='#C0C0C0')
lab.pack()

user_label=Label(pasrd,text="The length of the password",font=('arial,30'),fg='blue')
user_label.pack(pady=10)

user_entry=Entry(pasrd)
user_entry.pack()

password_button=Button(pasrd,text='Generate',font=('times',10,'bold'),bd=1,fg='white',bg='#454545',command=password_generate).place(x=150,y=120)

genertae_label=Label(pasrd,text="Geneterated password",font=('arial,30'),fg='blue')
genertae_label.pack(pady=50)

password_label=Label(pasrd,width=10,height=1,text='',font=('arial',30))
password_label.pack(pady=10)

pasrd.mainloop()