try:
    print("10"+10)
except IOError:
    print("You have an input output error")
    print("Did you check file permissions?")
except TypeError:
    print("You used the wrong data type somewhere you fuck")
except:
    print("You got an error")
finally:
    print("Finally block ran")


