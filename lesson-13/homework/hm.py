import datetime

from datetime import date,time,datetime

year = int(input("Enter your birth year: "))
month = int(input("Enter yout birth month: "))
day = int(input("Enter your birth day: "))

today = date.today()
birthdate = date(year, month, day)
delta= today - birthdate

years = delta.days// 365
months= (delta.days % 365) // 30
days = (delta.days % 365) % 30

print (f"You are approximately {years} years, {months} months and {days} days old")


month = int(input("Enter yout birth month: "))
day = int(input("Enter your birth day: "))

today = date.today()
year = today.year

birthday = date(year, month, day)

if birthday < today:
    birthday = date(year +1, month, day)

days_left = (birthday- today).days
print(f"There are {days_left} days left until your next birthday.")

from datetime import datetime,timedelta

date = input('Enter today date(YYYY-MM-DD): ')
time = input('Enter current time(HH:MM): ')

dt_str= date +" "+ time
current_time = datetime.strptime(dt_str,"%Y-%m-%d %H:%M")
hours = int(input("Meeting duration (hours): "))
minutes = int(input("Meeting duration (minutes): "))
end_time = current_time + timedelta(hours=hours, minutes=minutes)

print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

import pytz
from datetime import datetime


date = input("Enter date (YYYY-MM-DD): ")
time = input("Enter time (HH:MM): ")
dt_str = date + " " + time

from_zone = input("Your timezone (e.g. Asia/Tashkent): ")
to_zone = input("Convert to timezone (e.g. Europe/London): ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)
local_dt = from_tz.localize(dt)

converted_dt = local_dt.astimezone(to_tz)

print("Time in", to_zone, "is", converted_dt.strftime("%Y-%m-%d %H:%M"))


import time
from datetime import datetime

future = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")


future_time = datetime.strptime(future, "%Y-%m-%d %H:%M:%S")


while True:
    now = datetime.now()
    diff = future_time - now

    if diff.total_seconds() <= 0:
        print("Time's up!")
        break

    print("Time left:", diff)
    time.sleep(1)


import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email= input("Enter your Email address: ")
if re.match(pattern, email):
    print("Valid Email address!")
else :
    print("Error, Invalid email address!")

phone=(input("Enter a 10 digit phone number:"))
formatted= " ("+ phone[0:3]+") " + phone[3:6] + "-" + phone[6:10]
print(formatted)

password= (input("Enter a password:"))

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8

if has_upper and has_lower and has_digit and is_long_enough:
    print("strong password")
else:
    print("Weak Password")
    if not is_long_enough:
        print("Is at least 8 characters long")
    if not has_upper:
        print("Contains at least 1 uppercase letter")
    if not has_lower:
        print ("Contains at least 1 lowercase letter")
    if not has_digit:
        print ("Contains at least 1 digit")
