#coding=utf8
#!/usr/bin/env python<br>
"""还是有点问题  如果没有行首空格呢   如果存在乱码呢？"""
def delspace(file):
    txt=open(file,'r')
    newtxt=open('new.txt','w')
    lines=txt.readlines()
    for line in lines:
        newline=line[1:]
        newtxt.write(newline)
    txt.close()
    newtxt.close()
