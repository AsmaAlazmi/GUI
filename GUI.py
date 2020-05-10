from tkinter import *
from functools import partial


def validateLogin(Email, password):
	print("Email entered :",Email.get())
	print("password entered :",password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('300x300')
tkWindow.title(' sing in ')
tkWindow.configure(bg='white')


L1=Label(tkWindow,text="sing in ",bg="white" ,font=("bold",20)).place(relx=0.5,rely=0.1,anchor=CENTER)

#Email and Entry
Email=Label(tkWindow,text="Email address ",bg="white",font=("bold",7)).place(relx=0.2,rely=0.2)
Email = StringVar()
email=Entry(width="30",bg="white",textvariable=Email,fg="grey")
email.place(relx=0.2,rely=0.27)
email.insert(0,'Enter Email')


#password and Entry
Pass=Label(tkWindow,text="Password",bg="white",font=("bold",7)).place(relx=0.2,rely=0.35)
password = StringVar()
pwd=Entry(width="30",bg="white", textvariable=password,fg="grey",show="")
pwd.place(relx=0.2,rely=0.42)
pwd.insert(0,'Enter password')

#checkbuton
rem=Checkbutton(text="Remember me",bg="white").place(relx="0.2",rely="0.48")

forget=Label(tkWindow,text="Forgot",bg="white").place(relx="0.43",rely="0.67")

passw=Label(tkWindow,text="password?",bg="white",fg="#6c6ce6").place(relx=0.56,rely=0.67)

validateLogin = partial(validateLogin, Email, password)

#Submit button
loginButton = Button(tkWindow, text="Submit",width="25",bg="#6c6ce6", command=validateLogin).place(relx=0.2, rely=0.57)

tkWindow.mainloop()
