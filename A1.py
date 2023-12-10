Tt = []
A = []
B = []
C = []
t = int(input("Enter Total no of student in Class "))
a = int(input("Enter no of students who like CRICKET "))
b = int(input("Enter no of students who like BADMINTON "))
c = int(input("Enter no of students who like FOOTBALL \n\n"))
for i in range(a):
  r = int(input("Enter roll no of Student who like CRICKET "))
  A.append(r)
print("\n\n")

for i in range(b):
  r = int(input("Enter roll no of studen who like BADMINTON "))
  B.append(r)
print("\n\n")

for i in range(c):
  r = int(input("Enter roll no of student who like FOOTBALL "))
  C.append(r)
print("\n\n")

for i in range(t + 1):
  if (i != 0):
    Tt.append(i)
print("\n\n")

print("Roll no in class are", Tt)
print("Roll no of students who like CRICKET are", A)
print("Roll no of students who like BADMINTON are", B)
print("Roll no of students who like FOOTBALL are", C)

#for student who like only criket and badminton


def cric_badminton():
  CAB = []
  for i in A:
    temp = 0
    for j in B:
      if (i == j):
        temp = 1
    if (temp == 1):
      CAB.append(i)
  print("\n\nList of students who play both cricket and badminton", CAB)


cric_badminton()

#for student who like criket or badminton but not both


def cric_or_badminton():
  COB = []
  for i in A:
    temp = 0
    for j in B:
      if (i == j):
        temp = 1
    if (temp == 0):
      COB.append(i)
  for i in B:
    temp = 0
    for j in A:
      if (i == j):
        temp = 1
    if (temp == 0):
      COB.append(i)

  print("\n\n List of students who play either cricket or badminton but not both", COB)

