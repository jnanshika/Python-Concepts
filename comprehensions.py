#Create a list of squares of numbers from 1 to 10.
x = [x**2 for x in range(1, 11)]
print (f"Squares for 1 to 10: {x}")
print("------------")


# From a list of numbers, create a new list that contains only the even numbers.
list1 = [x for x in range(1,10)]
print(f"List of numbers= {list1}")
even = [x for x in range(1,11) if x%2==0]
evenBool = [x%2==0 for x in range(1,11) ]
print(f"Even numbers list: {even}")
print(f"Even numbers boolean list: {evenBool}")


# Given a list of strings, create a list containing the lengths of those strings.
# Example: ["apple", "banana", "kiwi"] → [5, 6, 4]
print("------------")
givenList = ["apple", "banana", "kiwi"]
length = [len(x) for x in givenList]
print(f"Lengths of words in given list {length}")


# Create a list of characters from the string 'hello'.
print("------------")
word = "hello"
listChar = [x for x in word]
print(f"List of character in given word: {listChar}")


# Create a list of all numbers from 1 to 20 that are divisible by 3.
print("------------")
div3 = [x for x in range(1,21) if x%3==0]
print(f"list of all numbers from 1 to 20 that are divisible by 3: {div3}")


# From a list with duplicates, create a set of unique words.
# Input: ["apple", "banana", "apple", "orange"]
print("------------")
Input= ["apple", "banana", "apple", "orange"]
output = {x for x in Input}
print(f"Distinct set: {output}")

# Given a list of numbers, create a set of their squares.
print("------------")
setSquareSet = {s*s for s in range(1,21) }
setSquareList = [s*s for s in range(1,21) ]
print(f"Set of squares in 1 to 20 : {sorted(setSquareSet)}")
print(f"List of squares in 1 to 20 : {setSquareList}")

# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
print("------------")
valueDict = {x : x**2 for x in range(1,6)}
print(f"Dictionary : {valueDict}")


# Given a list of strings, create a dictionary with string as key and its length as value.
# Input: ["cat", "dog", "elephant"]
print("------------")
input_list = ["cat", "dog", "elephant"]
outputDict = {x: len(x) for x in input_list}
print(f"word-length dictionary: {outputDict}")


# Invert a dictionary: swap keys and values.
# Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}
print("------------")
input_dict = {"a": 1, "b": 2}
swappedOutput = {value:key for key,value in input_dict.items()}
print(f"Swapped Dictionary: {swappedOutput}")