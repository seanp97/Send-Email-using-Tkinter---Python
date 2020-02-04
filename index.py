#This works for Gmail only. Allow less secure apps on Gmail settings

from tkinter import *
import sys
import tkinter
from tkinter import messagebox
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

email = ""
password = ""
message = ""
sendTo = ""

def sendEmail():
    try:
        global email
        email = Entry.get(userEmailEnt)
        global password
        password = Entry.get(userPasswordEnt)
        global message
        message = Entry.get(messageEnt)
        global sendTo
        sendTo = Entry.get(sendToEnt)
        server.login(email, password)
        server.sendmail(email, sendTo, message)
        messagebox.showinfo('Email', 'Message has been sent')
    except:
        Entry.insert(userEmailEnt, 0 , "Error")
        Entry.insert(messageEnt, 0 , "Error")
        Entry.insert(sendToEnt, 0 , "Error")
        messagebox.showwarning('ERROR', 'MESSAGE HAS NOT BEEN SENT!')

app = Tk()
app.title("Send Email")
app.geometry("900x450")

userEmail = Label(app, text="Email", padx=5, pady=5)
userEmail.grid(column=0, row=0)
userEmailEnt = Entry(app, bd=5)
userEmailEnt.grid(column=1, row=0)

userPassword = Label(app, text="Password", padx=5, pady=5)
userPassword.grid(column=0, row=1)
userPasswordEnt = Entry(app, bd=5, show="*")
userPasswordEnt.grid(column=1, row=1)

messageLabel = Label(app, text="Message", padx=5, pady=5)
messageLabel.grid(column=0, row=2)
messageEnt = Entry(app, bd=5)
messageEnt.grid(column=1, row=2)

sendToLabel = Label(app, text="Send to", padx=5, pady=5)
sendToLabel.grid(column=0, row=3)
sendToEnt = Entry(app, bd=5)
sendToEnt.grid(column=1, row=3)
sendToBtn = Button(app, text="Submit", command=sendEmail, padx=5, pady=5)
sendToBtn.grid(column=1, row=4)

app.mainloop()
