# %%
# Q1: Create a list of squares of even numbers from 1 to 10 using a list comprehension.

# %%
squares = [x**2 for x in range(1,11) if x%2==0]
print(squares)

# %%
#Q2 - words = ["sun", "elephant", "book", "table", "ai", "python"]
#Use a single list comprehension to create a new list containing only 
# the words longer than 4 letters. Paste your code and output here and I’ll review it.

# %%
words = ["sun", "elephant", "book", "table", "ai", "python"]

# %%
new_words = [word for word in words if len(word)>4]
print(new_words)

# %%
#Q3 - Q: Create a dictionary where the keys are numbers from 1 to 5, and the values are their cubes.

# %%
dict1 = {x:x**3 for x in range(1,6) }
print(dict1)

# %%
#Q4 - prices = {'apple': 50, 'banana': 30, 'orange': 40}
# Use dictionary comprehension to create a new dictionary where the prices are increased by 10%.


# %%
#A4 - Option 1 

prices = {'apple': 50, 'banana': 30, 'orange': 40}
new_prices = {key:prices[key]*1.1 for key in prices}
print(new_prices)

# %%
#A4 - Option 2

prices = {'apple': 50, 'banana': 30, 'orange': 40}
new_prices = {key:value*1.1 for key, value in prices.items()}
print(new_prices)


# %%
#Q5 - Create a generator that yields squares of numbers from 1 to 5, and print them.

# %%
def squares_gen(n):
    for i in range(0,n+1):
        yield i**2

gen = squares_gen(5)
for val in gen:
    print(val)

# %%
squares = [i**2 for i in range(0,5)]
print(squares)

# %%
# Q6 - Write a generator called even_gen that yields even numbers up to 20, 
# and print all values using a for loop.

# %%
#A6 - 

def even_gen(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i

gen = even_gen(20)
for val in gen:
    print(val)

# %%
#Q7 - Create an iterator for the string "Python" and 
# print each character using next() manually (one next() call per line).

string = "Python"
it = iter(string)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# %%
#Q8: Write code using a context manager (with) to open a file named test.txt in write mode 
# and write "Hello world!" into it.

# %%
#A8 -

with open('test.txt','w') as file:
    file.write("Hello World RK!")

# %%
#Q9 - Write a with statement to open a file named test.txt in read mode, 
# read all its lines, and print them.

# %%
#A9 - 
with open('test.txt','w') as file:
    file.write(" Hello work \n you rock \n we rock \n amazing")

with open('test.txt','r') as file:
    for line in file:
        print(line.strip())

# %%
#A9 - 
with open('test.txt','w') as file:
    file.write(" Hello work \n you rock \n we rock \n amazing")
    
with open('test.txt','r') as file:
    print(file.readlines())

# %%
#Q10 - Import the random module and:

# Use random.randint(1, 50) to generate 5 random integers between 1 and 50, 
# printing each inside a loop.

# %%
import random

for i in range(0,5):
    print(random.randint(1,50))

# %%
#Q11 - Using aliases:
# Import math module but rename it as m.
#Print:
"""
m.pi

m.sin(m.pi / 2)

💡 Reminder: sin(π/2) should output 1.0.

"""

# %%
import math as m

print(m.pi)

print(m.sin(m.pi/2))

# %%
#Q12 - Step 1: Create a file named maths.py to add two number using a function add
# Step 2: import the function and print the sum of two numbers into the add function as result

# %%
#A12 - 

with open("maths.py",'w') as file:
    file.write("def add(a,b):\n return a+b")


import maths

result = maths.add(3,8)
print(result)

# %%
## modules

# %%
with open("greet_module.py","w") as file:
    file.write("")

# %%
import greet_module
greet_module.greet("Rohit")

# %%
from shapes.circle import area

print(area(5))

# %%
from operations.multiply import multiply

print(multiply(4,5))

# %%



