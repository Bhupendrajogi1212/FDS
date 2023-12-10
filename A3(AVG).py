# The average score of class

def average(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i] != -1:  # it is for absent student
            sum += l[i]
            cnt += 1

    avg = sum / cnt
    print("\nTotal Marks are : ", sum)
    print("\nAverage Marks are : {:.2f}".format(avg))


# Highest score in the class
def Maximum(l):
    Max = l[0]
    for i in range(len(l)):
        if l[i] > Max:
            Max = l[i]
    return Max


# Lowest score in the class
def Minimum(l):
    # Assign first element in the array which corresponds to marks of the first present student
    # This for loop ensures the above condition
    for i in range(len(l)):
        if l[i] != -1:
            Min = l[i]
            break

    for j in range(i + 1, len(l)):
        if l[j] != -1 and l[j] < Min:
            Min = l[j]
    return Min


# Count of students who were absent for the test
def absentCnt(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] == -1:
            cnt += 1
    return cnt


# Display mark with the highest frequency
def maxFrequency(l):
    i = 0
    Max = 0
    print(" \nMarks	> frequency count ")
    for ele in l:
        if l.index(ele) == i:
            print(ele, "	>", l.count(ele))
        if l.count(ele) > Max:
            Max = l.count(ele)
            mark = ele
        i += 1
    return mark, Max


# Input the number of students and their corresponding marks in FDS
marksInFDS = []
print("******PRACTICAL NO-01(A-2) STUDENT INFORMATION******")
noStudents = int(input("\nEnter the total number of students: "))

for i in range(noStudents):
    marks = int(input("Enter marks of Student " + str(i + 1) + " : "))
    marksInFDS.append(marks)

while True:
    print("\n/*************MENU**************/")
    print("1. The average score of class ")
    print("2. Highest score and lowest score of class ")
    print("3. Count of students who were absent for the test ")
    print("4. Display mark with the highest frequency ")
    print("5. Exit ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        average(marksInFDS)  # call to average function
    elif choice == 2:
        print("\nHighest score in the class is : ", Maximum(marksInFDS))
        print("\nLowest score in the class is : ", Minimum(marksInFDS))
    elif choice == 3:
        print("\nCount of students who were absent for the test is : ", absentCnt(marksInFDS))
    elif choice == 4:
        mark, count = maxFrequency(marksInFDS)
        print("\nHighest frequency of marks {0} is {1} ".format(mark, count))
    elif choice == 5:
        print("\nSUCCESSFULLY TERMINATED")
        break
    else:
        print("\nWrong choice")
