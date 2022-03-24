import random
print("NUMBER GUESSING GAME! WHOEHOO!")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9 :D:")

while chances < 5:

    guess = int(input("Enter your guess OR ELSE:-"))

    if guess == number:
         print("CONGRATS YOU WON YOU VERY PRO(Emoji SOOn)(Cool Face with dark sunglasses")
         break
                    
    elif guess < number:
        print("NOOBL", guess)

    else:
        print("NOOBH", guess)

    chances += 1

if not chances < 5:
    print("YOU LOOSE THE NUMBER IS",number)
