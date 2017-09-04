import datetime
import time
import math
import sqlite3
import tkinter

#function definitions will go at the top of the program

'''
DataBase Functions

getStudentInfo should return the students Name, Grade,
and picture filename given the student ID number.

storeTransaction should store the appropriate information
in the database when a student in checkedIn/Out

getTransactions should query the database using the given
student ID, startDate, and endDate for all transactions
from the startDate until the endDate.  This is required
for billing.  It will call the getStudentInfo function so
that it can pass in the students name and grade to the bill.
It will also return the date each transaction occurred,
time spent in after school care, and the charge related to
each transaction.
'''
def getStudentInfo(ID):
    pass

def storeTransaction(ID, timeIn, quarterHours, cost):
    pass

def getTransactions(ID, startDate, endDate):
    pass

'''
Read and Write File Functions

readImage should take the student image filename and load
the file and store it in a file object.

writeBill should call the getTransactions function.
It will take the list of transactions for that student and
make a well formatted bill including student name, grade,
each transaction that took place which will be listed by date
showing how much time was spent in afterschool care and the
charge associated with each transaction.  Finally it will,
total up all of the charges and post the amount due.
It will output a textfile with the students name part of the
filename and a timestamp.

loadBill will allow the user to load a bill to the screen.
'''

def readImage():
    pass

def writeBill():
    pass

def loadBill():
    pass

'''
GUI windows

Main window that will allow the user to input
a student ID number and click an enter button.
This main window might also provide menu options
to allow the user to access future functionality.
For instance, we might allow the user to look up a student.
We will allow the user to generate a bill.

studentInfoWindow will show the students name, grade,
and image and allow the student to be checked in/out or
cancel and return back to the main window

confirmWindow will confirm to the user that the student has
been checked in/out at the given time (should display the time)

billWindow will allow the user to see a bill given the student
ID number.  There should be a textbox and a button to allow
the user to put in the ID number and access the monthly bill
if there is one.  If there is no monthly bill, then the window
will state that no bill is found.
'''