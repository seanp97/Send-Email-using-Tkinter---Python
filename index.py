from tkinter import *
import sys
import tkinter
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

email = ""
password = ""
message = ""

def getEmail():
    global email
    email = Entry.get(userEmailEnt)

def getPassword():
    global password
    password = Entry.get(userPasswordEnt)

def getMessage():
    global message
    message = Entry.get(messageEnt)

def sendEmail():
    server.login(email, password)
    server.sendmail(email, email, message)

app = Tk()
app.title("Send Email")
app.geometry("900x450")

userEmail = Label(app, text="Email", padx=5, pady=5)
userEmail.grid(column=0, row=0)
userEmailEnt = Entry(app, bd=5)
userEmailEnt.grid(column=1, row=0)
userEmailBtn = Button(app, text="Submit", command=getEmail)
userEmailBtn.grid(column=2, row=0)

userPassword = Label(app, text="Password", padx=5, pady=5)
userPassword.grid(column=0, row=1)
userPasswordEnt = Entry(app, bd=5, show="*")
userPasswordEnt.grid(column=1, row=1)
userPasswordBtn = Button(app, text="Submit", command=getPassword)
userPasswordBtn.grid(column=2, row=1)

messageLabel = Label(app, text="Message", padx=5, pady=5)
messageLabel.grid(column=0, row=2)
messageEnt = Entry(app, bd=5)
messageEnt.grid(column=1, row=2)
messageBtn = Button(app, text="Submit", command=getMessage)
messageBtn.grid(column=2, row=2)

sendToLabel = Label(app, text="Send to", padx=5, pady=5)
sendToLabel.grid(column=0, row=3)
sendToEnt = Entry(app, bd=5)
sendToEnt.grid(column=1, row=3)
sendToBtn = Button(app, text="Submit", command=sendEmail)
sendToBtn.grid(column=2, row=3)

app.mainloop()