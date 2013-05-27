#date :2013-1-20
#author :zhaoliang
#function: multiple write into file   "export"
#_*_ coding: utf-8 _*_
import os
def cdWalker(cdrom,cdfile):
    export = ""
    for root, dirs, files in os.walk(cdrom):
        export += "\n %s;%s;%s" % (root,dirs,files)
    open(cdfile,'w').write(export)
cdWalker('F:','cd1.cdc')
cdWalker('F:','cd2.cdc')
