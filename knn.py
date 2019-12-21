"""
@author: Francisco Pascual
Modified by: Lucía Calzado
"""

import pandas as panda
import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix


mental_health = panda.read_csv(r'C:\Users\lucia\OneDrive\Escritorio\datasetUsable.csv')
mental_health.head()

# features and labels
features = list(mental_health.columns.values)
features.remove('label')

X = mental_health[features]
y = mental_health['label']

# x axis for plotting
xx = np.stack(i for i in range(len(y)))

# 1. CROSS VALIDATION ANALYSIS
for i, weights in enumerate(['uniform', 'distance']):
    total_scores = []
    for n_neighbors in range(1,30):
        knn = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        knn.fit(X,y)
        scores = cross_val_score(knn, X, y, cv=10)
        total_scores.append(scores.mean())

    plt.plot(range(0,len(total_scores)), total_scores, marker='o', label=weights)
    plt.ylabel('cv score')

plt.legend()
plt.show()


#1. Build the model
n_neighbors = 11 # BEST PARAMETER
knn = neighbors.KNeighborsClassifier(n_neighbors, weights="distance")

#divide database features into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

#train model
knn.fit(X_train, y_train)

#predecir valores del test
y_pred = knn.predict(X_test)

#confusion matrix
confusion_matrix(y_test, y_pred, labels = [0, 1])