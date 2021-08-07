import random
array_length = int(input("please enter length of array: "))
Array = []
arrays = random.randint(0,20)
while array_length>0 :
    if arrays in Array:
        arrays = random.randint(0,20)
    else:
        Array.append(arrays)
        array_length -=1
print("Your random array is : " , Array)