import datetime

def generate_customer_stage(dateString):
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