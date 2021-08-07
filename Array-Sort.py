Array = []
Array_Test=[]
array_length = int(input("please enter length of Array: "))
for i in range(array_length):
    numbers = int(input("please enter numbers of Array: "))
    Array.append(numbers)
    Array_Test.append(numbers)
Array_Test.sort()
if Array == Array_Test:
    print("Your array is sort.")
else:
    print("Your array is not sort.")