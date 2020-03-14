import datetime

import pandas as pd

def calc_on_consecutive_elements_in_column(data_frame, column_name, function_to_perform, initial_value):
    """
    Given a column in a dataframe, performs a running calculation between subsequent elements in that column
    and adds a new column with the result of this calculation
    (eg. Calculating percentage change)
    Parameters:
        data_frame (DataFrame): The data frame
        column_name (string): The name of the column on which to perform the action
        function_to_perform (lambda pair: <something>): The running calculation. A lambda with an input tuple and output object
        initial_value (object): The value of the first element in the resulting column
    Returns: The calculated column
    """

    # (pair[1] - pair[0]) / pair[0]

    per = map(lambda pair: function_to_perform(pair), zip(data_frame[column_name], data_frame[column_name][1:]))

    return pd.Series([initial_value]).append(pd.Series(per)).reset_index(drop=True)

def convert_date_string_to_date(dateString):
    """
    Convert a year string like ('2008-09') to a date object
     Parameters:
        dateString(string): The date string
    """

    swticher = {
        '1999-00': datetime.datetime(1999, 1, 1),
        '2000-01': datetime.datetime(2000, 1, 1),
        '2001-02': datetime.datetime(2001, 1, 1),
        '2002-03': datetime.datetime(2002, 1, 1),
        '2003-04': datetime.datetime(2003, 1, 1),
        '2004-05': datetime.datetime(2004, 1, 1),
        '2005-06': datetime.datetime(2005, 1, 1),
        '2006-07': datetime.datetime(2006, 1, 1),
        '2007-08': datetime.datetime(2007, 1, 1),
        '2008-09': datetime.datetime(2008, 1, 1),
        '2009-10': datetime.datetime(2009, 1, 1),
        '2010-11': datetime.datetime(2010, 1, 1),
        '2011-12': datetime.datetime(2011, 1, 1),
        '2012-13': datetime.datetime(2012, 1, 1),
        '2013-14': datetime.datetime(2013, 1, 1),
        '2014-15': datetime.datetime(2014, 1, 1),
        '2015-16': datetime.datetime(2015, 1, 1),
        '2016-17': datetime.datetime(2016, 1, 1),
    }

    return swticher.get(dateString)

def whats(thing) :
    """
    Prints the type of object passed in
    Parameters:
        thing (Object): The object for which the type needs to be printed
    """

    print(type(thing))