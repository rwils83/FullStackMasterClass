# TASK: Print the second word of the string with all letters in UPPERCASE.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: Solution: https://gist.github.com/b4shy/575282ef3c7abf9714167bcc44498627

input_string = "I love programming with python!"
new = input_string.split(" ")
new[1] = new[1].upper()
print(new[1])
