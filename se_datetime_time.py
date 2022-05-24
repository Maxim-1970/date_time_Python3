from datetime import time
# t= time(14,45,36,9955)
# print(t.hour, t.minute, t.second, t.microsecond)
import datetime

lateness = []
time_norma = datetime.time(9,0,0)
file = open('visits.txt', 'r')
strings = file.readlines()
for string in strings:
    members = string.split(',')
    dd = members[1].split(':')
    p_date = datetime.time(int(dd[0]), int(dd[1]), int(dd[2]))
    if p_date > time_norma:
        lateness.append(int(members[0]))
file.close()
lateness = sorted(lateness)
i = 0
for i in range(len(lateness)):
    lateness[i] = str(lateness[i])
print( ','.join( lateness ) )

