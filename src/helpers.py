import re

def make_pythonic(name):
    '''
    Turns camel case into snake case and lowers it. 
    It also removes all whitespaces to get it in true pythonic form. 
    '''
    # get rid of spaces
    name = name.replace(' ', '')
    # isolate capitals from lower cases using regex
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # make all lower case
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    return name