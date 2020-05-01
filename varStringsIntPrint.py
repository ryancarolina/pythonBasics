# Vars and string concatenation
count = 0
age = 36
name = "Ryan"
name_age = name + str(age)
print("This is your name and age! " + str(name_age))


# If statements and comments
if age > 18:
    print(name + " you are older than 18")
else:
    print(name + " you are younger than 18")


# Functions
def hello(string="Default", int=0):  # Our function takes a string arg
    return "Hello " + string + ". The value of int is " + int

retVal = hello("Ryan", str(8))  # call the function here and pass in a string

print(retVal)


# Lists
dognames = ["Bob", "Fido", "Sally", "Reinhardt"]

dognames.insert(0, "Bingo")

print(dognames[0])  # return the 0 index value from the dognames list

randomlist = ["Ryan", 36, 88.8, False, True]  # lists in python can contain various types

print(randomlist)

catnames = ["Fisher", "Camper", "Mouser"]

del(catnames[2])  # remove the value at index 2 from the catnames list

print(catnames)

print(len(catnames))  # return the length of the catnames list

catnames[0] = "Mouser"  # update index 0 to a value of mouser

print(catnames)


# Loops
print("Printing dog names!")
for dog in dognames:
    print(dog)

for x in range(1,10):
    print(x)

while count < 10:
    print("Count is == " + str(count))
    count += 1


# Dictionaries
dic_dogs = {"Fido": 8, "Sally": 9, "Bingo": 10}

print("Bingo is how old? " + str(dic_dogs["Bingo"]))  # Look up the value of a key

dic_dogs["Popo"] = 2  # Add a key/value pair to our dictionary

print(dic_dogs)

del(dic_dogs["Popo"])  # Remove a key/value pair from our dictionary

print(dic_dogs)

dic_random = {"Key1": True, "Key2": False, "Key3": 44, "Key4": 88.08, "Key5": "String"}  # Dictionaries can contain various types

print(dic_random)




