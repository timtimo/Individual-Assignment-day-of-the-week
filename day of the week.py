#Name: MUYOMBA TIMOTHY  REG.NO.: 14/U/10289/PS
#Script shows the day of the week for a date
#These print statements visually gives user NUMBER needed for month
print '-' * 12
print "  March = 1" 
print "  April = 2" 
print "  May = 3"
print "  June = 4"
print "  July = 5"
print "  August = 6" 
print "  September = 7" 
print "  October = 8" 
print "  November = 9"
print "  December = 10" 
print "  January = 11" 
print "  February = 12"
print '-' * 12
print " "

def day_of_week():
    month = ["March", "April", "May", "June", "July", "August", "September", 
    "October", "November", "December", "January", "February"]

    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
    "Saturday", "Sunday"]
    
    a = int(raw_input("Enter NUMBER from above list for Month of the Year: "))
    print "Month : ", month[a - 1] 
    print " "

    b = int(raw_input("Enter day the month (e.g. 1, 2, 3, ..., 30, 31): "))
    print "Day : ", b
    print " "

    c = int(raw_input("Enter year in the century (e.g. 89 for the year 1989): "))
    print "Year : ", c
    print " "
    if a == 11 or a == 12:
        c = c - 1 
    else: 
        c = c        

    d = int(raw_input("Enter the century (e.g 19 for the year 1989): "))
    print "Century : ", d 
    print " "

    w = (13 * a - 1) / 5 
    x = c / 4 
    y = d / 4 
    z = w + x + y + b + c - 2 * d 
    r = z % 7

    print "  ", month[a - 1], str(b) + ",", str(d) + str(c),"was: ", day[r],"!!"
    print " "
    
day_of_week()

