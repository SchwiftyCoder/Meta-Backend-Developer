"""
IndexError
The below code has one problem. It is trying to locate an item from the list that does not exist. Running the code will throw the IndexError. Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".
"""
# Starter code
items = [1,2,3,4,5]
item = None
try:
    item = items[6]
except Exception as e:
    print(f"Error message: {e}") 
    print(f"error class: {e.__class__}") 

# if all goes well, print the element else None
print(item)


"""
ZeroDivisionError
In math there are rules about dividing by zero. The below code is trying to do just that and will throw a ZeroDivisionError. Add exception handling to return back 0 instead of allowing the error to be thrown.
"""
# Starter code
def divide_by(a, b):
    return a / b
    ans = None
    try:
        ans = divide_by(40, 0)
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(f"Error message: {e}")
        print(f"Error class: {e.__class__}")  
    print(ans)


"""
FileNotFoundError
The code below is looking for a file that does not exist. Add exception handling to catch this error and return the following "The file could not be found".
"""
# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print(f"Error message: {e}")
    print(f"Error class: {e.__class__}") 
