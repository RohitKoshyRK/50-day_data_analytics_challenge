# #### Day 1 - Practising the Python basics
 
# Variables, types, operators, strings, lists, tuples, sets, dicts, loops, conditionals, comprehensions, enumerate, zip, map/filter
 
## Question 1: Reverse a list without using reverse(); Input: [1,2,3,4] → Output: [4,3,2,1]

input = [1,2,3,4]

## Solution 1

reversed_list = input[::-1]
print(reversed_list)

## Solution 2 - Using for loops

reversed_list1 = []
for item in input[::-1]:
    reversed_list1.append(item)

print(reversed_list1)


# Question 2 - Flatten a nested list
# Input: [[1,2],[3,4],[5,6]] → Output: [1,2,3,4,5,6]

# Solution to Q2

input = [[1,2],[3,4],[5,6]]
output = []
for sublist in input:
    for item in sublist:
        output.append(item)

print(output)


# %%
# Question 3 - Find unique elements from a list
#Input: [1,2,2,3,4,4] → Output: [1,2,3,4]

# %%
# Solution to Q3

input = [1,2,2,3,4,4]
output = []

for item in input:
    if item not in output:
        output.append(item)

print(output)        

# %%
# Question 4: Merge two dictionaries
# Input: {'a':1}, {'b':2} → Output: {'a':1,'b':2}

# %%
dict1 = {'a':1}
dict2 = {'b':2}

dict1.update(dict2) ## use update instead of append in the case of dictionaries. Append was used in lists

print(dict1)

# %%
## Question 5: Count frequency of elements in a list
## Input: [1,2,2,3,3,3] → Output: {1:1,2:2,3:3}

# %%
# Solution to Q5

input = [1,2,2,3,3,3]
freq = {}

for num in input:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)
    

# %%
# Q6 - Get all even numbers from a list using filter()
# Input: [1,2,3,4,5,6] → Output: [2,4,6]

# %%
# Solution to Q6 

input = [1,2,3,4,5,6,7,8,10]
even_numbers = []

for num in input:
    if num%2 == 0 and num not in even_numbers:
        even_numbers.append(num)


print(even_numbers)

# %%
# Question 7 - Square all numbers using map()
# Input: [1,2,3,4] → Output: [1,4,9,16]

# %%
# Solution to Q7

input = [1,2,3,4]
squared = list(map(lambda x:x**2, input))
print(squared)

# %%
# Q8 - Pair elements from two lists using zip()
# Input: [1,2,3] and ['a','b','c'] → Output: [(1,'a'),(2,'b'),(3,'c')]

# %%
# Solution to Q8

input1 = [1,2,3]
input2 = ['a','b','c']
list1 = list(zip(input1,input2))
print(list1)

# %%
# Q9 - List comprehension filter
# Get words longer than 3 letters: ["cat","dog","elephant"] → ["elephant"]

# %%
# Solution to Q9

input = ["cat","dog","elephant"]
gt3 = []

for item in input:
    if len(item)>3:
        gt3.append(item)

print(gt3)


# %%
# Q10 - Swap keys and values in a dictionary
# Input: {'a':1,'b':2} → Output: {1:'a',2:'b'}

# %%
# Solution to Q10
input = {'a':1,'b':2}
output = {value:key for key,value in input.items()}
print(output)

# %%
#Q11 - Find common elements in two lists
# Input: [1,2,3], [2,3,4] → Output: [2,3]

# %%
list1 = [1,2,3,2,3]
list2 = [2,3,4,2,3]
op1 = []

for item in list1:
    for item1 in list2:
        if item==item1:
            op1.append(item)

op1 = list(set(op1))
print(op1)

# %%
# Q12 - Enumerate a list
# Input: ['apple','banana'] → Output: [(0,'apple'),(1,'banana')]

# %%
input = ['apple','banana']
output = {}

for i in range(len(input)):
    output[i] = input[i]

print(output)

# %%
# Q13 - Generate a dictionary of number squares (1–10)
# Output: {1:1,2:4,3:9,...,10:100}

# %%
output = {}

for i in range(1,11,1):
    output[i]=i**2

print(output)

# %%
# Q14 - Check if a string is a palindrome
# Input: "level" → Output: True

# %%
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

is_palindrome("pop2")

# %%
#Q15 - Sort a list of tuples by second element
# Input: [(1,3),(2,2),(3,1)] → Output: [(3,1),(2,2),(1,3)]

# %%
input = [(1,3),(2,2),(3,1)] 
sorted_list = sorted(input, key=lambda x: x[1])

print(sorted_list)

# %%



