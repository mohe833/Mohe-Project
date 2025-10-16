print("Welcome to Mohammed's Quiz App!")
user = input("What is your Name: ").upper()
print(f"Hello {user}. Welcome to my simple Quiz App")
score = 0
#Question 1
answer = input("1. What is the capital of Switzerland? ").capitalize()
if answer == "Bern":
    print("Correct!")
    score += 1
    print(f"wow {user} you did really great! You have {score} point")
else:
    print("Wrong! The correct answer is Bern")
    print(f"{user} you have {score}")
#Question 2
answer = input("2. What does CPU stand for? ")
if "central processing unit" in answer:
    print("Correct!")
    score += 1
    print(f"Wow {user} great job! You have {score} points!")
else:
    print("Wrong! The correct answer is << Central Processing Unit >>.")
#Question 3
answer = input("3. Which programming language are we using right now? ").capitalize()
if answer == "Python":
    print("Correct!")
    score += 1
    print(f"{user}, you are doing good job! You have {score}")
else:
    print("Wrong! The correct answer is Python")
    print(f"{user}, you have {score}")
print(f"\n You got {score} out of 3 questions!")
print("Thanks for plying!! Mohammed")