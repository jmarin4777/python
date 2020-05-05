class Llama:
    def __init__(self, nameOfLama, catchphrase, blades_of_grass_eaten,hat=""): #double underscore surrounding init
        #ATTRIBUTES GO HERE (inside __init__ function)
        print('__init__ executed.')
        self.name = nameOfLama
        self.catchphrase = catchphrase
        self.blades_of_grass_eaten = blades_of_grass_eaten
        self.owner = {"name": "Joey", "age": 29}
        self.hat = hat
    #METHODS GO HERE (inside class)
    def say_info(self):
        print("My name is {}.  {}.  I have eaten {} blades of grass.".format(self.name, self.catchphrase, self.blades_of_grass_eaten))
        if self.hat != "":
            print(f"I also have a {self.hat}!")
        return self
    def owner_info(self):
        print(self.owner["name"])
        return self
    def spit(self, nameOfLama):
        print(f"{self.name} spit at {nameOfLama}!")



#INSTANCES ARE MADE HERE (outside class)
jeff = Llama('Jeff', "I am a Llama", "17","cowboy hat") 
harold = Llama('Harold', "Howdy", "998") 
jeff.say_info()
jeff.owner_info()
harold.say_info().owner_info()
jeff.spit(harold.name)

def jeff_conversation():
    jeff.say_info().owner_info().spit(harold.name)
jeff_conversation()