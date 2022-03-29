# TASK: Implement the calculator.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution https://gist.github.com/b4shy/846ec0bd64beaf275f0e68876b5978d0

def calculator(a, b, c):
    if c == "-":
        return a-b
    if c == "+":
        return a+b
    else:
        return "Please enter + or -"
