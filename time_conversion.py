#!/bin/python3
'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
'''
import sys

def convertHour(hour, am_pm):
    if am_pm == "AM":
        if hour == "12":
            hour = "00"
    elif am_pm == "PM":
        if hour == "12":
            hour = "12"
        else:
            hour = str(int(hour) + 12) 
    
    return hour


time = input().strip()
#time = "07:05:45PM"

arr = time.split(":")
#print(arr)

seconds = str(arr[2])[:-2]
minutes = str(arr[1])
hour = convertHour(arr[0], arr[2][-2:])
print(hour+":"+minutes+":"+seconds)