#Activity 11

def bubble(l):
    n = len(l)
    for i in range (n):
        for j in range (0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(f"The sorted list is: {l}")

def binary(l, key):
    first = 0
    last = len(l) - 1
    flag = False
    while (first <= last and not flag):
        mid = (first + last) // 2
        if l[mid] == key:
            flag = True
            print(f"It is at {mid} index")
        else:
            if key < l[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if flag == False:
        print("Element not found in the list")

def linear(l, key):
    flag = False
    for i in range (len(l)):
        if l[i] == key:
            flag = True
            print(f"It is at {i} index")
            break
    if flag == False:
        print("Element not found in the list")

l = list(map(int, input("Enter the list elements seperated by space: ").split()))
n = input("Enter 'B' for bubble sort, 'L' for linear search or 'BS' for binary search: ")
if n == 'B':
    bubble(l)
elif n == 'L':
    key = int(input("Enter the element to be found: "))
    linear(l, key)
elif n == 'BS':
    key = int(input("Enter the element to be found: "))
    binary(l, key)