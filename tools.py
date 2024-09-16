# user_name = "Anal"
# user_age = 21
# user_information = f"{user_name} is {user_age} years of age"
# print(user_information)

# single line if statements -- these are really just teneray operators
# user_name = "Anna"
# user_age = 12
# user_status = "adult" if user_age >= 18 else "child"

# print(f"This user is called {user_name}. The user is {user_age} years old. Therefore the user is {"an" if user_age >= 18 else "a"} {user_status}.")

# list comprehension
# simple_list = []
# for i in range(0, 10000001, 1):
#     simple_list.append(i)

# another_list = [f"{j}{i}" for i in range(0, 11, 1) for j in ("a", "b", "c") if j == "a"]
# print(another_list)

# lambda function -- lambda functions are just typically arrow fuctions
# double_value = lambda num: num * 2
# print(double_value(67))

# somw fucntions want a function as an argument
# random_list = [ 3, 4, 2, 0, 4, 8, 9, 3]
# sorted_list = sorted(random_list)
# print(sorted_list)

# now imagine that yo want to sort a tuple by a given key (tuple of name and age and by the age in this case)
# you can use a lambda function to do this
# but by defaukt python would sort this by alphabetical order
# tuple_list = [ ("anna", 23), ("james", 12), ("sam", 19), ("tobi", 21) ]
# sorted_tuple = sorted(tuple_list, key = lambda age: age[1])
# print(sorted_tuple)

my_list = [f"{j}{i}" for i in range(1, 6, 1) for j in ("A", "B", "C", "D", "E") if f"{j}{i}" != "C3"]
print(my_list)