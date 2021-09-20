# list is ordered and can have duplication element

name = ['jack', 'john', 'josh']

print(name)

# sorting function
alphabet = ['z', 'a', 'c']

alphabet.sort()

print(alphabet)

# reverse the sorted alphabet

alphabet.sort(reverse=True)

print(alphabet)

# .sort(reverse=True) vs .reverse(): sort with reverse=True will sort the list reversely while .reverse() will only reverse the list but not sorting

first_num_list = [3, 1, 2]
second_num_list = [3, 1, 2]

first_num_list.sort(reverse=True)

print(first_num_list)

second_num_list.reverse()

print(second_num_list)

# slicing elements

alphabet = ['a', 'b', 'c', 'd', 'e']

print(alphabet)

# concate alaphabet list and num list

num = [1, 2, 3]

alphabet = ['a', ' b', 'c']

new_list = num + alphabet

print(new_list)

print(type(new_list))

# adding and remove
print(">>>>> ADDING AND REMOVE <<<<<")

numbers = [2, 3, 1]
print(numbers)

# add number in the last index
numbers.append(10)
print(numbers)

# remove the last number
numbers.pop()
print(numbers)

# remove insert in specific index

numbers.insert(1, 3)
print(numbers)
