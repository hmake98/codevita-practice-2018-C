# imports
import itertools

# taking input for numbers
numbers = int(input("Enter numbers: "))

# taking input for divider
divider = int(input("Enter divider: "))

# numbers list and taking numbers input
numbers_list = []
for i in range(0, numbers):
    number = int(input("Enter number: "))
    numbers_list.append(number)

#print(numbers_list)

# finding sum of each combination
sum_list = []
combination_list = []
for j in itertools.combinations(numbers_list, 3):
    mylist = list(j)
    combination_list.append(list(j))
    sum_list.append(sum(mylist))

#print(combination_list)
#print(sum_list)

# check if sum can be divide by divider
count = 0
for m in sum_list:
    if(m % divider == 0):
        count += 1
print("Possible pairs: ",count)





