# The code which can raise exceptions can be wrapped in 'try' statement. 'except' will handle that exception.
try:
    some_error_raised
except:
    print('Exception handled')

# Every exception in Python will inherit from 'exception' class.

# In the below example, you can see that the 'NameError' is the exception class derived from the main 'Exception' class.
try:
    some_error_raised
except Exception as e:
    print('Exception raised')
    print(e.__doc__)  # <class 'NameError'>

# 'else' block will execute if the code in the 'try' block has raised no exception. This will be useful in many situations.

try:
    some_error_raised
except:
    print('Exception handled')
else:
    # this code will execute if no error is raised in the 'try' block
    print('No error raised. You can resume your operation here')

# final block
# Code in 'finally' block will execute no matter whether the exception is raised or not.
try:
    some_error_raised
except Exception as e:
    print('Exception raised')
else:
    print('This will execute if no error is raised in try')
finally:
    print('This code will run whether the code has error or not.')


# Raise your own exception. You can also create your own exception class inherited from Exception class.
try:
    raise ZeroDivisionError  # Python built-in exception class
except Exception as e:
    print(e.__class__)  # <class 'ZeroDivisionError'>

# Catch a specific exception.
try:
    raise ZeroDivisionError  # Python built-in exception class
except TypeError as e:
    print('Only type error exception is captured')
except ZeroDivisionError as e:
    print('Only zero division exception is captured')
except Exception as e:
    print('Other execeptions')
