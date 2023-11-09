def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

# Add the announce decorator
@announce
def hello():
    print("Hello, world!")

hello()