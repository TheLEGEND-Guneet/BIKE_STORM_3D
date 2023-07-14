from tkinter import *
window=Tk()
window.geometry('800x600')
window.resizable(0,0)
'''
top_frame=tkinter.Frame(window).pack()
button_frame=tkinter.Frame(window).pack(side="bottom")

btn1=tkinter.Button(top_frame,text='Button1',fg='red',bg='black').pack()
btn2=tkinter.Button(top_frame,text='Button1',fg='red').pack()
btn3=tkinter.Button(top_frame,text='Button1',fg='red').pack()
#tkinter.Label(window,text='dfsgzdsfhdfgs',bg='cyan').pack(side='left',fill='y')

im=tkinter.PhotoImage(file='C:/Users/Guneet/Desktop/test/Photos/track.png')
def s(event):
  tkinter.Label(window,text='yoyo').pack()
def ss(event):
  tkinter.Label(window,text='yoyod').pack()
tkinter.Label(window,image=im).pack()
btn1=tkinter.Button(window,text='Button1',fg='red',bg='black')
btn1.bind('<Button-1>',s)
btn1.bind('<Button-3>',ss)
btn1.pack()

tkinter.Label(window,text='adsfsfg').grid(row=0)
tkinter.Label(window,text='a').grid(row =1)
tkinter.Entry(window).grid(row=0,column=1)
'''
'''
im=PhotoImage(file='Photos/track.png')
my_ca=Canvas(window,width=800,height=600)
my_ca.pack(fill='both',expand=True)

my_ca.create_image(0,0,image=im,anchor='nw')

my_ca.create_text(400,250,text='dfgg',font=('Helvetica',20),fill='red')

btn1=Button(window,text='Button1',fg='red',bg='black')
btn1_window=my_ca.create_window(10,10,anchor='nw',window=btn1)

btn2=Button(window,text='Button1',fg='red',bg='black')
btn2_window=my_ca.create_window(130,10,anchor='nw',window=btn2)

btn3=Button(window,text='Button1',fg='red',bg='black')
btn3_window=my_ca.create_window(250,10,anchor='nw',window=btn3)

#second method
im=PhotoImage(file='Photos/track.png')
lab=Label(window,image=im)
lab.place(x=0,y=0,relwidth=1,relheight=1)
label=Label(window,text='sd',bg='#32cbfe').pack(pady=20)
my_fr=Frame(window,bg='#32cbfe')
my_fr.pack()




btn1=Button(my_fr,text='Button1',fg='red',bg='black')
btn1.grid(row=0,column=0,pady=10,padx=10)
btn2=Button(my_fr,text='Button2',fg='red',bg='black')
btn2.grid(row=0,column=1,pady=10,padx=10)
btn3=Button(my_fr,text='Button3',fg='red',bg='black')
btn3.grid(row=0,column=2,pady=10,padx=10)
btn4=Button(my_fr,text='Button4',fg='red',bg='black')
btn4.grid(row=0,column=3,pady=10,padx=10)
'''
window.mainloop()