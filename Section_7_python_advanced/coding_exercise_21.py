# TASK: Implement the divider with error handling.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/bf9edbc97b27a1bb5c1d3cbfb0b02f19

def divider(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Please do not divide by zero!")
