#date :2013-1-21
#author :zhaoliang
#function: the fundemental knowledge about python!
import math
import wx


name = ('Bob','Black')
class MyClass:
    var1 = "variable"
    def Method(first,last,*tuple,**dictionary):
        print"he is %s,his hair color is %s"%(name)
        if(name == "zhao"):
            while 1:
                sex = raw_input("Please Enter your sex:")
                high =input("Please Enter your height:")
                if(sex == 1 and high >=170):
                    print "oh,Man! You can get into it!"
                    continue;
                elif(sex == 2 and high >=160):
                    print "oh,Ladies!Come into my house!"
                    continue;
                else:
                    print "Gun!"
                    break;
        else:
            print "whats up,you should leave now!"


def dictionaryE(**item):
    print item
bacon = {'Mom':21,'Dad':34}
dictionaryE(**bacon)

mycl1 = MyClass()
Test = mycl1.Method
strin = Test('hi','hello',2,math.sqrt(5),6,3,6,7,2,apples=5,bacons=8,butter = 10)

print "strin"+str(strin)
print strin
def list(*food):
    print food
access = list(9!=9,"hi",('doc'>'cat'))
print "hi"+`access`+repr(access)+str(access)
#print dir(math)+help(math.sqrt)+math.__doc__  #TypeError: can only concatenate list (not "NoneType") to list
print str(dir(math))+str(help(math.sqrt))+str(math.__doc__)
seperator = "_*_"
con = "welcome to "
place = "shao lin"
a = [1,2,3]
b = [4,5,6]
t = a.extend(b)

print seperator.join(str(t))
fob = open('readModule.txt','w')
fob.writelines("[1,2,4],[3,5,6]")
print fob.name  #help(file)
fob.close()

print ",:``:\:.:():[]:{}:%:#:*"+" Take care!every symbol has his own mening"
print "str,[]list,()tuple are all sequence which have index and slicing!"


                
