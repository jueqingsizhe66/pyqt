#date :2013-1-19
#author :zhaoliang
#function: read file
# _*_ coding:   utf-8 _*_
import os
for root, dirs, files in os.walk("G:/"):
    open('mycd.cdc','a').write("%s %s %s" % (root,dirs,files))
