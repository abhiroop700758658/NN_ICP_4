import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# a. Import the given “Salary_Data.csv”
df = pd.read_csv('C:\\Users\\Harshini\\Documents\\Python Codes\\ICP-4\\Salary_Data.csv')

# b. Split the data into train and test partitions
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)

# c. Train and predict the model
model = LinearRegression()
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# d. Calculate the mean_squared error
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

print(f"Mean Squared Error (Train): {mse_train}")
print(f"Mean Squared Error (Test): {mse_test}")

# e. Visualize both train and test data using scatter plot
plt.scatter(X_train, y_train, label='Train Data', color='blue')
plt.scatter(X_test, y_test, label='Test Data', color='red')
plt.plot(X_train, y_train_pred, label='Linear Regression (Train)', color='green')
plt.plot(X_test, y_test_pred, label='Linear Regression (Test)', color='orange')
plt.title('Linear Regression - Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
