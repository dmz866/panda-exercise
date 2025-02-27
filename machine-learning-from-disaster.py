import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import tree
#plot_confusion_matrix
df = pd.read_csv('test_files/DataSet_Titanic.csv')

x = df.drop('Sobreviviente', axis = 1) #1 is column, 0 is row

y = df.Sobreviviente

tree1 = DecisionTreeClassifier(max_depth = 2, random_state = 42)
tree1.fit(x, y)

pred_y = tree1.predict(x)

print(f'Precision: {accuracy_score(pred_y, y)}')

confusion_matrix(y, pred_y)

#plot_confusion_matrix(tree1, x, y, cmap = plt.cm.Blues, values_format = '.0f')

