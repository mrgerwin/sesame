from tkinter import *
from time import *
from datetime import *
import time
import math


window = Tk()
window2 = Frame(master=window)

fin="testfilemth.txt"
file=open(fin,"r")
inout=file.read().splitlines()[0]
inout=int(inout)


hello = StringVar()
student = PhotoImage(file="/home/pi/sesame/student0006.gif") #This is where we will need to get a image from the DB

window.geometry("500x500")

def loadBill():
    
    
    curtime=time.time()
    curtime=math.floor(curtime)
    #SID = '00001'
    #transaction_list=getTransactions(SID)
    
    #for item in transaction_list:
     #   print(item)
    
    billWindow = Frame(master=window)
    billWindow.grid(row=3, column=1)
    file=open("testfilemth.txt","r")
    #inout=file.read().splitlines()[0]
    file=open("testfilemth.txt","r")
    timein=file.read().splitlines()[1]
    file=open("testfilemth.txt","r")
    #timeout=file.read().splitlines()[2]
    inout=int(inout)
    #timeout=int(timeout)
    timein=int(timein)
    
    #fin="testfilemth.txt"
    #file=open(fin,"r")
    #inout=file.read().splitlines()[0]
    #inout=int(inout)
    
    
    if(inout==0):
        fin="testfilemth.txt"
        file=open(fin,"w")
        timein=curtime
        inout=1
        #file.write(str(inout))
        file.write("\n"+str(timein))
        #file.write("\n"+str(timeout))
        file.close()
    
    '''else:
        fin="testfilemth.txt"
        file=open(fin,"r")
        timein=file.read().splitlines()[1]
        timein=int(timein)
        timeout=curtime
        fin="testfilemth.txt"
        file=open(fin,"w")
        inout=0
        disp=1
        file.write(str(inout))
        file.write("\n"+str(timein))
        file.write("\n"+str(timeout))
    '''
    
    
    if(inout==1):    
        timedurring=timeout-timein
        times=timedurring
        timem=times//60
        timeh=timem//60
        #timeq=timeh//4
        moneys=3
        bill=moneys*timem
        billLabel = Label(billWindow, text="$" + str(bill))
        timespentLabel = Label(billWindow, text=str(timeh) + ":" + str(timem) + ":" + str(times))
        billLabel.grid(row = 0, column = 0)
        timespentLabel.grid(row = 1, column = 0)

    
    
def getTransactions(studentID):
    date1 = datetime(2017, 2, 4, 4, 0, 0)
    date2 = datetime(2017, 2, 4, 3, 30, 0)
    
    timeInAfterSchoolCare = date1-date2
    
    transaction = [date1, date2, timeInAfterSchoolCare]
    
    return (transaction)

def onClick():
    window2.grid(row = 3, column = 1)


def collapseWindow():
    window2.destroy()
    clickButton.destroy()
    nameLabel.destroy()
    enterID.grid_forget()
        
    if(inout==0):
        hello.set("studentNameVar" + " with Student ID " + enterID.get() + " Checked-in on " + str(datetime.now().strftime("%m/%d/%Y at %H:%M"))) #This statement will need to be changed in order to get all the info from the DB.
    else:
        hello.set("studentNameVar" + " with Student ID " + enterID.get() + " Checked-out on " + str(datetime.now().strftime("%m/%d/%Y at %H:%M"))) #This statement will need to be changed in order to get all the info from the DB.
    billButton.grid(row=4, column=1)
    #waybackButton.grid(row=5, column=1)
    loadBill()
    #if (datetime.now() >= ):
        #print("Your student was here for 5 hours.")


def cancel():
    window2.grid_forget()


nameLabel = Label(window, text="Enter Student ID")
billButton=Button(window, text="click to see bill", command= loadBill, pady=10)
#waybackButton=Button(window, text="click to go back", command= wayback, pady=10)
#message = Message(window, text="Check-in Time and Date", bg="yellow", font="Times 12 italic")
#message1 = Message(window)
#message2 = Message(window, text="Amount of Times Checked-in", bg="yellow", font="Times 12 italic")
#message3 = Message(window)
#message4 = Message(window)
clickButton = Button(window, text="Submit", command = onClick, pady=10)
enterID = Entry(window)
helloLabel = Label(window, textvariable = hello, bg = "yellow")
#billWindow = Message(window, text="Your bill is ", bg="red", fg="white", font="Times 12 italic")
confirmWindow = Button(window2, text="Confirm", bg = "yellow", command = collapseWindow)
cancelWindow = Button(window2, text="Cancel", bg = "red", command = cancel)
#enterTime = Message(window, text="The time your Student has spent ", bg="red", fg="white", font="Times 12 italic")
imageLabel = Label(window2, image=student)



nameLabel.grid(row = 0, column = 0)
enterID.grid(row = 0, column = 1)
confirmWindow.grid(row = 2, column = 1)
cancelWindow.grid(row = 1, column = 1)
imageLabel.grid(row = 3, column = 1)
clickButton.grid(row = 1, column = 1)
helloLabel.grid(row = 2, column = 1)
#message.grid(row = 3, column = 1)
#message1.grid(row = 4, column = 1)
#message2.grid(row = 5, column = 1)
#message3.grid(row = 8, column = 1)
#message4.grid(row = 6, column = 1)
#billWindow.grid(row = 9, column = 1)
#enterTime.grid(row = 7, column = 1)

window.mainloop()

