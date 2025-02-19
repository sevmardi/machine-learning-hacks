import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data.csv')
X = dataset.iloc(:, :-1).values
y = dataset.iloc(:, :3).values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = Imputer.fit(X[:, 1:3])

X[:, 1:3] = imputer.transform(X[:, 1:3])

