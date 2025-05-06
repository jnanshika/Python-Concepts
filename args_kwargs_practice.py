#sum of nums using *args
def add_all(*args):
    print(args)
    return sum(args)
print(add_all(1, 2, 3,4,5))     
print("----------")

#working with *args
def my_function(*args):
    print(args)

my_function(1, 2, 3, "hello") 
print("----------")

#print pairs using *args
def pairs(x,y):
    print(x,y)

list_pair = [(1,2), (4,5)]
pairs(*list_pair)
print("----------")

#Display information using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Vanshika", age=25, city="Delhi")
print("----------")


#Write a function introduce(name, *hobbies, **details) that:
def introduce(name, *hobbies, **details): 
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")
    for key, value in details.items():
        print(f"{key} = {value}")
    
introduce("Vanshika", "coding", "reading", age=25, profession="Developer")
print("----------")