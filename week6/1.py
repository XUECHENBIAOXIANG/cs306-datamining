import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load data from csv files
data = pd.read_csv("iris.csv")

# x为不包括最后一列
# y为最后一列
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


# Step 4: Build a KNN model based on scikit-learn. (e.g., k = 1~12)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Fit the model
train_accuracy = []
test_accuracy = []
neighbors = range(1, 13)

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    train_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test, y_test))

# Step 6: Compute accuracy on the training set and test set
plt.plot(neighbors, train_accuracy, label='Training accuracy')
plt.plot(neighbors, test_accuracy, label='Test accuracy')
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Step 7: Generate a plot of accuracy to choose a good value of k

# Step 8: Setup a KNN classifier with k neighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Step 9: Fit the model and get the accuracy of the test set
knn.fit(X_train, y_train)
test_accuracy_k3 = knn.score(X_test, y_test)
print("Accuracy with k=3:", test_accuracy_k3)
