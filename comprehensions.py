#Create a list of squares of numbers from 1 to 10.

x = [x**2 for x in range(1, 11)]
print (f"Squares for 1 to 10: {x}")
print()

# From a list of numbers, create a new list that contains only the even numbers.
list1 = [x for x in range(1,10)]
print(f"List of numbers= {list1}")
even = [x for x in range(1,11) if x%2==0]
evenBool = [x%2==0 for x in range(1,11) ]
print(f"Even numbers: {even}")
print(f"Even numbers: {evenBool}")


# Given a list of strings, create a list containing the lengths of those strings.
# Example: ["apple", "banana", "kiwi"] → [5, 6, 4]

# Create a list of characters from the string 'hello'.

# Create a list of all numbers from 1 to 20 that are divisible by 3.