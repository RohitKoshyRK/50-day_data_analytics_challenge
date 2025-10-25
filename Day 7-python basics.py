# %%
import pandas as pd

# %%
data = {
    'Name':['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Sales':[12000, 15000, 9000, 18000, 16000]
}

df = pd.DataFrame(data)

# %%
df

# %%
#Q1 - Find the minimum and maximum sales value.
"""
Calculate the average sales.

Identify the best performing employee (highest sales).

Sort the DataFrame in descending order of Sales.

"""

# %%
average_sales = df['Sales'].mean()
print(f"Average sales is: {average_sales}")

# %%
max_index = df['Sales'].idxmax()
max_sales = df['Sales'].max()
best_perf_name = df.loc[max_index, 'Name']

print(f"The best performing employee is {best_perf_name} with {max_sales} in sales")

# %%
min_index = df['Sales'].idxmin()
min_sales = df['Sales'].min()
min_sales_name = df.loc[min_index,'Name']
print(f"The employee with min sales is {min_sales_name} with {min_sales} in sales")

# %%
## Q2 - 

"""
Find the lowest productivity score.

Find the highest productivity score.

Compute the average productivity.

Identify the top performer.

Sort the employees in descending order of productivity.

"""

data = {
    'Employee': ['Raj', 'Simran', 'Aman', 'Priya', 'Vikram'],
    'Productivity': [78, 85, 65, 92, 88]
}

df = pd.DataFrame(data)
df


# %%
min_productivity = df['Productivity'].min()
print(f"Min productivity is {min_productivity}")

# %%
max_productivity = df['Productivity'].max()
print(f"Max productivity is {max_productivity}")

# %%
avg_prod = df['Productivity'].mean()
print(f"The average productivity is {avg_prod}")

# %%
max_employee = df.loc[df['Productivity'].idxmax(),'Employee']
print(f"The employee with maximum sales is {max_employee}")

# %%
# Sort the employees in descending order of productivity.

sorted_df = df.sort_values(by="Productivity", ascending=False)
print(sorted_df)

# %%
import pandas as pd

# %%

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Region': ['North', 'North', 'East', 'South', 'West', 'East', 'South', 'North', 'West', 'South'],
    'Sales': [12000, 15000, 9000, 18000, 16000, 11000, 14000, 9500, 17000, 15500]
}

df = pd.DataFrame(data)

# %%
df

# %%
#Q - 

"""
Group the data by Region and calculate the total sales per region.
Find the average sales per region.
Identify the region with the highest total sales.
"""

# %%
sales_by_region = df.groupby('Region')['Sales'].sum()
print(sales_by_region)

# %%
avg_sales_per_reg = df.groupby('Region')['Sales'].mean()
print(f"The average sales per region is {avg_sales_per_reg}")

# %%
# Identify the region with the highest total sales.


sales_by_region = pd.DataFrame(sales_by_region)
sales_by_region.columns = ['Sales']
sales_by_region

# %%
highest_sales_reg = sales_by_region.idxmax()
print(f"The region with the highest sales: {highest_sales_reg}")

# %%
#Q

data = {
    'Department':['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Score':[75, 88, 82, 90, 68, 79, 85, 72]
}

df = pd.DataFrame(data)
df

# %%
"""
Calculate the total score per department.

Find the average score per department.

Identify the department with the highest total score.

"""

# %%
total_score_per_dept = df.groupby('Department')['Score'].sum()
print("The total score per department:\n", total_score_per_dept)

# %%
avg_score_per_dept = df.groupby('Department')['Score'].mean()
print("The average score is:\n", avg_score_per_dept)

# %%
## Identify the department with the highest total score.

df.head(2)

# %%
total_score_per_dept.idxmax()

# %%
data = {
    'Employee': ['John', 'Sara', 'Mike', 'Lara', 'Alex', 'Nina', 'Tom', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Hours_Worked': [38, 45, 40, 50, 42, 36, 48, 44]
}

df = pd.DataFrame(data)

# %%
dept_stats = df.groupby('Department')['Hours_Worked'].agg(['sum', 'mean', 'min', 'max'])
print(dept_stats)


# %%
data = {
    'Student': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Harsh'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Score': [88, 92, 75, 85, 90, 78, 95, 80]
}

df = pd.DataFrame(data)

# %%
# Q - Group by Subject and calculate: sum, mean, min, max.
# Add a new column indicating whether the average score is above 85.

# %%
sub_agg = df.groupby('Subject')['Score'].agg(['sum','mean','min','max'])
sub_agg

# %%
sub_agg['sc_greater_than_85'] = sub_agg['mean']>85
sub_agg

# %%
#Q - 

data = {
    'Employee': ['John', 'Sara', 'Mike', 'Lara', 'Alex', 'Nina', 'Tom', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Score': [78, 90, 85, 92, 88, 80, 83, 89]
}

df = pd.DataFrame(data)

# %%
# Q - 

"""
Find the best-performing employee in each department.
Return a DataFrame with only the top performer per department.
"""

# %%
df.head(2)

# %%
idx = df.groupby('Department')['Score'].idxmax()
idx

# %%
df_names = df.loc[idx]
df_names

# %%
data = {
    'Rep': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Harsh'],
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West', 'West'],
    'Revenue': [50000, 60000, 55000, 70000, 65000, 62000, 58000, 59000]
}

df = pd.DataFrame(data)

# %%
#Q - 
"""
Find the top-performing rep in each region (highest revenue).
Return only the rows for those top performers.
"""

# %%
top_rep_id = df.groupby('Region')['Revenue'].idxmax()
top_rep = df.loc[top_rep_id]
top_rep

# %%
## Q  --

data = {
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Department': ['HR', 'HR', 'HR', 'IT', 'IT', 'IT', 'Finance', 'Finance', 'Finance', 'Finance'],
    'Score': [75, 82, 90, 88, 92, 85, 70, 78, 88, 95]
}

df = pd.DataFrame(data)

#Get the top 2 employees in each department based on Score.

# %%
top2_per_dept = df.groupby('Department').apply(lambda x:x.nlargest(2,'Score')).reset_index(drop = True)
top2_per_dept

# %%
data = {
    'Player': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    'Team': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Points': [50, 65, 60, 75, 80, 70, 55, 68]
}

df = pd.DataFrame(data)

# Q - Get the top 2 players in each team based on Points

# %%
top2_players = df.groupby('Team').apply(lambda x:x.nlargest(2,'Points')).reset_index(drop=True)
top2_players

# %%
"""
For each subject, calculate the range of marks using a groupby + lambda.
Create a new column 'Result_Category':
Excellent if Marks ≥ 90
Good if 75 ≤ Marks < 90
Needs Improvement if Marks < 75
"""

data = {
    'Student': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Harsh'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [78, 92, 85, 88, 60, 90, 95, 70]
}

df = pd.DataFrame(data)

# %%
range_per_sub = df.groupby('Subject')['Marks'].apply(lambda x:x.max()-x.min())

# %%
range_per_sub

# %%
df.head()

# %%
df['Performance Level'] = df['Marks'].apply(lambda x:'Excellent' if x>=90
                                            else 'Good' if x>=75
                                            else 'Needs Improvement')

df = df.drop('Performanc_level', axis=1)

# %%
df

# %%
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Class': ['10A', '10A', '10A', '10B', '10B', '10B', '10A', '10B'],
    'Subject': ['Math', 'Science', 'Math', 'Math', 'Science', 'Math', 'Science', 'Science'],
    'Marks': [85, 90, 78, 88, 82, 91, 87, 89]
}

df = pd.DataFrame(data)

#Q - Group by Class and Subject to calculate sum and mean of Marks.
# Find the Class-Subject pair with the highest average score.

# %%
df.head()

# %%
grouped = df.groupby(['Class','Subject'])['Marks'].agg(['sum','mean'])
grouped

# %%
max_mean = grouped['mean'].idxmax()
max_mean

# %%
#Q - 

data = {
    'Student': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science'],
    'Marks': [88, 92, 85, 90, 75, 89]
}

df = pd.DataFrame(data)

# Rank students within each subject based on Marks (higher = rank 1).
# Add this rank in a column called 'Rank_in_Subject'.

# %%
df['rank'] = df.groupby('Subject')['Marks'].rank(ascending = False,method = 'dense')
df

# %%
data = {
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Sales': [50000, 42000, 60000, 58000, 45000, 49000, 62000, 47000]
}

df = pd.DataFrame(data)

#Q - Create a pivot table showing total Sales per Region per Department 
# (Region as rows, Department as columns).
# Add average Sales in the same pivot table.

# %%
pivot = pd.pivot_table(
    df,
    values = 'Sales',
    index = 'Region',
    columns = 'Department',
    aggfunc = ['sum','mean']
)   

print(pivot)

# %%
data = {
    'Student': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Harsh'],
    'Class': ['10A', '10A', '10B', '10B', '10A', '10B', '10A', '10B'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Science', 'Math', 'Math', 'Science'],
    'Marks': [85, 90, 88, 82, 75, 91, 79, 87]
}

df = pd.DataFrame(data)

"""
Create a pivot table with:

Rows: Class

Columns: Subject

Values: Marks

Aggregations: sum and mean

"""

# %%
pivot = pd.pivot_table(
    df,
    values = 'Marks',
    index = 'Class',
    columns = 'Subject',
    aggfunc = ['sum','mean']
)

print(pivot)

# %%
import pandas as pd

data = {
    'Rep': ['Aman', 'Bhavya', 'Chirag', 'Divya', 'Esha', 'Farhan', 'Gauri', 'Harsh', 'Isha', 'Jay'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Clothing', 'Clothing', 'Furniture', 'Electronics', 'Clothing', 'Furniture', 'Electronics'],
    'Sales': [50000, 42000, 60000, 38000, 45000, 52000, 61000, 40000, 48000, 70000]
}

df = pd.DataFrame(data)


# %%
df.head()

# %%
#Q - Find total and average sales per region

sales_grouped = df.groupby('Region')['Sales'].agg(['sum','mean'])
sales_grouped

# %%
#Q - Find total & average sales per region-category combo

sales_grouped_category = df.groupby(['Region','Category'])['Sales'].agg(['sum','mean'])
sales_grouped_category

# %%
#Q- Identify the top-performing category in each region

df.head()

# %%
top_cat_data = pd.DataFrame(df.groupby(['Region','Category'])['Sales'].sum())

top_cat_data


# %%
top_category_each_region = top_cat_data.groupby(level=0).idxmax()
print(top_category_each_region)

# %%
top_category_each_region = top_category_each_region.apply(lambda x: x[1])
print(top_category_each_region)


# %%
# Find the top 2 sales reps per category

df.head(2)

# %%
df['rank by category'] = df.groupby('Category')['Sales'].rank(ascending = False,method='dense')
df

# %%
df.head(2)

# %%
df[df['rank by category']<=2]

# %%
top2_reps = df.groupby('Category').apply(lambda x:x.nlargest(2,'Sales')).reset_index(drop = True)
top2_reps

# %%
df.head(2)

# %%
df.groupby('Region')['Sales'].rank(ascending=False, method='dense')

# %%
df.head(2)

# %%
pivot = pd.pivot_table(
    df,
    values = 'Sales',
    index = 'Region',
    columns = 'Category',
    aggfunc = ['sum','mean']
    )

print(pivot)

# %%
df['performance_tier'] = df['Sales'].apply(lambda x:'High' if x>=60000
                                                else 'Medium' if x>=45000
                                                else 'Low')

# %%
df

# %%



