from time import *
from datetime import *
import time
import math
import os


HD=8
MD=60
H=datetime.now().strftime("%H")
M=datetime.now().strftime("%M")
H=int(H)
M=int(M)
deltah=HD-H
deltam=MD-M
deltah=abs(deltah)
delta=str(deltah)+":"+str(deltam)
print(delta)
print(deltah)

SID=666076
name='Blayk'
middleInitinal='R'
Lname='Sterling'
grade="2"
parentNamemale='t'
parentNamefemale="turte"
email="bman1920x@aol.com"
description="LATE"
rate=3
charge=deltah*rate
balance=100
paid=balance-charge


Y=str(datetime.now().strftime("%Y"))
Y=int(Y)
years=Y+1
curtime=time.time()
curtime=math.floor(curtime)
Date=datetime.now().strftime("%m"+"/"+"%d"+"/"+"%y")


def txtapp():
    if(os.path.getsize("testfilemth.txt")==0):
        fin="testfilemth.txt"
        file=open(fin,"w")
        file.write(name+" "+middleInitinal+' '+Lname+'\t'+str(SID)+'\n')
        file.write("Name:"+parentNamemale+" "+parentNamefemale+'\n')
        file.write("Latch Key"+"\t"+"Grade:"+grade+'\n')
        file.write("Email: "+email+'\n')
        file.write("Years: "+str(Y)+"-"+str(years)+'\n')
        file.write("EIN#34-6401543"+'\n')
        file.write("==============================================================="+'\n')
        file.write("KEEP FOR TEXAS!"+'\n')
        file.write("\n")
        file.write("#HRS"+"      IN "+"     DESCRIPTION"+"    PER"+"    AMT"+"     AMT"+'\n')
        file.write("      "+"   DATE "+"                "+"   HOUR"+ "   CHRG"+"    PAID"+"    TOTAL"+'\n')
        file.write("----------------------------------------------------------------"+'\n')
        
    fin="testfilemth.txt"
    file=open(fin,"a")
    file.write(" "+str(deltah)+"     "+str(Date)+"      "+description+"         "+"$"+str(rate)+"     "+"$"+str(charge)+ "      $"+str(charge)+"      $"+str(paid)+"\n")
    
    

txtapp()