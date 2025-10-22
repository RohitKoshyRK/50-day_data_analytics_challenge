# %%
#Q1 - Read a File
# Create a text file manually, then write a script to open and read its contents line by line.

# %%
with open('test.txt','r') as file:
    for line in file:
        print(line.strip())

# %%
#Q2 - Write to a File
# Write a program that takes user input and writes it into a text file (notes.txt).

# %%
#A2- 
user_input = input("Enter the text you want to save into the file: ")

with open('notes1.txt','w') as file:
    file.write(user_input)

print("Your notes have been written into notes1.txt")

# %%
# Q3 - Append Mode Practice
#Modify the previous code to append new lines without overwriting existing data.

# %%
#A3 - 

user_input = input("Enter the text you want to save")

with open('notes1.txt','a') as file:
    file.write(user_input + '\n')

print('Your input has been appended to notes1.txt')

# %%
# Q4 - Read CSV File
# Read a simple CSV file (e.g. name, age, city) and print each row neatly.

# %%
with open('names.csv','r') as file:
    for line in file:
        print(line.strip())

# %%
# Q5 - Write JSON File
# Create a Python dictionary and save it as a JSON file (data.json).

# %%
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "email": "johndoe@example.com",
    "is_active": True
}

# %%
import json

with open("data.json","w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved as data.json")



# %%
#Q6 - Read JSON File
#Load and print data from a JSON file you just wrote.

# %%
with open('data.json','r') as file:
    for line in file:
        print(line.strip())

# %%
with open("data.json",'r') as file:
    a = json.load(file)
    print(a)

# %%
#Q7 - File Path Management
# Use os and pathlib to list all .txt files in a directory.

# %%
#A7 - 

from pathlib import Path

directory = Path("C:\\Users\\rk\\Desktop\\Python")

txt_files = list(directory.glob("*.txt"))

print("Text files using pathlib:")
for file in txt_files:
    print(file.name)

# %%
#Q8 - Word Counter
# Write a function that reads a file and counts how many times each word appears.

# %%
words = {}

with open("word_count.txt",'r', encoding='utf-8') as file:
    text = file.read().lower()

words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word]=1

print(word_counts)


# %%
#Q9 - Regex Basics
# Given a string like "Contact me at email123@gmail.com or test_user@outlook.com", extract all valid email addresses.

# %%
import re

string = "Contact me at email123@gmail.com or test_user@outlook.com"

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, string)

print(emails)

# %%
#Q10 - Regex Cleaning
# Clean a messy string: "Price: $1,200.00!! Offer ends 10/10/2025??" → extract only the numeric value 1200.00 and date.

# %%
#A10 - 

import re
text = "Price: $1,200.00!! Offer ends 10/10/2025??"

#Extract numbers
number_pattern = r'\$?([\d,]+\.?\d*)'
number_match = re.search(number_pattern,text)

#Extract dates
date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
date_match = re.search(date_pattern, text)

if number_match:
    # Remove commas and convert to float
    numeric_value = float(number_match.group(1).replace(',', ''))
else:
    numeric_value = None

date_value = date_match.group(0) if date_match else None

print(f"Numeric value: {numeric_value}")
print(f"Date: {date_value}")

# %%


# %%


# %%


# %%


# %%


# %%


# %%



