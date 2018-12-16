# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and URC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import pytz
import datetime

utcTime = datetime.datetime.utcnow()

availableZones = {'1': "Africa/Tunis",
                  '2': "Asia/Kolkata",
                  '3': "Australia/Adelaide",
                  '4': "Europe/Brussels",
                  '5': "Europe/London",
                  '6': "Japan",
                  '7': "Pacific/Tahiti",
                  '8': "US/Central",
                  '9': "Zulu"}

print("Please choose a time zone or 0 to quit: ")
for place in sorted(availableZones):
    print("\t{}. {}".format(place, availableZones[place]))

while True:
    choice = input()

    if choice == '0':
        print("Good bye!")
        break

    if choice in availableZones.keys():
        tzToDisplay = pytz.timezone(availableZones[choice])
        worldTime = datetime.datetime.now(tz=tzToDisplay)
        print("The time in {} is {} {}".format(availableZones[choice], worldTime.strftime('%A %x %X %z'), worldTime.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
