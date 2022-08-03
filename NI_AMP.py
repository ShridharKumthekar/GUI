from tkinter import*
root=Tk()
#Setting title
root.title('Analog Integrated Circuits')
#to set the size/Geometry of the interface
root.geometry('700x500+350+200')
root['bg']='black'
#fontsize,bg,fg and bd of the title
label=Label(root,font=("Ariel",16),text='Gain & Output Calculator of OPAMP',bg="orange",fg="white",borderwidth=10,relief="sunken")
label.pack()
#fontsize,bg,fg and bd of the creater tag
label=Label(root,font=('Ariel',10),text='Created by: A&S',bg='powder blue',fg="black"
,borderwidth=5,relief='flat')
label.pack()
#adding an image of NI amp to the interface 
photo = PhotoImage(file="E:\GUI_project\op-amp_1.png")
label=Label(image=photo)
#placing the image to LHS of the interface
label.place(x=50,y=100)
f0 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f0.pack(fill="y",side="left")
f1 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f1.pack(fill="y",side="right")
#calculate gain function
def cal_gain():
   t1=int(a.get())
   t2=int(b.get())
   gain=1+(t2/t1)
   label.config(text=gain)
   return gain 
#Calculate gain
Label(root, text="Enter R1", font=('Calibri 10'),bg='Yellow',fg='black').pack()
a=Entry(root,width=40)
a.pack()
Label(root, text="Enter Rf", font=('Calibri 10'),bg='Yellow',fg='black').pack()
b=Entry(root,width=40)
b.pack()

#label=Label(root, text="", font=('Calibri 15'),bg='red',fg='black')
#label.pack(pady=20)
Button(root, text="Calculate gain", command=cal_gain).pack()
# Output(Vo)function
def cal_out():  
    x2=cal_gain()
    x1=int(y.get())
    output=x2*x1
    label.config(text=output)
#calculate output 
Label(root, text="Enter Input voltage(Vin)",font=('Calibri 10'),bg='Yellow',fg='black').pack()
y=Entry(root,width=40)
y.pack()
label=Label(root, text="Result", font=('Calibri 15'),bg='blue',fg='white')
label.pack(pady=20)
Button(root,text="Calculate output voltage",command=cal_out).pack()
root.mainloop()

