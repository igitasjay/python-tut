# if statements
# if 5 == 4:
#     print(True)
# elif len([2, 2, 4]) < 2 and 5 * 2 < 30:
#     print("list is long enough")
#     if 2 + 3 < 6:
#         print("condition is met")
#     else:
#         print(False)
# else:
#     print("no conditions met")

# while loop
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

# for loop
# my_list = [1, 2, 3, 4]
# for x in my_list:
#     print(x)
# my_dic = {
#     "name": "John",
#     "age": 30,
# }
# for key, value in my_dic.items():
#     print(key, value)

my_list = [1, 2, 3, 4, 5]
my_counter = 0
for x in my_list:
    if x == 2:
        print("the value is 2")
    else:
        print("the value is not 2")
while my_counter <= 6:
    print("last time")
    my_counter += 1