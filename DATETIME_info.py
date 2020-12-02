# Scratch
#!/usr/bin/env python3
import datetime
import pytz

dt_india = datetime.datetime.now()
utc_dt_india = datetime.datetime.now(tz=pytz.UTC)
utc_dt_Dubai = utc_dt_india.astimezone(pytz.timezone('Asia/Dubai'))
utc_dt_US = utc_dt_india.astimezone(pytz.timezone('US/Mountain'))
print("IST CUR:", dt_india)
print("UTC IND:", utc_dt_india)
#print("UTC :", utc_dt_US)
print("UTC UAE :", utc_dt_Dubai)

#TO SEE ALL TIMEZONES
#for tz in pytz.all_timezones:
#    print(tz)

#TO CONVERT CURRENT TIME TO OTHER CURRENT
utc_ind_dubai = dt_india.astimezone(pytz.timezone('Asia/Dubai'))
print("IST TO UAE :",utc_ind_dubai)

#TO CONVER CURENT TIME TO UTC
india_tz = pytz.timezone('Asia/Kolkata')
ind = india_tz.localize(dt_india)
print("IND LOCAL : ",ind)

#TO PRINT IN FORMAT, FOR MORE CHECK PYTHON DOCUMENTATION @ https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior
#print(dt_india.strftime('%B %D, %Y'))
#print(dt_india.strftime('%B %d, %Y'))

#TO CONVERT STRING TO DATETIME
dt_str = 'December 03, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)