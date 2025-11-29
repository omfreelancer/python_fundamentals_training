class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "..."
    
    def info(self):
        return(f"Name: {self.name} | Age: {self.age}")

class Dog(Animal):
    def speak(self):
        return "wooof!"
    
    def fetch(self):
        return(f"{self.name} is fetching the ball!")

class Cat(Animal):
    def speak(self):
        return "meow!"
    
    def sleep(self):
        return(f"{self.name} is sleeping ...")
