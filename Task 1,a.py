# TASK DOUBT CLARIFICATION SESSION

import time

time_stamp = time.strftime("%Y%m%d-%H%M%S")
time_stamp = str(time_stamp+".txt")
print(time_stamp)
print(type(time_stamp))
file = open(time_stamp, "w")
file.write(time.strftime("%Y%m%d-%H%M%S"))
file.close()
