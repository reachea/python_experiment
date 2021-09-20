# similar to lists but set is unordered list and cannot have duplication element
# by unordered means, we can't take element in any specific index only by looping

num = {1, 2, 3}

print(num)
print(type(num))

# looping through set

for n in num:
    print(n)

# adding element
num = {1, 2, 3}
print(num)

num.add(4)
print(num)

# adding multiple elements
num.update([4, 5, 6, 7])
print(num)

# remove
num.remove(1)
print(num)

# safer remove => discard: discard doesnt pop error when remove element inside set but remove do
num.discard(6)
print(num)
