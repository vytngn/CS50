# decorator: a function that takes a function and modify by adding some more behaviors
# and give back some output
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

#call function announce(hello()) --> replace  arg f() with hello()
@announce
def hello():
    print("Hello, world!")

#run the function hello
hello()
