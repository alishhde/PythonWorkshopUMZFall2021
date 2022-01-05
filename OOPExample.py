class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self, s):
        self.sound = s
    
    def speak(self):
        return f"{self.name}'s sound is {self.sound}"
    
    # def desc(self):
    #     return f"This object's name is {self.name}, and age is {self.age}"
    
    def __str__(self):
        return f"This object's name is {self.name}, and age is {self.age}"
    
# popi = Dog("Popi", 12)
# buddy = Dog("Buddy", 15)


# popi.sound("Q Q")

# print(popi.speak())

# print(popi.name)
# print(buddy.age)

# # print(popi.desc())
# print(popi)