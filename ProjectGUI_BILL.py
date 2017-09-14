from tkinter import *
from time import *
from datetime import *
import sqlite3
#from HelloWorld import read_from_db
#import HelloWorld
#import SesameF
#from SesameF import curtime
from math import *

'''
conn = sqlite3.connect('ProjectSesame.db')
c = conn.cursor()
'''
window = Tk()
window2 = Frame(master=window)
window3 = Frame(master=window2)
hello = StringVar()


window.geometry("500x500")

def onClick(*args):
    global student, imageLabel
    '''
    data = read_from_db(conn, c, enterID.get())
    for row in data:
        LastName =row[0]
        MiddleInitial = row[1]
        FirstName = row[2]
        StudentImage = row[3]
    student = PhotoImage(file="C:/Users/Student/Desktop/sesame-master/"+ StudentImage)
    imageLabel = Label(window2, image=student)
    imageLabel.grid(row = 3, column = 1)
    '''
    window2.grid(row = 3, column = 1)

def collapseWindow(*args):
    window2.grid_forget()
    clickButton.grid_forget()
    nameLabel.grid_forget()
    enterID.grid_forget()
    '''
    data = read_from_db(conn, c, enterID.get())
    for row in data:
        LastName =row[0]
        MiddleInitial = row[1]
        FirstName = row[2]
        StudentImage = row[3]
        '''
    helloLabel.place(x = 85, y = 0)
    backButton.place(x = 0, y = 0)
    billButton.place(x = 200, y = 50)
    #hello.set(FirstName + " " + MiddleInitial + " " + LastName + " Checked-in on " + str(datetime.now().strftime("%m/%d/%Y at %H:%M")))

def cancel(*args):
    window2.grid_forget()
    enterID.delete(0, END)
    
def goBack(*args):
    helloLabel.place_forget()
    backButton.place_forget()
    enterID.delete(0, END)
    nameLabel.grid(row = 0, column = 0)
    enterID.grid(row = 0, column = 1)
    confirmWindow.grid(row = 2, column = 1)
    cancelWindow.grid(row = 1, column = 1)
    clickButton.grid(row = 1, column = 1)
    
def billWindow():
    root = Tk()
    menu = Menu(root)
    menu.add_cascade(label="See Bill", menu=menu)
    menu.add_command(command='fill')
    menu.add_separator()
    menu.add_command(label="Exit", command=menu.quit) #Check this
    window3.grid(row=1, column=3)
    billButton.place_forget()
    window3.place(x=200, y=75)

'''  
def transTable():
    data = read_from_db(conn, c, enterID.get())
    for row in data:
        LastName =row[0]
        MiddleInitial = row[1]
        FirstName = row[2]
        StudentImage = row[3]
'''
nameLabel = Label(window, text="Enter Student ID")
clickButton = Button(window, text="Submit", command = onClick, pady=10)
enterID = Entry(window)
helloLabel = Label(window, textvariable = hello)
confirmWindow = Button(window2, text="Confirm", bg = "yellow", command = collapseWindow)
cancelWindow = Button(window2, text="Cancel", bg = "red", command = cancel)
backButton = Button(window, text="<--New User", bg = "green", command = goBack)
billButton = Button(window, text="See Bill", command = billWindow)

nameLabel.grid(row = 0, column = 0)
enterID.grid(row = 0, column = 1)
confirmWindow.grid(row = 2, column = 1)
cancelWindow.grid(row = 1, column = 1)
clickButton.grid(row = 1, column = 1)


window.bind('<Return>', onClick)
window.bind('<Tab>', collapseWindow)
window.bind('<BackSpace>', cancel)
window.bind('<Shift_L>', goBack)
window.mainloop()
