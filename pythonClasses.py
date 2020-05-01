class Dog:
    dogInfo = "Class var on dogs!"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self, volume):
        print("Bark!" + " at volume " + str(volume))

mydog = Dog("Fido", 12, "Brown")  # create a var and assign a new Dog object to it

print("Newly created dog stats! " + mydog.name + " " + str(mydog.age) + " " + mydog.color)  # print the instances vars

mydog.bark(10) # call the bark method on the Dog object within the mydog var and pass in the volume

print(Dog.dogInfo)  # print the class var dogInfo from the class Dog
