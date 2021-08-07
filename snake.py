snake_length = int(input("please enter long of snake: "))
if snake_length <= 0 :
    print("ERROR!")
else:
    for i in range(snake_length):
        if i%2 == 0:
            print('*', end='') 
        else:
            print('#' ,end='')
    