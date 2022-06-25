print("Welcome to my mobile quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

user = input("What is your name? ")

print("Okay! " + user + " Let's play :)")
score = 0

answer = input("What is the capital of Malaysia? ")
if answer.lower() == "kuala lumpur":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Australia? ")
if answer.lower() == "canberra":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Brazil? ")
if answer.lower() == "brasilia":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Canada? ")
if answer.lower() == "ottawa" :
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Egypt? ")
if answer.lower() == "cairo":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" What is the capital of Saudie Arabia? ")
if answer.lower() == "riyadh":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of United State? ")
if answer.lower() == "washington":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What is the capital of China? ")
if answer.lower() == "beijing":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Finland? ")
if answer.lower() == "helsinki":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Germany? ")
if answer.lower() == "berlin":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Palestine? ")
if answer.lower() == "jerusalem":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Qatar? ")
if answer.lower() == "doha":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Jordan? ")
if answer.lower() == "amman":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Syria? ")
if answer.lower() == "damascus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Sudan? ")
if answer.lower() == "khartoum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Iraq? ")
if answer.lower() == "baghdad":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Jaban? ")
if answer.lower() == "tokyo":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Kuwait? ")
if answer.lower() == "kuwait city":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Morocco? ")
if answer.lower() == "rabat":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Türkiye? ")
if answer.lower() == "ankara":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of United Arab Emirates? ")
if answer.lower() == "abu dhabi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Tunisia? ")
if answer.lower() == "tunis":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Sweden? ")
if answer.lower() == "stockholm":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/ 25) * 100) + "%.")

