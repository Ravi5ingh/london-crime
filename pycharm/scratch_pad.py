import pandas as pd

from util import *

crime = pd.read_csv('D:/Ravi/Documents/Udacity/Pipelines/london-crime/pycharm/data/LondonCrime.csv')
crime['Year'] = crime['Year'].apply(convert_date_string_to_date)
crime['London'] = crime['Inner London'] + crime['Outer London']

# new_crime = pd.DataFrame(crime['Year'].unique())
new_crime = pd.DataFrame({
    'Year': crime['Year'].unique()
}, columns=['Year'])

new_crime['All Crimes'] = calc_on_consecutive_elements_in_column(crime[crime['CrimeType'] == 'All recorded offences'], 'London', lambda pair: (pair[1]-pair[0])/pair[0], 1)

print(new_crime)

# allCrime = pd.DataFrame(crime[crime['CrimeType'] == 'All recorded offences'])
# func = lambda pair: (pair[1]-pair[0])/pair[0]
#
# per = map(lambda pair: (pair[1]-pair[0])/pair[0], zip(allCrime['London'], allCrime['London'][1:]))
#
# newcol = pd.Series([1]).append(pd.Series(per)).reset_index(drop=True)
#
# print(new_crime)

# new_crime['AllCrime'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1, 1]#newcol # pd.Series([1]).append(pd.Series(per)).reset_index(drop=True)

# print(new_crime)


# data = {
#     'Value': [12, 34, 12, 54, 23, 65, 23, 56, 23]
# }
#
# vals = pd.DataFrame(data, columns=['Value'])
#
# # print(vals)
#
#
# # for previous, current in zip(vals['Value'], vals['Value'][1:]):
# #     print(previous, current)
#
# # per = zip(vals['Value'], vals['Value'][1:]).apply(lambda prev, curr: (curr-prev)/prev)
#
# per = map(lambda pair: (pair[1]-pair[0])/pair[0], zip(vals['Value'], vals['Value'][1:]))
#
# vals['Per'] = pd.Series([1]).append(pd.Series(per)).reset_index(drop=True)
#
# print(vals)

