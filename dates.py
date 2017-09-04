import datetime
import time
import math

#Get the current date and time
readDate = datetime.datetime.now()

#Get the time from the datetime object
currentTime = readDate.time()

#construct datetime for school start time and end time
#datetime is required to do time math
schoolStart = datetime.datetime(readDate.year, readDate.month, readDate.day, 9,0,0)
schoolEnd = datetime.datetime(readDate.year, readDate.month, readDate.day, 15, 30, 0)

#Printing values for debugging purposes
print(readDate)
print(schoolStart)
print(schoolEnd)
print(currentTime)

#Calculating the time elapsed between the current time and school end time
if readDate>schoolEnd:
    timeIn = readDate-schoolEnd
elif readDate<schoolStart:
    timeIn = readDate-schoolStart
else:
    print("Time during the school day, 2 hr. Delay?")
    
timeInMinutes = timeIn.seconds//60
print(timeIn)
print(timeInMinutes)

#Determines how many 15 minute increments in the time delta
#Rounds up
quarterHours = math.ceil(timeInMinutes/15)
print(quarterHours)
cost = quarterHours * 3/4
print("Cost for "+ str(quarterHours) + " quarter hours is $" + str(cost))

#Current Unix stamp for use in the database
UNIX = time.time()

print(UNIX)