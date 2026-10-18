print("This is a line")

def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__": # a special built-in variable (often called a "dunder" or double-underscore variable) that is automatically evaluated to the name of the current module or script
    print(greet("Alice"))