# For loops like for(i=0; i<5; i++) are not mostly used in Python. Instead, Python insists on iterating over items

arr = ['a', 'b', 'c', 'd', 'e']
for ele in arr:  # Prints every element in an array
    print(ele)

word = "python"
for char in word:  # Prints every char in the word
    print(char)

# You can use break, continue and else part in for-loop also.

# When talking about for loops, I noticed that most resources have also mentioned about range() function. (We will deal with functions later part of this article.)

# range() function will generates a sequence of numbers.

# range(start, stop, step)
# start - optional, the starting number. Default is 0. This number is included in the sequence
# stop - mandatory, the ending number. This number is excluded in the sequence
# step - optional, increments by. Default is 1.

range(3)  # This code generates a sequences from 0 to 2.
range(1, 4)  # This code generates a sequence from 1 to 3.
range(1, 8, 2)  # This code generates a sequence with 1, 3, 5, 7

for ele in range(3):  # Prints from 0 to 2.
    print(ele)

# In the below example, you can see I have used range to iterate through an array with index.
for index in range(0, len(arr)):
    print(arr[index])

dict = {'name': 'John wick'}

# You can iterate through a dictionary. items() will return both keys and values. You can also use keys() and values() if needed.
for key, value in dict.items():
    print(key + " is " + value)

# You can also use a built-in function enumerate(). enumurate() will return a tuple with index. It is mostly used to add a counter to the iterable objects in Python.
for index, value in enumerate(arr):
    print(value + " is present in " + str(index))
