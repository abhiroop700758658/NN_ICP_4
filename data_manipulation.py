import pandas as pd
import matplotlib.pyplot as plt
# a. Read the CSV file
df = pd.read_csv('C:\\Users\\Harshini\\Documents\\Python Codes\\ICP-4\\data.csv')

# b. Show the basic statistical description about the data
basic_stats = df.describe()
print("Basic Statistical Description:")
print(basic_stats)

# c. Check if the data has null values
null_values = df.isnull().sum()
print("\nNull Values:")
print(null_values)

# d. Replace the null values with the mean
df.fillna(df.mean(), inplace=True)

# e. Select at least two columns and aggregate the data using: min, max, count, mean
selected_columns = ['Duration', 'Calories']
aggregated_data = df[selected_columns].agg(['min', 'max', 'count', 'mean'])
print("\nAggregated Data:")
print(aggregated_data)

# f. Filter the dataframe to select the rows with calories values between 500 and 1000
filtered_df_1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

# g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100
filtered_df_2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# h. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified = df.drop(columns=['Maxpulse'])

# i. Delete the “Maxpulse” column from the main df dataframe
df.drop(columns=['Maxpulse'], inplace=True)

# j. Convert the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)

# k. Using pandas create a scatter plot for the two columns (Duration and Calories)
df.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')

# Show the plots
plt.show()
