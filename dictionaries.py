# define dictionaries

dictionaries = {'name': 'reachea', 1: "3"}
print(dictionaries[1])

# adding new values

dictionaries['new_value'] = 'ok'
print(dictionaries["new_value"])

# changing state

dictionaries["new_value"] = "not ok"
print(dictionaries["new_value"])

# checking types, length, values, keys

print(type(dictionaries))
print(len(dictionaries))
print(dictionaries.values())
print(dictionaries.keys())


# Example of nested dict.
user = {
    'id': 1,
    'name': 'John wick',
    'cars': ['audi', 'bmw', 'tesla'],
    'projects': [
        {
            'id': 10,
            'name': 'Project 1'
        },
        {
            'id': 11,
            'name': 'Project 2'
        }
    ]
}

# access nested dict

print(user["projects"][0]['name'])

print(user.items())
