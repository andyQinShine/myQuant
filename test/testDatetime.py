import datetime
import time


# print(datetime.datetime.strptime('2018-08-27 22:00:00',"%Y-%m-%d %H:%M:%S").strftime('%Y%m%d'))
# print(datetime.datetime.strptime('2018-08-27 22:00:00',"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
#
# timeStamp  = 1543593600
# timeArray = time.localtime(timeStamp)
# print(timeArray)
# date = time.strftime("%Y%m%d %H:%M:%S", timeArray)
# datetime = datetime.datetime.strptime(date, "%Y%m%d %H:%M:%S")
# print(datetime)
# # date = time.strptime(timeArray, "%Y%m%d %H:%M:%S")
# print(datetime.strftime('%Y%m%d'))


timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
print("", timestamp)