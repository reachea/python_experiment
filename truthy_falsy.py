# According to Python docs, any object can be tested truthy or falsy.

# Below are the Truthy values
True
2  # Any numeric values other than 0
[1]  # non-empty list
{'a': 1}  # non-empty dict
'a'  # non-empty string
{'a'}  # non-empty Set

# Below are the Falsy values
False
None
0
0.0
[]  # empty list
{}  # empty dict
()  # empty tuple
""  # empty string
range(0)  # empty set

# You can evaluate any object to bool using
bool(any_object)  # returns True or False
