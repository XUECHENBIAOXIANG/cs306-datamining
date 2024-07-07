import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Step 1: Load data from csv files
data = pd.read_csv("iris.csv")

# x为不包括最后一列
# y为最后一列
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
# Step 4: Build a Decision Tree model based on scikit-learn
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()

# Step 5: Fit the model
clf.fit(X_train, y_train)

# Step 6: Visualization
plt.figure(figsize=(12,12))
plot_tree(clf, fontsize=10)
plt.show()