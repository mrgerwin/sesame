import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('ProjectSesame.db')
c = conn.cursor()

def create_table():
    #c.execute("CREATE TABLE IF NOT EXISTS TransactionTable (LastName TEXT, MiddleInitial TEXT, FirstName TEXT, SID REAL, Grade REAL, Age REAL, Adress TEXT, Guardian1 TEXT, Contact TEXT, StudentImage TEXT)")
 c.execute("CREATE TABLE IF NOT EXISTS TransactionTable (SID REAL, DateTime TIMESTAMP, TimeDelta INT)")


def data_entry():
    c.execute("INSERT INTO StudentInformation VALUES('Jones','C','Jason',665738, 10, 15, '11450 South River RD. Grand Rapids OH', 'Jennifer Jones', '703-482-0623', 'student0001.gif')")
    
    conn.commit()
    c.close()
    conn.close()

'''
def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

'''

def read_from_db(conn, c, SID):
    global LastName, MiddleInitial, FirstName, StudentImage
    SID = SID
    c.execute("SELECT LastName, MiddleInitial, FirstName, StudentImage FROM StudentInformation WHERE SID = " + SID)
    data = c.fetchall()
    return data

def dynamic_data_entry(fname, MI, SID, LN, Grade, Age, Address, PGuardian, PEmail, PPhone, G2, E2, P2, G3, E3, P3, G4, E4, P4, Allergies, Notes, StudentImage):
    sqlstring="INSERT INTO StudentInformation (MiddleInitial, FirstName, SID, LastName, Grade, Age, Address, Guardian1, Email, Contact, Guardian2, Email2, Contact2, Guardian3, Email3, Contact3, Guardian4, Email4, Contact4, Allergies, Notes, StudentImage) VALUES('"+MI+"', '"+fname+"', '"+SID+"', '"+LN+"', '"+Grade+"', '"+Age+"', '"+Address+"', '"+PGuardian+"', '"+PEmail+"', '"+PPhone+"', '"+G2+"' , '"+E2+"' , '"+P2+"' , '"+G3+"' , '"+E3+"' , '"+P3+"' , '"+G4+"' , '"+E4+"' , '"+P4+"' , '"+Allergies+"', '"+Notes+"', '"+StudentImage+"');"
    #print(sqlstring)
    c.execute(sqlstring)
    conn.commit()

def convertcsv():
    regFile = open('LatchkeyStudentReg.csv','r')
    contents=regFile.read()
    students = []
    studentInfo = []
    word = ''
    i = 1
    end = 22
    #Takes the stream from the file and parses it as separate pieces of data
    for char in contents:
        if char == '\n':
            # Name, SID, Address all stored info for each student
            studentInfo.append(word)
            # List of students
            students.append(studentInfo[0:end])
            studentInfo.clear()
            word =""
            i = 1
        elif not(char == ','):
            word = word + char
        else:
            studentInfo.append(word)
            word = ''
            i = i + 1
            # Every 4 pieces of data go to the next student
            if i>end:
                print(studentInfo)
                students.append(studentInfo[0:end])
                studentInfo.clear()
                i = 1

   # print(students)
    regFile.close()
    return students

#Gets the Students List but still has header info
students = convertcsv()
#Makes the students list iterable
studentsIter = iter(students)
#Advances the iterable list past the header
next(studentsIter)
next(studentsIter)
#Enters the student data into a record, one piece at a time
for student in studentsIter:
    #print(student)
    fname = student[1]
    MI = student[2]
    LN = student[3]
    SID = student[4]
    Age = student[5]
    Grade = student[6]
    Address = student[7]
    PGuardian = student[8]
    PEmail = student[9]
    PPhone = student[10]
    G2 = student[11]
    E2 = student[12]
    P2 = student[13]
    G3 = student[14]
    E3 = student[15]
    P3 = student[16]
    G4 = student[17]
    E4 = student[18]
    P4 = student[19]
    Allergies = student[20]
    Notes = student[21]
    StudentImage = student[4] + '.gif'
   # print(Notes)
    
    dynamic_data_entry(fname, MI, SID, LN, Grade, Age, Address, PGuardian, PEmail, PPhone, G2, E2, P2, G3, E3, P3, G4, E4, P4, Allergies, Notes, StudentImage)

#convertcsv()


  
#read_from_db()
#create_table()
#data_entry()


c.close
conn.close()