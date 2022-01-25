# import time
#
# print("The epoch time of the system starts at",time.strftime("%c", time.gmtime(0)))
# print("The current timezone is {0} with an offset of  {1} ".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDay Light Saving Time is in affect of this location")
#     print("\tThe DST timezone is ", time.tzname[1])
#
# print("Local Time is ", time.strftime("%y-%m-%d %H-%M-%S", time.localtime()))
# print("UTC Time is ", time.strftime("%y-%m-%d %H-%M-%S", time.gmtime()))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
