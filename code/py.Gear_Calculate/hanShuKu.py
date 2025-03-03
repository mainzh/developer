#函数库
    #根据不同的功能，自定义函数，建立库，其他脚本需要对应功能时，直接调用该库中的对应函数

from math import *
from scipy.stats.mstats import gmean

#渐开线函数
    #输入: theta ——角度(弧度值)
    #输出: inv ——渐开线函数
#inv= lambda theta: tan( theta)- theta
#def inv(theta): return tan( theta)- theta
def inv(theta):
    return tan(theta)- theta

#反渐开线函数
    #输入：inv ——渐开线函数
    #输出：rinv ——角度(弧度值)
    #注：python不能对负数开方，即使是奇数次方
def rinv(inv):
    rinv_0= pow((sqrt(9* inv+ 1)- 1)/ 1.5, 1/3)
    for i in range(10):
        rinv_0= acos(sin(rinv_0)/ (inv+ rinv_0))
    return rinv_0

#找出给定值在(有序)数列中最近的上下限
    #输入：array ——(有序)数列，value ——给定值
    #输出：[ before, after] ——最近的上下限值(前一个值，后一个值)
from bisect import bisect_left
def nearest(array,value):
    #若 给定值value <= 列表array中第一个值，则最近的上下限值为列表array中的第一个值和第二个值
    if value<= array[0]:
        before= array[0]
        after= array[1]
    #若 给定值value >= 列表array中倒数第一个值，则最近的上下限值为列表array中的倒数第一个值和倒数第二个值
    elif value>= array[-1]:
        before= array[-2]
        after= array[-1]
    else:
        #找到 给定数值value <= 列表array中第一个值的下标
        pos= bisect_left(array, value)
        before= array[pos -1]
        after= array[pos]
    return [before, after]

#标准公差数值计算
    #输入：d ——基本尺寸(mm)，IT ——公差等级(20个等级：IT01、IT0、IT1、IT2、...、IT18)。
    #输出：tolerance_IT ——标准公差(um)。
    #基本尺寸< 1mm ， 无IT14~ IT18。
    #公式和代码没错，计算值与查表值对不上?????
def tolerance_IT(d,IT):
    d_FenDuan= [3,6,10,18,30,50,80,120,180,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]
    if d<= d_FenDuan[0]: D= gmean([1, d_FenDuan[0]])
    else: D= gmean(nearest(d_FenDuan, d))
    #基本尺寸<=500mm
    if d<= 500:
        i= 0.45* pow(D, 1/3)+ 0.001* D
        iI= i
        if IT== 0.1: tolerance_IT= 0.3+ 0.008* D
        if IT== 0: tolerance_IT= 0.5+ 0.012* D
        if IT== 1: tolerance_IT= 0.8+ 0.02* D
        if IT== 2: tolerance_IT= (0.8+ 0.02* D)* pow(7* iI/(0.8+ 0.02* D), 1/4)
        if IT== 3: tolerance_IT= (0.8+ 0.02* D)* pow(7* iI/(0.8+ 0.02* D), 1/2)
        if IT== 4: tolerance_IT= (0.8+ 0.02* D)* pow(7* iI/(0.8+ 0.02* D), 3/4)
    #基本尺寸>500~3150mm
    elif d> 500 and d<= 3150:
        I= 0.004* D+ 2.1
        iI= I
        if IT== 0.1: tolerance_IT= 1* iI
        if IT== 0: tolerance_IT= pow(2, 1/2)* iI
        if IT== 1: tolerance_IT= 2* iI
        if IT== 2: tolerance_IT= (2* iI)* pow(2* iI/ 7* iI, 1/4)
        if IT== 3: tolerance_IT= (2* iI)* pow(2* iI/ 7* iI, 1/2)
        if IT== 4: tolerance_IT= (2* iI)* pow(2* iI/ 7* iI, 3/4)
    if IT== 5: tolerance_IT= 7* iI
    if IT== 6: tolerance_IT= 10* iI
    if IT== 7: tolerance_IT= 16* iI
    if IT== 8: tolerance_IT= 25* iI
    if IT== 9: tolerance_IT= 40* iI
    if IT== 10: tolerance_IT= 64* iI
    if IT== 11: tolerance_IT= 100* iI
    if IT== 12: tolerance_IT= 160* iI
    if IT== 13: tolerance_IT= 250* iI
    if IT== 14: tolerance_IT= 400* iI
    if IT== 15: tolerance_IT= 640* iI
    if IT== 16: tolerance_IT= 1000* iI
    if IT== 17: tolerance_IT= 1600* iI
    if IT== 18: tolerance_IT= 2500* iI
    return tolerance_IT
