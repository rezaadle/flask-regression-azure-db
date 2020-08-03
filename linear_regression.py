#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

df = pd.read_csv("Salary_Data.csv")
X = df.iloc[:, [0]]
y = df.iloc[:, -1]

linreg = LinearRegression()
linreg.fit(X, y)

print(linreg.score(X, y))
#linreg.predict(new_data)

dump(linreg, "linear_regression_model.joblib")
