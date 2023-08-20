from tkinter import *
from tkinter.font import Font 
form = Tk()
form.geometry('570x600+100+200')
form.resizable(False,False)
form.title("Calculator")
form.configure(bg='#000000')

equation=""

def show(value):
    global equation
    equation+=value
    Top_label.config(text=equation)


def clear():
    global equation
    equation=""
    Top_label.config(text=equation)

def calculate():
    global equation
    result=''
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    Top_label.config(text=result)






#top result and type place

Top_label=Label(form,width=25,height=2,text='',font=('arial',30))
Top_label.pack()

#First row

Button(form,text='C',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='blue',command=lambda: clear()).place(x=10,y=100)
Button(form,text='/',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('/')).place(x=150,y=100)
Button(form,text='%',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('%')).place(x=290,y=100)
Button(form,text='*',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('*')).place(x=430,y=100)

#Second Row

Button(form,text='7',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('7')).place(x=10,y=200)
Button(form,text='8',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('8')).place(x=150,y=200)
Button(form,text='9',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('9')).place(x=290,y=200)
Button(form,text='-',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('-')).place(x=430,y=200)

#Third row
Button(form,text='4',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('4')).place(x=10,y=300)
Button(form,text='5',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('5')).place(x=150,y=300)
Button(form,text='6',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('6')).place(x=290,y=300)
Button(form,text='+',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('+')).place(x=430,y=300)

#Fouth  row
Button(form,text='1',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('1')).place(x=10,y=400)
Button(form,text='2',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('2')).place(x=150,y=400)
Button(form,text='3',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('3')).place(x=290,y=400)

#Fifth  row
Button(form,text='0',width=11,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('0')).place(x=10,y=500)
Button(form,text='.',width=5,height=1,font=('times',30,'bold'),bd=1,fg='white',bg='#454545',command=lambda: show('.')).place(x=290,y=500)
Button(form,text='=',width=5,height=3,font=('times',30,'bold'),bd=1,fg='white',bg='Green',command=lambda: calculate()).place(x=430,y=400)


form.mainloop() 

