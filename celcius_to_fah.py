#  WAP to convert celcius to fahrenheit

def cel_to_fah(temp_c):
    '''(num,num)--> float
Convert the given temp in celcius temp_c to Fahrenheit
>>>cel_to_fah(57)
134.6
>>>cel_to_fah(100)
212.0
'''
    return (temp_c*9/5)+32
