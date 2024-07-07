#Implementing DBSCAN with Scikit-Learn
#1. Load data from csv files. 2. Data cleaning. 3. Get features. 4. Build a DBSCAN model with scikit-learn.
#5. Fit the model. 6. Visualization. 7. Evaluation.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
# Step 1: Load data from csv files
data = pd.read_csv("DBSCAN_TASK1.csv")
# Step 2: Data cleaning
# Step 3: Get features
X = data[['x0', 'x1']]
# Step 4: Build a DBSCAN model with scikit-learn
dbscan = DBSCAN(eps=0.1, min_samples=20)
# Step 5: Fit the model
y_pred = dbscan.fit_predict(X)
# Step 6: Visualization
plt.scatter(X['x0'], X['x1'], c=y_pred, cmap='viridis')
plt.xlabel('x0')
plt.ylabel('x1')
plt.title('DBSCAN clustering')
plt.show()
