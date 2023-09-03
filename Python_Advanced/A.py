from common import shared_function

def a_function():
    return shared_function(), "Function a_function from A.py"

if __name__ == "__main__":
    result, message = a_function()
    print(result)
    print(message)
