import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
# Load data from CSV
data = pd.read_csv('cluster_task1.csv')
X = data[['X0', 'X1']]
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_pred = kmeans.predict(X)
# Visualize the cluster result
plt.scatter(X['X0'], X['X1'], c=y_pred, cmap='viridis')
plt.xlabel('X0')
plt.ylabel('X1')
plt.title('K-means clustering')
plt.show()
ch_score = metrics.calinski_harabasz_score(X, y_pred)
print("Calinski-Harabasz Score:", ch_score)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_pred = kmeans.predict(X)
# Visualize the cluster result
plt.scatter(X['X0'], X['X1'], c=y_pred, cmap='viridis')
plt.xlabel('X0')
plt.ylabel('X1')
plt.title('K-means clustering')
plt.show()
ch_score = metrics.calinski_harabasz_score(X, y_pred)
print("Calinski-Harabasz Score:", ch_score)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_pred = kmeans.predict(X)
# Visualize the cluster result
plt.scatter(X['X0'], X['X1'], c=y_pred, cmap='viridis')
plt.xlabel('X0')
plt.ylabel('X1')
plt.title('K-means clustering')
plt.show()
ch_score = metrics.calinski_harabasz_score(X, y_pred)
print("Calinski-Harabasz Score:", ch_score)
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_pred = kmeans.predict(X)
# Visualize the cluster result
plt.scatter(X['X0'], X['X1'], c=y_pred, cmap='viridis')
plt.xlabel('X0')
plt.ylabel('X1')
plt.title('K-means clustering')
plt.show()
ch_score = metrics.calinski_harabasz_score(X, y_pred)
print("Calinski-Harabasz Score:", ch_score)