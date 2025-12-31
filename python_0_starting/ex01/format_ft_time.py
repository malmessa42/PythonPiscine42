# Allowed functions : time, datetime or any other library that allows to receive the date

import time as t
from datetime import datetime as dt

time_sinse_1970 = t.time()
now = dt.now()
day = now.day
month = now.strftime("%b") # .strftime("%b") is a method used to convert that datetime object into a string representation.
year = now.year

print("Seconds since January 1, 1970: {} or {:.2e} in scientific notation\n{} {} {}".format(time_sinse_1970, time_sinse_1970, month, day, year))