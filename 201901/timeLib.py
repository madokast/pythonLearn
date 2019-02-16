import time

print(time.time())
#1547642050.57

print(time.ctime())
#Wed Jan 16 20:31:01 2019

print(time.gmtime())
#time.struct_time(tm_year=2019, tm_mon=1, tm_mday=16, 
# tm_hour=12, tm_min=34, tm_sec=10, tm_wday=2, tm_yday=16, tm_isdst=0)

print(time.strftime("%Y",time.gmtime()))
#2019
