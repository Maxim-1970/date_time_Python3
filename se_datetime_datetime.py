from datetime import datetime as dt

# now_date = dt(2020, 4, 5, 18, 11)
now_date = dt.now()
fin = []

lateness = []
time_norma = dt.now()
file = open('calendar.txt', 'r')
strings = file.readlines()
for string in strings:
    members = string.split(',')
    dd = members[1].split(' ')
    ddd = dd[0].split('.') + dd[1].split(':')
    i = 0
    for i in range(len(ddd)):
        ddd[i] = int(ddd[i])
    sa_date = dt(ddd[2], ddd[1], ddd[0], ddd[3], ddd[4])
    if sa_date > now_date:
        fin.append(members[0])
file.close()
# print(fin)
i = 0
for i in range(len(fin)):
    fin[i] = str(fin[i])
print( ', '.join( fin ) )
