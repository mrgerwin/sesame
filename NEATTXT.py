from tkinter import *
from time import *
from datetime import *
import time
import math
import os

midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
now = datetime.now()
delta = now - midnight
deltam=int(delta.seconds)//60
deltah=int(deltam)//60
deltami=str(datetime.now().strftime("%M"))
print(str(deltah) + ":" + str(deltami))

SID=666076
name='Blayk'
middleInitinal='R'
Lname='Sterling'
#54,900=3:15pm

curtime=time.time()
curtime=math.floor(curtime)
print(curtime)

def txtapp():
    if(os.path.getsize("testfilemth.txt")==0):
        fin="testfilemth.txt"
        file=open(fin,"w")
        file.write("==============================================")
        file.write('\n'+name+" "+middleInitinal+' '+Lname+'\t'+str(SID))
    fin="testfilemth.txt"
    file=open(fin,"a")
    file.write('\n'+"Date in: " + str(datetime.now().strftime("%m/%d/%Y")))
    
    H=datetime.now().strftime("%H")
    M=datetime.now().strftime("%M")
    H=int(H)
    M=int(M)
    
    if(H >= 16 and M>=15):
        
        file.write('\n'+"Time out: " + str(datetime.now().strftime("%H:%M:%S")))
        Due=timeSpent*3
        file.write('\n'+"Money Due: $"+str(Due))
    
    elif(H >=9 and H <= 11):
        timeSpent= 11-H
        file.write('\n'+"Time in: " + str(datetime.now().strftime("%H:%M:%S")))
    elif(H <=9):
        timeSpent=9-H
        file.write('\n'+"Time in: " + str(datetime.now().strftime("%H:%M:%S")))
    file.close()

txtapp()