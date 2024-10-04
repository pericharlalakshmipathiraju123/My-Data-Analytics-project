#lets import the required libraries first
import pandas as pd

# Loading the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Displaying the first few rows of the dataset
print(df.head())

# Displaying data types of each column so we can make required changes for the datatypes
print(df.dtypes)

#the order_date, ship_date, and sales columns need attention. Let's go through the necessary steps to clean and prepare your dataset for analysis.
#Since order_date is currently an object type, convert it to datetime format. The same applies to the ship_date.
# Convert 'order_date' and 'ship_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], format='%m/%d/%Y', errors='coerce')

# Check for any conversion errors
print(df['order_date'].isnull().sum())  # Number of NaT values in 'Order Date'
print(df['ship_date'].isnull().sum())   # Number of NaT values in 'Ship Date'
print(df.dtypes)

#we saw the order date and shipdate were now hanged to datetime and now lets make some more required changes

#sales columnn in also in object fprmat so we need to change that to numeric type 
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

print(df.dtypes)
# nowthat we changed the object to numeric so kets check for any conversional errors
print(df['sales'].isnull().sum())  # Number of NaN values in 'Sales'

#we found 2630 errors here when converting the data type so we should fix them now
# Check unique values in the 'Sales' column to identify potential issues
print(df['sales'].unique())
# Convert 'Sales' to numeric, coercing errors to NaN
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# Check for any NaN values in 'Sales' after conversion
print("NaN values in 'sales':", df['sales'].isnull().sum())

# Display rows where Sales is NaN
problematic_sales = df[df['sales'].isnull()]
print("Problematic_sales_Entries:")
print(problematic_sales[['sales']])  # Display only the 'Sales' column

# Convert 'Sales' to string first (this handles NaN as well)
df['sales'] = df['sales'].astype(str)

# Now you can safely strip whitespace
df['sales'] = df['sales'].str.strip()

# Remove currency symbols and commas
df['sales'] = df['sales'].replace({'\$': '', ',': ''}, regex=True)
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
print("NaN values in 'sales' after conversion:", df['sales'].isnull().sum())

# Load the dataset again if needed
df = pd.read_csv('SuperStoreOrders.csv')

# Convert 'Sales' to string and strip whitespace
df['sales'] = df['sales'].astype(str).str.strip()

# Check unique values that couldn't be converted to numeric
problematic_sales = df[pd.to_numeric(df['sales'], errors='coerce').isnull()]
print("Problematic_Sale_Entries:")
print(problematic_sales[['sales']])  # Display problematic entries

# Remove any unwanted characters (for example, letters)
df['sales'] = df['sales'].replace({'[^0-9.]': ''}, regex=True)

df['sales'] = df['sales'].replace({'\$': '', ',': ''}, regex=True)

df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# Check for NaN values after conversion
print("NaN values in 'sales' after conversion:", df['sales'].isnull().sum())

print(df.describe())

print(df.dtypes)  # Check the data types of all columns

# Convert 'Order Date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

print(df['order_date'].isnull().sum())  # Check for NaT (not-a-time) values
print(df.dtypes)  # Check the data types again

# Check the data types
print(df.dtypes)  # This will show the data types of all columns

# Convert 'Sales' to numeric, coercing errors to NaN
df['sales'] = pd.to_numeric(df['sales'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')

# Check for any NaN values in 'Sales'
print("NaN values in 'sales':", df['sales'].isnull().sum())



import pandas as pd

# Load the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Display the first few rows and check column names
print(df.head())
print(df.columns)  # Print column names
print(df.dtypes)   # Print data types

print("NaN values in 'sales':", df['sales'].isnull().sum())

# Check if 'Order Date' is of datetime type
if not pd.api.types.is_datetime64_any_dtype(df['order_date']):
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Now group sales by month and sum them
sales_over_time = df.groupby(df['order_date'].dt.to_period('M'))['sales'].sum()



import pandas as pd

# Load the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Display the first few rows and check column names and data types
print(df.head())
print(df.columns)  # Print column names
print(df.dtypes)   # Print data types

# Convert 'Order Date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Check for NaT (not-a-time) values in 'Order Date'
print("NaT values in 'order_date':", df['order_date'].isnull().sum())

# Clean 'Sales' column and convert to numeric
df['sales'] = pd.to_numeric(df['sales'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')

# Check for any NaN values in 'Sales' after conversion
print("NaN values in 'sales':", df['sales'].isnull().sum())

# Check if 'Sales' is of numeric type
print("Data type of 'sales':", df['sales'].dtype)



# Group by product_name and sum sales
top_products = df.groupby('product_name')['sales'].sum().nlargest(10)

# Group by product_name and sum only numeric columns
numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
top_products = df.groupby('product_name')['sales'].sum().nlargest(10)

import pandas as pd

# Load the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Display the first few rows and check column names and data types
print(df.head())
print(df.columns)  # Print column names
print(df.dtypes)   # Print data types

# Convert 'Order Date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Check for NaT (not-a-time) values in 'Order Date'
print("NaT values in 'order_date':", df['order_date'].isnull().sum())

# Clean 'Sales' column and convert to numeric
df['sales'] = pd.to_numeric(df['sales'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')

# Check for any NaN values in 'Sales' after conversion
print("NaN values in 'sales':", df['sales'].isnull().sum())

# Check if 'Sales' is of numeric type
print("Data type of 'sales':", df['sales'].dtype)

# Ensure there are no datetime types in the 'Sales' or any other relevant columns
# Group by product_name and sum sales
top_products = df.groupby('product_name')['sales'].sum().nlargest(10)

import pandas as pd
import matplotlib.pyplot as plt  # Make sure this line is included
import seaborn as sns  # For additional plotting options

# Load the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Clean 'sales' column and convert to numeric
df['sales'] = pd.to_numeric(df['sales'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')

# Plotting sales by region (ensure 'region' exists in your data)
plt.figure(figsize=(10, 5))  # Create a figure
sns.barplot(x='region', y='sales', data=df)  # Create a bar plot
plt.title('sales_by_region')  # Add title
plt.ylabel('sales')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout to fit labels
plt.show()  # Display the plot


import pandas as pd
import matplotlib.pyplot as plt  # Make sure this line is included
import seaborn as sns  # For additional plotting options

# Load the dataset
df = pd.read_csv('SuperStoreOrders.csv')

# Clean 'Sales' column and convert to numeric
df['sales'] = pd.to_numeric(df['sales'].replace({'\$': '', ',': ''}, regex=True), errors='coerce')

# Plotting sales by region (ensure 'Region' exists in your data)
plt.figure(figsize=(10, 5))  # Create a figure
sns.barplot(x='region', y='sales', data=df)  # Create a bar plot
plt.title('sales by Region')  # Add title
plt.ylabel('sales')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout to fit labels
plt.show()  # Display the plot
