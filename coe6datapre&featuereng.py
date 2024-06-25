# Import libraries and load the dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('"D:\titanic.csv"')
# Analyze the dataset

# Display the first few rows of the dataset
data.head()
# Get the summary of the dataset
data.info()

# Fill missing values
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Feature engineering

# Create new features
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

# Categorical features encoding

data = pd.get_dummies(data, columns=['Embarked', 'Sex'], drop_first=True)

# Drop unnecessary columns

data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId', 'SibSp', 'Parch'], axis=1, inplace=True)

# Visualize the results

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()

# Create a simple unit test to check if the number of columns in the preprocessed dataset matches the expected value

def test_preprocessed_data_columns():
    expected_columns = ['Survived', 'Pclass', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S', 'Sex_male']
    assert len(data.columns) == len(expected_columns), f"Expected {len(expected_columns)} columns, but got {len(data.columns)}"
    assert set(data.columns) == set(expected_columns), f"Expected columns {expected_columns}, but got {list(data.columns)}"

    return "All tests passed."

# Call the test function and print the result
print(test_preprocessed_data_columns())






