def Selection_Sort(marks):
  for i in range(len(marks)):
      # Find the minimum element in the remaining unsorted array
      min_idx = i
      for j in range(i + 1, len(marks)):
          if marks[min_idx] > marks[j]:
              min_idx = j

      # Swap the minimum element with the first element
      marks[i], marks[min_idx] = marks[min_idx], marks[i]

  print("MARKS OF STUDENT AFTER PERFORMING SELECTION SORTING : ")
  for i in range(len(marks)):
      print(marks[i])

# Function for Bubble Sort of elements
def Bubble_Sort(marks):
  n = len(marks)
  # Traverse through all array elements
  for i in range(n - 1):
      # Last i elements are already in place
      for j in range(0, n - i - 1):
          # Traverse the array from 0 to n-i-1
          # Swap if the element found is greater than the next element
          if marks[j] > marks[j + 1]:
              marks[j], marks[j + 1] = marks[j + 1], marks[j]

  print("MARKS OF STUDENT AFTER PERFORMING BUBBLE SORTING :")
  for i in range(len(marks)):
      print(marks[i])

# Function for displaying top five marks
def top_five_marks(marks):
  n = len(marks)
  print("TOP FIVE MARKS ARE : ")
  for i in range(n - 1, n - 6, -1):
      print(marks[i])

# Main
print("******PRACTICAL NO-05(B-14) BUBBLE & SELECTION SORT******")
n = int(input("\nENTER TOTAL NUMBER OF STUDENTS : "))
print("ENTER MARKS FOR ", n, "STUDENTS : ")
marks = []
for i in range(0, n):
  ele = float(input())
  marks.append(ele)  # adding the element

print("THE MARKS OF ", n, " STUDENTS ARE : ")
print(marks)

while True:
  print("\n\tMENU\t")
  print("1. SELECTION SORT")
  print("2. BUBBLE SORT")
  print("3. TOP FIVE FOR SELECTION SORT")
  print("4. TOP FIVE FOR BUBBLE SORT")
  print("5. EXIT")
  ch = int(input("\n\nENTER YOUR CHOICE (1-5) : "))

  if ch == 1:
      Selection_Sort(marks)
  elif ch == 2:
      Bubble_Sort(marks)
  elif ch == 3:
      top_five_marks(marks)
  elif ch == 4:
      top_five_marks(marks)
  elif ch == 5:
      print("\nTERMINATED!!!!!")
      break
  else:
      print("\nINVALID CHOICE!!")
      print("\nTHANKS!!!!!")
