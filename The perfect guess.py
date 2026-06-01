import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Enter your guess between 1 and 100: "))
    if (a>n):
        print("Too low! Try again.")
        guesses +=1
    elif (a<n):
        print("Too high! Try again.")
        guesses +=1

print(f"Congratulations! You've guessed the number {n} in {guesses} attempts")cc
    