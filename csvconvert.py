'''
Take the file StudentReg.csv and make a list for each data row in the spreadsheet.  Return this as a list inside of a list.

'''
def convertcsv():
    regFile = open('StudentReg.csv','r')
    contents=regFile.read()
    students = []
    studentInfo = []
    word = ''
    i = 1
    #Takes the stream from the file and parses it as separate pieces of data
    for char in contents:
        if char == '\n':
            # Name, SID, Address all stored info for each student
            studentInfo.append(word)
            # List of students
            students.append(studentInfo[0:4])
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
            if i>4:
                students.append(studentInfo[0:4])
                studentInfo.clear()
                i = 1

    print(students)
    regFile.close()
    return students
