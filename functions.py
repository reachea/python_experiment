def prints_hello_world():
    print('Hello world from Python')


prints_hello_world()

# Return statement


def prints_something(something):
    return something + ' from Python'


print(prints_something('Hello world'))

# If you pass wrong number of arguments like two or three arguments to this function then Python will throw an error.
print(prints_something())

# Default parameter. I think its common in most languages now.


def prints_something(something='Hello world'):
    print(something + ' from Python')

# keyword arguments. You can pass explicitly which parameter should be matched. In this way, you don't have to send the arguments in order just explicitly mention the parameter name.


def movie_info(title, director_name, ratings):
    print(title + " - " + director_name + " - " + ratings)


movie_info(ratings='9/10', director_name='David Fincher', title='Fight Club')


# Arbitrary number of arguments
# Sometimes, you dont know how many arguments are passed. In that case, you have ask Python to accept as many arguments as possible.

def languages(*names):
    print(names)  # ('Python', 'Ruby', 'JavaScript', 'Go'). This is a tuple.
    return 'You have mentioned ' + str(len(names)) + ' languages'


# You have mentioned 4 languages
print(languages('Python', 'Ruby', 'JavaScript', 'Go'))


def languages(fav_language, *names):
    print(names)  # ('Ruby', 'JavaScript', 'Go')
    return 'My favorite language is ' + fav_language + '. And Im planning to learn other ' + str(len(names)) + ' languages too'


# My favorite language is Python. And Im planning to learn other 3 languages too
print(languages('Python', 'Ruby', 'JavaScript', 'Go'))


# Arbitrary keyword arguments
# These types of arguments are useful when you don't know what kind of parameters are passed. In the previous case, it's useful when you don't know how many number of parameters are passed but in this case, you don't know what type of information will be passed.

def user_info(**info):
    # {'id': 1, 'name': 'Srebalaji', 'fav_language': ['Python', 'Ruby']} This is a dictionary
    print(info)


# Arbitrary keyword args will always expect to mention the parameters explicitly
user_info(id=1, name='Srebalaji', fav_language=['Python', 'Ruby'])

# The below code will throw error. There is no keyword arguments.
user_info(1, 'Srebalaji')


def user_info(id, name, **info):
    # {'fav_language': ['Python', 'Ruby'], 'twitter_handle': '@srebalaji'}
    print(info)


user_info(1, 'Srebalaji', fav_language=[
          'Python', 'Ruby'], twitter_handle='@srebalaji')
