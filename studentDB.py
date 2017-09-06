import sqlite3
import time
import datetime

conn = sqlite3.connect('business.db')
c = conn.cursor()

def create_student_table():
    c.execute('CREATE TABLE IF NOT EXISTS student(idnum TEXT, fname TEXT, lname TEXT, imagefile TEXT, gradelevel REAL)')

def create_transaction_table():
    c.execute('CREATE TABLE IF NOT EXISTS transactions(datestamp TEXT, idnum TEXT, totaltime REAL)')

def student_entry(idnum, fname, lname, imagefile, gradelevel):
    c.execute("INSERT INTO student(idnum, fname, lname, imagefile, gradelevel) VALUES (?, ?, ?, ?)", (idnum, fname, lname, imagefile, gradelevel))
    conn.commit()
    
def transaction_entry(datestamp, idnum, totaltime):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
    c.execute("INSERT INTO transactions (datestamp, idnum, totaltime) VALUES (?, ?, ?, ?, ?)", (datestamp, idnum, totaltime))
    conn.commit()

create_student_table()
create_transaction_table()
#To do make dummy data for student and transaction table
c.close()
conn.close()