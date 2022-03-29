# TASK: Define the Students class with its special methods.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/2b4b866e68b5f402c9bdcbfcfedde5b7
class Students:
    def __init__(self, names):
        self.names = names
        self.size = len(self.names)
        
    def __len__(self):
        return self.size
    def __str__(self):
        return f"{self.names}"
