import random
print("Welcome to the BAND NAME GENERATOR.\n")
cities = list(map(str, input("Enter the names of all your favorite cities:-").strip().split()))
print(cities)
foods = list(map(str, input("Enter the names of all your favorite food:-").strip().split()))
print(foods)
rand1 = random.randint(0,len(cities)-1)
rand2 = random.randint(0,len(foods)-1)
print("My Band name suggestion is :- " +cities[rand1]+" "+foods[rand2])