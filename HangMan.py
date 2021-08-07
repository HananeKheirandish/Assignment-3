import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'clock', 'engineer', 'toothpace', 'shirmoz','dog']
word = random.choice(words)
joon = 10
answer = []
print('- ' * len(word))
while joon > 0:
    user_character = input("enter word: ").lower()
    if user_character in word:
        answer.append(user_character)
    else:
        joon = joon - 1
        print("no!")
        if(joon == 0):
            print("You lose! ")
    turn = 0
    for char in word:
        if char in answer:
            print(char , end = ' ')
            turn += 1
        else:
            print('- ' , end = '')
    if turn == len(word):
        print('You Win. ')
        break
        