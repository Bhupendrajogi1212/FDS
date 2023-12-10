# Function for accepting the percentage of the Students
def input_percentage():
    perc = []
    number_of_students = int(input("ENTER THE TOTAL NUMBER OF STUDENTS : "))
    for i in range(number_of_students):
        perc.append(float(input("ENTER THE PERCENTAGE OF STUDENT {0} : ".format(i + 1))))
    return perc

# Function for printing the percentage of the Students
def print_percentage(perc):
    for i in range(len(perc)):
        print(perc[i], sep="\n")

# Function for performing partition of the Data
def percentage_partition(perc, start, end):
    pivot = perc[start]
    lower_bound = start + 1
    upper_bound = end

    while True:
        while lower_bound <= upper_bound and perc[lower_bound] <= pivot:
            lower_bound += 1

        while lower_bound <= upper_bound and perc[upper_bound] >= pivot:
            upper_bound -= 1

        if lower_bound <= upper_bound:
            perc[lower_bound], perc[upper_bound] = perc[upper_bound], perc[lower_bound]
        else:
            break

    perc[start], perc[upper_bound] = perc[upper_bound], perc[start]
    return upper_bound

## Function for performing Quick Sort on the Data
def Quick_Sort(perc, start, end):
    if start < end:
        partition_index = percentage_partition(perc, start, end)
        Quick_Sort(perc, start, partition_index - 1)
        Quick_Sort(perc, partition_index + 1, end)
    return perc

# Function for Displaying Top Five Percentages of Students
def display_top_five(perc):
    n = len(perc)
    print("TOP FIVE PERCENTAGE ARE : ")
    for i in range(n - 1, n - 6, -1):
        print(perc[i], sep="\n")

# Main
unsorted_percentage = []
sorted_percentage = []

while True:
    print("\n******PRACTICAL NO-07(B-16) QUICK SORT******")
    print("\n\tMENU\t")
    print("1. ACCEPT PERCENTAGE OF STUDENTS")
    print("2. DISPLAY PERCENTAGE OF STUDENTS(UNSORTED)")
    print("3. PERFORM QUICK SORT(SORTED)")
    print("4. DISPLAY TOP FIVE SCORES")
    print("5. EXIT")

    ch = int(input("ENTER YOUR CHOICE FROM MENUS(1-4): "))

    if ch == 1:
        unsorted_percentage = input_percentage()

    elif ch == 2:
        print_percentage(unsorted_percentage)

    elif ch == 3:
        print("PERCENTAGE OF STUDENT AFTER PERFORMING QUICK SORT : ")
        sorted_percentage = Quick_Sort(unsorted_percentage, 0, len(unsorted_percentage) - 1)
        print_percentage(sorted_percentage)

    elif ch == 4:
        display_top_five(sorted_percentage)

    elif ch == 5:
        print("THANKS!!!!!!")
        break

    else:
        print("INVALID CHOICE!!!!")
