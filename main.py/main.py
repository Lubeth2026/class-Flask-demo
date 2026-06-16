
# DECORATOR Code Logic Example
# Creating a DECORATOR loud function to modify the bottom 3 functions to make them all Capital letters
def loud(func):
    def wrapper():
        result = func()   # This is the string "hello"
        return result.upper()   # This is returning the string "HELLO"
    return wrapper   # Returns the wrapper to replace your original function such as say_hello  

@loud
def say_hello():
    return "hello"

@loud
def say_goodbye():
    return "goodbye"

@loud
def greet():
    return "Hello, Dave!"

print(say_hello())
print(say_goodbye())
print(greet())
