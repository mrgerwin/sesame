regFile = open('StudentReg.csv','r')
contents=regFile.read()
students = []
studentInfo = []
word = ''
i = 1
for char in contents:
    if char == '\n':
        studentInfo.append(word)
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
        if i>4:
            students.append(studentInfo[0:4])
            studentInfo.clear()
            i = 1

print(students)
regFile.close()