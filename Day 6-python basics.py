# %%
import numpy as np


# %%
!pip install numpy

# %%
arr = np.array([1,2,3,4,5])
result = arr*10
print(result)

# %%
#Q2 - Create a NumPy array with values [2, 4, 6, 8, 10] and divide each value by 2.


arr = np.array([2, 4, 6, 8, 10])
ar2 = arr/2
print(ar2)

# %%
#Q3 - Create a NumPy array [5, 10, 15, 20, 25, 30] and extract:

# The middle two elements

# All elements except the first

# Every second element starting from the second element

# %%
#A3 - 

arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[2:4])
print(arr[1:])
print(arr[1::2])


# %%
#Q4 - Create a NumPy array: [10, 20, 30, 40, 50], and compute:
# The product of all elements
# The standard deviation (np.std())
# The square root of each element (np.sqrt())

# %%
arr = np.array([10, 20, 30, 40, 50])

print(arr.prod()) # Product
print(arr.std())  # Standard Deviation
print(np.sqrt(arr)) # Square Root

# %%
!pip install pandas
import pandas as pd

# %%
#Q5 - Pandas

s = pd.Series([28, 30, 27, 29], index = ['Mon', 'Tue', 'Wed', 'Thu'])
print(s['Wed'].mean())
print(s.mean())
list1 = s.tolist()
print(list1)

# %%
#Q6 - Pandas data frame

df1 = {
    'Employees':['Tom','Jane','Sam'],
    'Department':['HR','IT','Finance'],
    'Salary':[50000,60000,55000]
}

df = pd.DataFrame(df1)
df

df['Employees']
df.head(1)
avg_salary = df['Salary'].mean()
print(avg_salary)

# %%
df

# %%
print(df.loc[1,'Salary'])

# %%
print(df.iloc[2,1])

# %%
print(df.loc[0:1,:])

# %%
print(df.loc[0,:])

# %%
print(df.iloc[1,1])

# %%
print(df.iloc[:2,:])

# %%
df

# %%
high_salary = df[df['Salary']>50000]
print(high_salary)

# %%
# Show only employees in the "IT" department
# Show employees earning less than or equal to 55,000
# Show employees who are in "HR" or earn more than 55,000

# %%
df

# %%
IT_emp = df[df['Department']=='IT']
print(IT_emp)

# %%
less_salary = df[df['Salary']<=55000]
print(less_salary['Employees'])

# %%
# Show employees who are in "HR" or earn more than 55,000

df[(df['Department']=='HR') | (df['Salary']>55000)]

# %%
IT_emp = df[df['Department']=='IT']
print(IT_emp)
less_salary = df[df['Salary']<=55000]
print(less_salary['Employees'])
df[(df['Department']=='HR') | (df['Salary']>55000)]

# %%
df2 = pd.DataFrame({
    'Employee':['Tom', 'Jane', 'Sam', 'Alice'],
    'Department':['HR', 'IT', 'Finance', 'IT'],
    'Salary':[50000, 60000, 55000, 62000]
})

# %%
df2

# %%
df2.groupby('Department')['Salary'].mean()

# %%
df2.groupby('Department')['Salary'].max()

# %%
df2.groupby('Department')['Employee'].count()

# %%
avg_value_sorted = df2.groupby('Department')['Salary'].mean().sort_values(ascending = False)
print(avg_value_sorted)

# %%
df_emp = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name': ['Tom', 'Sam', 'Jane'],
    'Department': ['HR', 'Finance', 'IT']
})

df_sal = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Salary': [50000, 55000, 60000]
})

merged_df = pd.merge(df_emp, df_sal, on='EmpID', how='inner')
print(merged_df)

# %%
left_merged_df = pd.merge(df_emp,df_sal, on='EmpID', how='left')
print(left_merged_df)

# %%
df_bonus = pd.DataFrame({
    'EmpID':[1,3],
    'Bonus':[5000,7000]
})

# %%
bonus_merged = pd.merge(df_sal,df_bonus,on="EmpID", how='left')
print(bonus_merged)

# %%
df

# %%
df['Salary_Category'] = df['Salary'].apply(lambda x:"Low" if x < 55000 
                                  else "Med" if x<60000 
                                  else "High")

# %%
df['Salary_Category']
df

# %%



