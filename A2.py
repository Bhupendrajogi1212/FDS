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


# for nither cricket nor badminton


def ncnb():
  cbh = []

  for i in (Tt):
    temp = 0
    for j in (A):
      if (i == j):
        temp = 1
        break

    for k in (B):
      if (i == k):
        temp = 1
        break

    if (temp == 0):
      cbh.append(i)
  print("\n\nList of students who play neither cricket nor badminton", cbh)


ncnb()

#for students who like cricket and football but not badminton


def cfnb():
  cf = []
  for i in (A):
    temp = 0
    for j in (C):
      if (i == j):
        temp = 1
        break
    if (temp == 1):
      flag = 0
      for k in B:
        if (i == k):
          flag = 1
          break
      if flag == 0:
        cf.append(i)
  print("\n\nList of students who play cricket and football but not badminton", cf)


cfnb()
