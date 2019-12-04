import pandas as pd
import matplotlib.pyplot as plt

b = pd.read_csv('https://github.com/siddarthkrishna10/Optimisation_Project_Python/blob/master/Part%20I/Mean_Table.csv')
b.plot(x='Season', y='Average Difference')
plt.title('The Average Difference Over All Seasons')
plt.xlabel('Season')
plt.ylabel('Average Difference')
plt.show()
