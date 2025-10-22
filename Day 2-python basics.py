# %%
#Q1 - Write a function sum_two_numbers(a, b) 
# that returns the sum of two numbers and raises a TypeError if inputs aren’t numeric.

# %%
#A1

def sum_two_numbers(a,b):
    if not (isinstance(a,(int,float))) and isinstance(b,(int,float)):
        raise TypeError("Both inputs must be numeric.")
    
    return a+b

sum_two_numbers(4,5)

# %%
#Q2 - Scope Test
# Demonstrate the difference between global and local scope by modifying a global variable inside a function.

x=10

def modify_variable():
    x=1
    x+=5
    print("Inside local var function x = ",x)

def modify_variable1():
    global x
    x+=5
    print("Inside global var function x = ",x)

modify_variable()
modify_variable1()

print("Outside function x = ", x)

# %%
# Q3 - Multiple Returns
# Write a function that returns both quotient and remainder, and unpack the returned tuple.

# %%
# A3

def division_fun(num, divisor):
    quotient = num//divisor
    rem = num%divisor
    return quotient,rem

q,r = division_fun(12,5)
print(q,r)


# %%
#Q4 - Multiply All
# Create a function multiply_all(*args) that multiplies all given numbers.

# %%
#A4 - 
def mul_all(*args):
    result = 1
    for num in args:
        result*=num
    return result


mul_all(2,3,7,2)

# %%
# Q5 - Print Person Info
# Write print_person(**kwargs) that prints person details (name, age, city), handling missing keys gracefully.

# %%
#A5 - 

def print_person(**kwargs):
    name = kwargs.get('name','Unknown')
    age = kwargs.get('age', 'unknown')
    city = kwargs.get('city','unkown')

    print(f"name: {name}")
    print(f"age: {age}")
    print(f"city: {city}")

print_person(name = "Rohan",age="42", city = "delhi")

# %%
# Q6 - Args + Kwargs Combo
#   Write a function that prints positional and keyword arguments separately and returns a summary string.

# %%
#A6

def args_kwargs_combo(*args,**kwargs):
    print("Args positional")
    for i, arg in enumerate(args,start=1):
        print(f" Arg{i}, {arg}")

    print("\nKwargs positional")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# %%
summary = args_kwargs_combo(1, 'apple', True, name='Alice', age=30, city='Paris')
print(summary)

# %%
# Q7 - Lambda Sort
# Use a lambda function to sort a list of tuples by the second element.

# %%
data = [(1, 'apple'), (3, 'duck'), (2, 'biscuit')]

new_sort = sorted(data, key = lambda x:x[1])
print(new_sort)

# %%
# Q8 - Map & Filter
# Given a list of integers, use map() and filter() with lambdas to square numbers and keep only even ones.

# %%
l1 = [1,2,3,4,5]
l2=[]

for num in l1:
    if num%2==0:
        l2.append(num**2)

print(l2)


# %%
l1 = [1,2,3,4,5]
res = list(filter(lambda x:x%2==0, map(lambda x:x**2,l1)))
print(res)

# %%
#Q9 - Anonymous Function Inside Function
# Create a function that uses a lambda to compute x^2 + 2x + 1 for a given x.

# %%
#A9 -  Create a function that uses a lambda to compute x^2 + 2x + 1 for a given x.

def new_fun(x):
    return (lambda x:(x**2)+(2*x)+1)(x)

result = new_fun(3)
print(result)

# %%
#Q10 - Safe Division
# Write a function to divide two numbers safely, handling ZeroDivisionError and TypeError.

# %%
def safe_division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both inputs must be numbers"
    else:
        return result
    
safe_division(5,15)

# %%
#Q11 -
# Try-Except-Finally
# Extend the previous challenge to include a finally block that always prints "Operation complete".

# %%
def safe_div(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both inputs must be numbers"
    else:
        return result
    finally:
        print("Operation complete")
    
print(safe_div(5,10))

# %%


# %%


# %%


# %%



