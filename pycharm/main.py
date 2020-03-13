from sections import *

import pandas as pd
import matplotlib.pyplot as plt

crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')

crime['Year'] = crime['Year'].apply(generate_customer_stage)

crime = crime[crime['CrimeType']=='All recorded offences']

crime.plot(x='Year')

# crime.plot(x='Year', y='Harrow')
# crime.plot(x='Year', y='Bexley')

plt.show()

# plotToShow = loginsPerDayOfWeek.plot(x='DayOfWeek', y = 'NumberOfLogins')
# plotToShow.set_xlabel('Day of Week')
# plotToShow.set_ylabel('Number of Logins')
#
# plt.show()