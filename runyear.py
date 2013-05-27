
#date :2013-1-19
#author :zhaoliang
#function: justify whether the yeah is lunar year or not

year = int(raw_input("please Enter the year:"))
if(year%400 == 0 or year%4 == 0 and year %100 != 0):
    print year,'is run nian!'

else:
    print year,'is not run nian'
