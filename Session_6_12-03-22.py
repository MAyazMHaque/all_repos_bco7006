print ("Awesome Day")

# list

x = 3
another_list = [x, x+1, 'hello' * x]
print(another_list)
print(len(another_list))

second_list = list(range(1,5))
print("second List:",second_list)
# or lenght of the list can be save as a seperate variable
len_second_list = len(second_list)
print(len(second_list))
print(3 in second_list)
print(30 in second_list)
print(second_list)
print(second_list[2]) # select 2nd element of the list
print(second_list[-1]) # select last element of the list
print(second_list[2:4]) # select 3rd and 4th element of the list
first_list = [3,4,5,6]
print(first_list + second_list) # merging the two lists
print(first_list == second_list) # comparing two lists

third_list = [] # empty list will be filled by while or fpr loop
index = 0
# creating another list from first list with each element added by 3

while index < len(first_list):
    print(first_list)
    print(third_list)
    third_list.append(first_list[index] + 3)
    index += 1

print(first_list)
print(third_list)

list_of_fruits = ['apple', 'kiwi', 'mango', 'banana', 'cherry' ]
print(list_of_fruits)
fruits_with_a = [fruit for fruit in list_of_fruits if 'a' in fruit]
print(fruits_with_a)