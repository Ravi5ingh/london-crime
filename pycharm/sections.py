from util import *
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def plot_crime_segments():

    crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')
    crime['Year'] = crime['Year'].apply(convert_date_string_to_date)
    crime['London'] = crime['Inner London'] + crime['Outer London']

    crime_segments = pd.DataFrame({
        'Year': crime['Year'].unique()
    }, columns=['Year'])

    crime_segments['Year'] = crime_segments['Year'].apply(lambda x: x.strftime("%Y"))

    # crime_segments['All Crime'] = crime[crime['CrimeType'] == 'All recorded offences']['London']
    crime_segments['Violence Against the Person'] = list(crime[crime['CrimeType'] == 'Violence Against the Person']['London'])
    crime_segments['Sexual Offences'] = list(crime[crime['CrimeType'] == 'Sexual Offences']['London'])
    crime_segments['Robbery'] = list(crime[crime['CrimeType'] == 'Robbery']['London'])
    crime_segments['Burglary'] = list(crime[crime['CrimeType'] == 'Burglary']['London'])
    crime_segments['Theft and Handling'] = list(crime[crime['CrimeType'] == 'Theft and Handling']['London'])
    crime_segments['Fraud or Forgery'] = list(crime[crime['CrimeType'] == 'Fraud or Forgery']['London'])
    crime_segments['Criminal Damage'] = list(crime[crime['CrimeType'] == 'Criminal Damage']['London'])
    crime_segments['Drugs'] = list(crime[crime['CrimeType'] == 'Drugs']['London'])
    crime_segments['Other Notifiables'] = list(crime[crime['CrimeType'] == 'Other Notifiable Offences']['London'])

    plot = crime_segments.plot.bar(x='Year', stacked=True)
    plot.set_ylabel('Number of offences')

    plt.show()

def plot_crime_by_type():
    """
    Plots crime in all boroughs by by type
    """
    crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')
    crime['Year'] = crime['Year'].apply(convert_date_string_to_date)
    crime['London'] = crime['Inner London'] + crime['Outer London']

    crime_by_type = pd.DataFrame({
        'Year': crime['Year'].unique()
    }, columns=['Year'])

    defaultFractionChange = 0

    crime_by_type['Violence Against the Person'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Violence Against the Person'], 'London', lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Sexual Offences'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Sexual Offences'], 'London', lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Robbery'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Robbery'], 'London', lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Burglary'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Burglary'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Theft and Handling'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Theft and Handling'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Fraud or Forgery'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Fraud or Forgery'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Criminal Damage'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Criminal Damage'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Drugs'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Drugs'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)
    crime_by_type['Other Notifiables'] = 100 * calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'Other Notifiable Offences'], 'London',lambda pair: (pair[1] - pair[0]) / pair[0], defaultFractionChange)

    plot = crime_by_type.plot(x='Year')
    plot.set_ylabel('Percentage change in offences')

    plt.show()

def plot_crime_by_borough():
    """
    Plots all crime in london by borough
    """

    crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')
    crime['Year'] = crime['Year'].apply(convert_date_string_to_date)

    crime = crime[crime['CrimeType'] == 'All recorded offences']

    plot = crime.plot(x='Year')
    plot.set_ylabel('Number of Recorded Crimes')

    plt.show()