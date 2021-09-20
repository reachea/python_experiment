# The following while print till 5. Remember the indentation.
i = 0
while i <= 5:
    print(i)
    i += 1

# Using brake or continue in while loop
i = 0
while i <= 5:
    print(i)
    i += 1
    if i == 2:
        break  # You can try using continue here

# Here comes the interesting part. While loop has else part. Else part will execute once the entire loop is completed.
i = 10
while i <= 15:
    print(i)
    i += 1
else:
    print('Completed')

# But if you are using break in the loop, then Python will break out of the entire loop and it won't execute else part.
i = 10
while i <= 15:
    print(i)
    i += 1
    if i == 13:
        break
else:
    print('Completed')
