# for loop

numbers = [1, 1, 2, 2, 3, 4, 5, 5, 5, 6]

set = set()

for num in numbers:
    if num % 2 == 0:
        set.add(num)

print(set)

# while loop

age = 25

while age < 40:
    print(age)
    age += 1


# guess = input("Guess a number between 1 and 10: ")

# while guess != '8':
#     guess = input("Guess a number between 1 and 10: ")

# print("You win!😍")


# break, continue and else

for x in range(10):
    print(x)
    if x == 5:
        break


# else part will run after the for loop
# break will skip the else part
for x in range(10):
    print(x)
    if x == 5:
        continue
    print("rest part")
else:
    print("😇")
