from functools import reduce

print("# basic example")
x = lambda x:x +2
print(f"Add 2 to given number: {x(4)}")

#map(): list of squares if given list 
givenList = [2,5,6,8,14,54]
sqaures = list(map(lambda x:x **2, givenList))
print(f"Sqaure of given list: {sqaures}")


#filter() :filter even numbers from a given list
inputList = [12,34,53,64,75,36,21]
evenList = [x for x in inputList if x%2==0]
print(f"Even list using comprehensions: {evenList}")

filterEvenList = list(filter(lambda x: x%2 == 0, inputList))
print(f"Even list using filter & lambda: {filterEvenList}")

#sorted()
names = [("Vanshika", 25), ("Anshika", 22), ("Ritika", 30)]
sorted_by_age = sorted(names, key=lambda x: x[1])
print(sorted_by_age)


#with reduce()
#max value in numbers
numbers= [1,4,6,8,2,1,5,10]

max_number = reduce(lambda acc, x: acc if acc> x else x  , numbers)
print(f"Max number: {max_number}")

#sum of given numbers
sum_number = reduce(lambda acc, x: x+acc, numbers)
print(f"Sum of given numbers: {sum_number}")

print()
print("------ Intermediate Level ------")
print()

print("# Sort a list of tuples based on the second element using a lambda.")
items = [(1, 'b'), (3, 'a'), (2, 'c')]
print(f"Given items: {items}")
sorted_items = sorted(items, key= lambda x:x[1])
print(f"Sorted items: {sorted_items}")

print()
print("# Using reduce() and lambda, calculate the product of all elements.")
input_nums = [1, 2, 3, 4]
print(f"Input nums: {input_nums}")
product = reduce(lambda acc,x :x* acc, input_nums)
print(f"Product of nums: {product}")

print()
print("# Given a list of dictionaries, sort them by a key using a lambda.")
users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
print(f"Given dictionary : {users}")
sort_dict = sorted()