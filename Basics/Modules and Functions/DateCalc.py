import time
from time import monotonic as my_timer
import random

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())
#
# timeHere = time.localtime()
# print(timeHere)
# print("Year: ", timeHere[0], timeHere.tm_year)
# print("Month: ", timeHere[1], timeHere.tm_mon)
# print("Day: ", timeHere[2], timeHere.tm_mday)

input("Press enter to start")

waitTime = random.randint(1, 6)
time.sleep(waitTime)
startTime = my_timer()
input("Press enter to stop")

endTime = my_timer()

print("Started at " + time.strftime("%X", time.localtime(startTime)))
print("Ended at " + time.strftime("%X", time.localtime(endTime)))
print("Your reaction time was {} seconds".format(endTime - startTime))
