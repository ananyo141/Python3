# WAP to convert hours to seconds
from hours_to_min import convert_to_min

def convert_to_sec(in_hours):
    '''(num)-->num
Convert the given in_hours to seconds.
>>>convert_to_sec(5)
18000
>>>convert_to_sec(7)
25200
'''
    min= convert_to_min(in_hours)
    sec= min*60
    return sec
