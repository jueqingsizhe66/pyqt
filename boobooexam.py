#date :2013-1-18
#author :zhaoliang
#function: the way to define class and constructor
import sys
import os

class test():
    def _init_(self,name1='test',age1=0):
        self.name=name1
        self.age=age1

    def setfun(self,new_name,new_age):
        self.name=new_name
        self.age=new_age

    def getfun(self):
        return self.name,self.age

    def show(self):
        print "my name is: %s,and the age is :%d"%(self.name,self.age)

if __name__ == "name":
    title = raw_input("please enter of name :")
    print "the enter of string is:",title

    tt = test()
    tt.show()
    tt.setfun("tester",22)
    tt.show()
    print tt.getfun()

    print os.path

    
