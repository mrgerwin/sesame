import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('ProjectSesameDB.db')
c = conn.cursor()

def transactionEntry(SID, datestamp, timespent):
    sqlstring="INSERT INTO TransactionTable (SID, DateTime, TimeDelta) VALUES("+SID+ ', '+datestamp+ ", "+ timespent+');'
    
    
    
    
    c.execute(sqlstring)
    
    conn.commit()
    c.close()
    conn.close()

def getTransaction(ID):
    transactions=[]
    sqlstring="SELECT Datetime, TimeDelta FROM TransactionTable"
    sqlstring = sqlstring +" WHERE SID="+ID
    c.execute(sqlstring)
    data = c.fetchall()
    print(data)
    
getTransaction('666076')
#getTransaction('668756')