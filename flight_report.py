#WAP to find out if flight is on schedule, early or delayed
# Time convention: 3:00-->3.0, 14:30--> 14.5
# 0<=time<24

def flightReport(declared_time, actual_time):
    '''(float,float)-->NoneType
Precondition: Time convention: 3:00-->3.0, 14:30--> 14.5 and 0<=time<24
Print whether the flight is on time, arriving early or delayed based on declared_time, and actual_time.
>>>flightReport(19.0,19.0)
On time
>>>flightReport(6.25,7.00)
Delayed
'''
    if actual_time<declared_time:
        print("Arriving early")
    elif actual_time==declared_time:
        print("On time")
    else:
        print("Delayed")
