#date :2013-1-19
#author :zhaoliang
#function: write file  and string.append
# _*_ coding: utf-8 _*_
import os
export = []
for root, dirs, files in os.walk("c:"):
    export.append("\n %s; %s; %s" % (root,dirs,files))
open('mycd3.cdc','w').write(''.join(export))
