#!-*-coding = utf-8-*-:
#simpson 法计算积分，数值积分，效果非常理想
from math import *
def func(x): 
    """
    定义被积分函数
    """
    return x*sin(x)

def Get_N(a,b,width):
    # width为步长
    N=int((b-a)/width + 1)
    if N%2 == 0:
        N=N+1
    return N

def GenerateData(a,b,n,width):
    datas = []
    r=a
    for i in range(0,n):#N相当大的  所以计算结果误差相当小 因为补偿特别小！ 但是效率不敢保证
        datas.append(func(r))
        r = r+width
    return datas

def simpson_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        if i%2== 0:
            sum = sum +4*datas[i-1]#这边不能用数学上要求的k+1/2  k+1因为这是一个数组  里面的值就是已经算好的！  只要满足那种前后关系！书写数值积分的关键在于系数和时间步长
            #还有就是上下限的值   时间步长重要是因为决定着循环次数！也就是让计算机做多少遍   上下积分重要是因为决定一定的时间的步长的次数！
        else:
            sum = sum +2*datas[i-1]
    return sum*width/3.0 #why not /6.0  因为这时候他的所有不常在原来的基础上在进行细化了 h/6*2才是现在的差分格式的算法

def Trapezoidal_intergral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        sum = sum +2*datas[i]
    return sum*width/2.0 #why not /6.0    

if __name__ == "__main__":
    a=1.0 #积分上限
    b=3.0 #积分下限
    width=0.0625 #步长
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
    print "simpson_integral is ",simpson_integral(datas,width,N)
    print "Trapezoidal_integral is ",Trapezoidal_intergral(datas,width,N)

#-3cos3+sin3+cos1-sin1
