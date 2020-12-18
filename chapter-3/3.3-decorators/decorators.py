def null_decorator(func):
    # Returns a function not the function's result
    return func

def hello():
    return 'Hello, there'

hello = null_decorator(hello)
print(hello)
print(hello())