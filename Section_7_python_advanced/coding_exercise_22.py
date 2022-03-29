# TASK: Create the dogs.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/b4577386f34d7d5d1591770328defe24
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

lou = Dog("Lou", "Labrador")
hans = Dog("Hans", "German Sheppard")
print(f"{hans.name} and {lou.name} are friends")
