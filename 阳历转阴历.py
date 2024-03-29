#! -*- encoding: GBK -*-
#其实不是有那个纸质版本的万年历嘛
import re
import math
import time
import os

MONTH_NAME = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MONTH_DAYS = [0,31,28,31,30,31,30,31,31,30,31,30,31];

LUNAR_CALENDAR_TABLE = [
    0x04AE53,0x0A5748,0x5526BD,0x0D2650,0x0D9544,0x46AAB9,0x056A4D,0x09AD42,0x24AEB6,0x04AE4A, # //*1901-1910*/
    0x6A4DBE,0x0A4D52,0x0D2546,0x5D52BA,0x0B544E,0x0D6A43,0x296D37,0x095B4B,0x749BC1,0x049754, # //*1911-1920*/
    0x0A4B48,0x5B25BC,0x06A550,0x06D445,0x4ADAB8,0x02B64D,0x095742,0x2497B7,0x04974A,0x664B3E, # //*1921-1930*/
    0x0D4A51,0x0EA546,0x56D4BA,0x05AD4E,0x02B644,0x393738,0x092E4B,0x7C96BF,0x0C9553,0x0D4A48, # //*1931-1940*/   
    0x6DA53B,0x0B554F,0x056A45,0x4AADB9,0x025D4D,0x092D42,0x2C95B6,0x0A954A,0x7B4ABD,0x06CA51, # //*1941-1950*/
    0x0B5546,0x555ABB,0x04DA4E,0x0A5B43,0x352BB8,0x052B4C,0x8A953F,0x0E9552,0x06AA48,0x6AD53C, # //*1951-1960*/
    0x0AB54F,0x04B645,0x4A5739,0x0A574D,0x052642,0x3E9335,0x0D9549,0x75AABE,0x056A51,0x096D46, # //*1961-1970*/
    0x54AEBB,0x04AD4F,0x0A4D43,0x4D26B7,0x0D254B,0x8D52BF,0x0B5452,0x0B6A47,0x696D3C,0x095B50, # //*1971-1980*/
    0x049B45,0x4A4BB9,0x0A4B4D,0xAB25C2,0x06A554,0x06D449,0x6ADA3D,0x0AB651,0x093746,0x5497BB, # //*1981-1990*/
    0x04974F,0x064B44,0x36A537,0x0EA54A,0x86B2BF,0x05AC53,0x0AB647,0x5936BC,0x092E50,0x0C9645, # //*1991-2000*/
    0x4D4AB8,0x0D4A4C,0x0DA541,0x25AAB6,0x056A49,0x7AADBD,0x025D52,0x092D47,0x5C95BA,0x0A954E, # //*2001-2010*/
    0x0B4A43,0x4B5537,0x0AD54A,0x955ABF,0x04BA53,0x0A5B48,0x652BBC,0x052B50,0x0A9345,0x474AB9, # //*2011-2020*/
    0x06AA4C,0x0AD541,0x24DAB6,0x04B64A,0x69573D,0x0A4E51,0x0D2646,0x5E933A,0x0D534D,0x05AA43, # //*2021-2030*/
    0x36B537,0x096D4B,0xB4AEBF,0x04AD53,0x0A4D48,0x6D25BC,0x0D254F,0x0D5244,0x5DAA38,0x0B5A4C, # //*2031-2040*/
    0x056D41,0x24ADB6,0x049B4A,0x7A4BBE,0x0A4B51,0x0AA546,0x5B52BA,0x06D24E,0x0ADA42,0x355B37, # //*2041-2050*/
    0x09374B,0x8497C1,0x049753,0x064B48,0x66A53C,0x0EA54F,0x06B244,0x4AB638,0x0AAE4C,0x092E42, # //*2051-2060*/
    0x3C9735,0x0C9649,0x7D4ABD,0x0D4A51,0x0DA545,0x55AABA,0x056A4E,0x0A6D43,0x452EB7,0x052D4B, # //*2061-2070*/
    0x8A95BF,0x0A9553,0x0B4A47,0x6B553B,0x0AD54F,0x055A45,0x4A5D38,0x0A5B4C,0x052B42,0x3A93B6, # //*2071-2080*/
    0x069349,0x7729BD,0x06AA51,0x0AD546,0x54DABA,0x04B64E,0x0A5743,0x452738,0x0D264A,0x8E933E, # //*2081-2090*/
    0x0D5252,0x0DAA47,0x66B53B,0x056D4F,0x04AE45,0x4A4EB9,0x0A4D4C,0x0D1541,0x2D92B5           # //*2091-2099*/
]
# 下面的三个表格是农历数据表 LunarCalendarTable 的结构。总共使用了32位整数的0～23位。
# 
# 6 5                4 3 2 1 0 
# 表示春节的公历月份 表示春节的公历日期 
# 
# 19 18 17 16 15 14 13 12 11 10  9  8  7 
# 1   2  3  4  5  6  7  8  9 10 11 12 13
# 农历1-13 月大小 。月份对应位为1，农历月大(30 天),为0 表示小(29 天)
# 
# 23 22 21 20 
# 表示当年闰月月份，值为0 为则表示当年无闰月。

def get_month_days(year, month):
  global MONTH_DAYS;
  if(month==2):
    if(((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
      return 29
    else:
      return 28
  else:
    return(MONTH_DAYS[month]);

def get_syear_days(syear):
  if(((syear%4 == 0) and (syear%100 != 0)) or (syear%400 == 0)):
    return 366
  else:
    return 365

def get_days_of_syear(syear, smonth, sday):
  """ get given day's number of sun year """
  days = 0
  for i in range(1, smonth):
    days += get_month_days(syear, i)
  days += sday
  return days

def get_days_of_lyear(syear, smonth, sday):
  """ get given day's number of the lunar year """
  global LUNAR_CALENDAR_TABLE
  lyear = syear
  spring_month = (LUNAR_CALENDAR_TABLE[syear-1901] & 0x60) >> 5
  spring_day = (LUNAR_CALENDAR_TABLE[syear-1901] & 0x1F)
  if ((spring_month > smonth) or ((spring_month == smonth) and (spring_day > sday))):
    # the day is before spring festival day, and is previous day in lunar year
    spring_month = (LUNAR_CALENDAR_TABLE[syear-1901 - 1] & 0x60) >> 5
    spring_day = (LUNAR_CALENDAR_TABLE[syear-1901 - 1] & 0x1F)
    lyear -= 1
    lunar_days = get_syear_days(lyear) + get_days_of_syear(syear, smonth, sday) \
        - get_days_of_syear(lyear, spring_month, spring_day)
  else:
    lunar_days = get_days_of_syear(syear, smonth, sday)  \
        -  get_days_of_syear(syear, spring_month, spring_day)
  lunar_days += 1 # consider current day
  return (lyear, lunar_days)

def get_lunar_date(syear, smonth, sday):
  if syear < 1901 or syear > 2099:
    return
  # lunar year, lunar days to spring festival
  lyear, lunar_days = get_days_of_lyear(syear, smonth, sday);
  l_double_month = (LUNAR_CALENDAR_TABLE[lyear-1901] >> 20 ) & 0xF

  lmonth = lday = 1
  bits = 19
  month_begin_day = 0
  for lmonth in range(1, 14):
    l_month_big = (LUNAR_CALENDAR_TABLE[lyear-1901] >> bits) & 0x1
    if month_begin_day + 29 + l_month_big < lunar_days:
      lmonth += 1
      month_begin_day += 29 + l_month_big
    else:
      lday = lunar_days - month_begin_day
      break
    bits -= 1
  if l_double_month:
    # lunar double month adjust
    if l_double_month == lmonth - 1:
      lmonth -= 1
      lmonth += 100  # double month 
    elif l_double_month < lmonth - 1:
      lmonth -= 1
  return (lyear, lmonth, lday)

if __name__ == "__main__":
    y,m,d = 2010, 9, 28
    print "Sun calendar 2010-9-28 == Lunar calendar ",  get_lunar_date(y,m,d)
