#converting time from 12 to 24 hour
from datetime import datetime
def convert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "AM":
        return str1[:-2]

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
print( current_time)
print(convert(current_time))

