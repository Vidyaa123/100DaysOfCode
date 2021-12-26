import random
import string
print("******PASSWORD GENERATOR******")
nochar=int(input("Enter number of characters in your password:- "))
splchar=int(input("Enter number of special characters in your password:- "))
num=int(input("Enter how many numbers in your password:- "))
character = nochar-(splchar+num)
random_char=[]

#generate random characters
for x in range(character):
    random_char.append(random.choice(string.ascii_letters))

#generate random special characters   
for x in range(splchar):
    random_char.append(random.choice(string.punctuation))

#generate random numbers
for x in range(num):
    random_char.append(random.choice(string.digits))
print(random_char)

#shuffle the generated password sequence
random.shuffle(random_char)
print("Your NEW password :- "random_char)