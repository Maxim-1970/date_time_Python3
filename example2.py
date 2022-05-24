import datetime

zarpl = 0
file = open('days.txt', 'r')
strings = file.readlines()
for string in strings:
    # вычисляем день недели
    # print( string )
    members = string.split(',')
    # print(members[0])
    dd = members[0].split('-')
    p_date = datetime.date(int(dd[0]), int(dd[1]), int(dd[2]))
    # print(p_date.isoweekday())
    dn = p_date.isoweekday()
    if dn == 6 or dn == 7:
        zarpl += int(members[1])*1500
    else:
        zarpl += int(members[1])*1000
file.close()

print(zarpl)