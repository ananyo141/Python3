#WAP to display if person should take umbrella for rain or boots and coat for snow for subzero temp or nothing.

def predictWeather(temp,humidity):
    optimal_temp = 25
    critical_humidity= 95
    if temp==optimal_temp:
        if humidity<critical_humidity:
            print("Clear day, beautiful day indeed.\n")
        else:
            print("Expect rain.Take umbrella\n")
    elif temp>optimal_temp:
        if humidity>=critical_humidity:
            print("Expect rain.Take umbrella\n")
        else:
            print("It is a hot day. Take umbrella anyway.\n")
    elif 0<temp<optimal_temp:
        if humidity>=critical_humidity:
            print("Expect rain, take umbrella.\n")
        else:
            print("Temperature is lower than optimal. Wear a woolen scarf\n")
    elif temp<=0:
        if humidity>=critical_humidity:
            print("Snowfall!Take your boots and gloves and make that ugly snowman!\n")
        else:
            print("Sub-zero temperatures. Advised to stay indoors.\n")