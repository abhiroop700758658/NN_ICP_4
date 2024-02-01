**code execution link:**


**1. Data Manipulation Program**

**Read the CSV file:**
The code reads a CSV file named 'data.csv' using the pd.read_csv function from the pandas library. The file path is specified as 'C:\Users\Harshini\Documents\Python Codes\ICP-4\data.csv'. Make sure to replace this path with the actual location of your CSV file.

**Show Basic Statistical Description:**
The describe() method is used to generate basic statistical information (count, mean, std, min, 25%, 50%, 75%, max) about the numerical columns in the DataFrame. The results are stored in the basic_stats variable and printed to the console.

**Check for Null Values:**
The isnull() method checks for missing values in each column, and sum() is then applied to count the number of null values in each column. The results are stored in the null_values variable and printed to the console.

**Replace Null Values with the Mean:**
Missing values in the DataFrame (df) are replaced with the mean value of each column using the fillna() method. The changes are made in place.

**Aggregate Two Columns:**
The 'Duration' and 'Calories' columns are selected, and the agg() method is used to aggregate statistics (min, max, count, mean) for these columns. The results are stored in the aggregated_data variable and printed to the console.

**Filter DataFrame Based on Calories Range:**
Rows in the DataFrame are filtered to select those with 'Calories' values between 500 and 1000 (inclusive). The resulting DataFrame is stored in the filtered_df_1 variable.

**Filter DataFrame Based on Calories and Pulse Conditions:**
Rows in the DataFrame are filtered to select those with 'Calories' greater than 500 and 'Pulse' less than 100. The resulting DataFrame is stored in the filtered_df_2 variable.

**Create a New DataFrame Without 'Maxpulse':**
A new DataFrame named df_modified is created by dropping the 'Maxpulse' column from the original DataFrame (df).

**Delete 'Maxpulse' Column from the Original DataFrame:**
The 'Maxpulse' column is removed from the original DataFrame (df) in place.

**Convert Datatype of Calories Column to Integer:**
The 'Calories' column in the DataFrame (df) is converted to an integer data type using the astype(int) method.
Scatter Plot for 'Duration' and 'Calories':
A scatter plot is created using Matplotlib, with 'Duration' on the x-axis and 'Calories' on the y-axis. The title and axis labels are added, and the plot is displayed using plt.show().
This code snippet performs various data manipulation and analysis tasks, including handling missing values, filtering data, and creating a scatter plot for visualization.

**2. Regression Program**
   
**Import Libraries:**
Import necessary libraries: pandas for data manipulation, matplotlib.pyplot for plotting, and relevant modules from scikit-learn for machine learning.

**Import Dataset:**
Read the "Salary_Data.csv" file into a DataFrame (df) using the pd.read_csv function. The file path is specified as 'C:\Users\Harshini\Documents\Python Codes\ICP-4\Salary_Data.csv'. Adjust this path to your file location.

**Split the Data:**
Split the dataset into independent variable (X - 'YearsExperience') and dependent variable (y - 'Salary') using the train_test_split function. The training set comprises 2/3 of the data, and the random state is set to 42 for reproducibility.

**Train and Predict the Model:**
Create a linear regression model using LinearRegression() from scikit-learn, and fit it to the training data (X_train, y_train). Predict the salary values for both the training and test sets.

**Calculate Mean Squared Error:**
Calculate the mean squared error for both the training and test sets using the mean_squared_error function from scikit-learn.

**Visualize Train and Test Data:**
Create a scatter plot to visualize both the training and test data points. The linear regression line for both sets is overlaid on the plot. The plot includes legends, labels, and a title for better interpretation.

**Show the Plot:**
Display the scatter plot with linear regression lines using plt.show().
This code provides a comprehensive example of training a linear regression model, evaluating its performance using mean squared error, and visualizing the results on both the training and test datasets.




