from math import e
deposit = int(input("enter the deposit amount:"))
rate = int(input("Enter the rate:"))
time = int(input("Enter the time:"))

for time in range(1,time + 1):
    interest = deposit*e**((rate/100)*time)
    print("Interest for", time, "day(s)is:",interest)