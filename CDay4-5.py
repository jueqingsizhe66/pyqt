#date :2013-1-19
#author :zhaoliang
#function: for cycle and then write the consequence into the file
# _*_ coding:   utf-8 _*_
import os
export = ""
for root,dirs,files in os.walk('J:'):
    export += "\n %s;%s;%s"% (root,dirs,files)
    open('mycd2.cdc','w').write(export)
