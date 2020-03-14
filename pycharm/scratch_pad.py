import pandas as pd

from util import *

crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')
crime['Year'] = crime['Year'].apply(convert_date_string_to_date)
crime['London'] = crime['Inner London'] + crime['Outer London']

crime_segments = pd.DataFrame({
    'Year': crime['Year'].unique()
}, columns=['Year'])

all = crime_segments['All Crime'] = crime[crime['CrimeType']=='All recorded offences']['London'][0]

print(all)

