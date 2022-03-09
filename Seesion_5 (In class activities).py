print('09/03/2022')
 # changed the repo and folder name and making sure if it works or not
people = 20
cats  = 30
dogs = 15
if cats > people:
     print('Too many cats')

 # Example: 1
number_of_cars = int(input("How many cars do you have? "))
if number_of_cars > 5:
     print(f'you have {number_of_cars} cars, you should sell some cars')
elif number_of_cars > 2:
     print(f'you have {number_of_cars} which is good')
elif number_of_cars > 0:
     print(f'Having {number_of_cars} is good when fuel price is so high ')
else: print("Please buy something for your transport ")

 # Example :2: if and (else statment)
number_1 = int(input('Please enter any number: '))
number_2 = int(input('Please another number: '))
if number_1 > number_2:
     print('First number is bigger than second one')
elif number_2 == number_1:
     print("They are equal")
else: print("Second number is bigger than the first one")

# Example: For - Loops
product = 1
print(product)

# Example 3: Class activity:
lower_bound = int(input('Please enter the lower limit of numbers: '))
upper_bound = int(input('Please enter the upper limit of the numbers: '))
total = 0
if lower_bound < upper_bound:
     for count in range(lower_bound, upper_bound):
         total = total + count
         print("Current total is:",total)
     print("Total count is:",total)
else:
     print("Please enter the right values")

# Break Example:
for i in range(5):
     if i == 3:
         print("Lets break the loop because is i is: ",i)
         break
     print('Current value of i is: ', i)

 # Continue Example:
for i in range(5):
     if i == 3:
         print("Lets continue the loop although is i is: ",i)
         continue
     print('Current value of i is: ', i)

# Augmented assignment: i += 1 or i *= 2:
count = 0
while count < 10:
     print("Current value of count is: ",count)
     count += 0.5

print("last count is: ", count)
for count in range(1,5):
     product = product * (count + 1)

# is_done = False:

is_done = False
while not is_done:
    marks= int(input('Enter the marks: '))
    if marks >= 0 and marks <= 100:
        is_done = True
    else:
        print('Error: Pleas eenter valid marks betwwen zero and 100')

print("Your marks is: ", marks)