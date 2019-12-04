import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

c = pd.read_csv('https://github.com/siddarthkrishna10/Optimisation_Project_Python/blob/master/Part%20II/Transfers.csv')

c1 = c.dropna()

X = c1['Transfer_fee'].values.reshape(-1, 1)
y = c1['Market_value'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

cx = LinearRegression()
cx.fit(X_train, y_train)
print('Intercept:', cx.intercept_)
print('Coefficient:', cx.coef_)

y_pred = cx.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df.to_csv('Actual_Predicted.csv')

plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

mean = c1["Market_value"].mean()
print('Mean of Market Value:', mean)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
