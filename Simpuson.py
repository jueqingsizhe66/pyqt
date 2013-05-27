#!-*-coding = utf-8-*-:
#simpson ��������֣���ֵ���֣�Ч���ǳ�����
from math import *
def func(x): 
    """
    ���屻���ֺ���
    """
    return x*sin(x)

def Get_N(a,b,width):
    # widthΪ����
    N=int((b-a)/width + 1)
    if N%2 == 0:
        N=N+1
    return N

def GenerateData(a,b,n,width):
    datas = []
    r=a
    for i in range(0,n):#N�൱���  ���Լ���������൱С ��Ϊ�����ر�С�� ����Ч�ʲ��ұ�֤
        datas.append(func(r))
        r = r+width
    return datas

def simpson_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        if i%2== 0:
            sum = sum +4*datas[i-1]#��߲�������ѧ��Ҫ���k+1/2  k+1��Ϊ����һ������  �����ֵ�����Ѿ���õģ�  ֻҪ��������ǰ���ϵ����д��ֵ���ֵĹؼ�����ϵ����ʱ�䲽��
            #���о��������޵�ֵ   ʱ�䲽����Ҫ����Ϊ������ѭ��������Ҳ�����ü���������ٱ�   ���»�����Ҫ����Ϊ����һ����ʱ��Ĳ����Ĵ�����
        else:
            sum = sum +2*datas[i-1]
    return sum*width/3.0 #why not /6.0  ��Ϊ��ʱ���������в�����ԭ���Ļ������ڽ���ϸ���� h/6*2�������ڵĲ�ָ�ʽ���㷨

def Trapezoidal_intergral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        sum = sum +2*datas[i]
    return sum*width/2.0 #why not /6.0    

if __name__ == "__main__":
    a=1.0 #��������
    b=3.0 #��������
    width=0.0625 #����
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
    print "simpson_integral is ",simpson_integral(datas,width,N)
    print "Trapezoidal_integral is ",Trapezoidal_intergral(datas,width,N)

#-3cos3+sin3+cos1-sin1
