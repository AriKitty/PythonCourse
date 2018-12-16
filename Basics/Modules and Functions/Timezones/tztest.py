import pytz
import datetime

country = 'Europe/Moscow'

tzToDisplay = pytz.timezone(country)
localTime = datetime.datetime.now(tz=tzToDisplay)
print("The time in {} is {}".format(country, localTime))
print("UTC is {}".format(datetime.datetime.utcnow()))

# # Print all of the timezones
# for x in pytz.all_timezones:
#     print(x)
#
# # Print the country codes sorted alphabetically
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# Will produce an error w/o the .get(x)
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))


for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tzToDisplay = pytz.timezone(zone)
            localTime = datetime.datetime.now(tz=tzToDisplay)
            print("\t\t{}: {}".format(zone, localTime))
    else:
        print("\t\tNo time zone defined")
