from common import shared_function

def b_function():
    return shared_function(), "Function b_function from B.py"

if __name__ == "__main__":
    result, message = b_function()
    print(result)
    print(message)
