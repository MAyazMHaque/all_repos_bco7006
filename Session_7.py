# Tuple
# tuple_1 =(1,4,7,10)
# tuple_2 = (2,4,7,9)
#
# tuple_3 = tuple_1 + tuple_2
#
# print(tuple_3[3])
#
# # exersice
# student = ("John", 75, "Engineering")
# name, score, college = student
# print(name, score, college)
#
# print(name)
# print(college)
# # lseft over naming convention if naming
# name_1, *score_1 = student
# print(name_1)
# print(score_1)


# Sets:

# number_set = set([1,2,4,5,6,7,"Apple"])
# print(number_set)
#
# fruit_set = {"Apple", "banana", "Orange"}
# print(fruit_set)
# print(number_set & fruit_set) # intersection oif two sets
# print(number_set | fruit_set) # gives all the valuses
# print(number_set - fruit_set ) # gives the difference of two sets
# number_set.add(40) # adding new element n the set
# print(number_set)
# number_set.remove("Apple")
# print(number_set)
# number_list = list(number_set)
# print(number_list)

# Dictionary Session_7

this_dict = {
    "brand" : "Toyota",
    "year" : 2016,
    "model" : "Rav4",
}
# print(len(this_dict))
# print(this_dict)
# this_dict["electric"] = "NO" # adding another key
# this_dict["color"] = ["Silver","Black"] # adding the key with list in the value
# print(this_dict)
# print(this_dict["color"][0]) # printing the
#
# print(this_dict.get("model")) # does the same thing as accessing the key and value of the dictionary
# print(this_dict.keys()) # give the keys of the dictionary
#
# this_dict["year"] = 2020 # changing the value of the key
# print(this_dict) # after the change
#
# print(this_dict.values())
# print(this_dict)
# del this_dict["year"] # delete the key with value
# this_dict.pop("model")

# items

# this_items = this_dict.items()
# print("Dictionary: ", this_dict)
# print("Items: ", this_items)


# For loop with dictionary
# print(this_dict)
#
# for x in this_dict:
#     print("Printing the keys", x)
#     print("Printing the values of dict", this_dict[x])

# Workshop3 Task

# states = {"VIC":"Victoria", "NSW": "New South Wales"}
# for x in states:
#     print(x)
#     print(states[x])

# exception handling
try:
    print(x)
except NameError:
    print("Please enter value of variable")
except:
    print("Something else is wrong")

