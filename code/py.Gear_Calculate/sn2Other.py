from hanShuKu import * 


print("---已知齿厚求其他---")
import datetime
print("当前日期时间：" +datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

print("---输入参数---")
wainiehe=1
if wainiehe==1:print("齿轮类型: 外齿轮")  
else:print("齿轮类型: 内齿轮")
mn=3
print("法向模数mn(mm):",mn)
alphan=radians(20)
print("法向压力角alphan(°):",degrees(alphan))
beta=radians(9)
print("螺旋角beta(°):",degrees(beta))
z=22
print("齿数z:",z)

k=0
dp=5

sn=4.734
print("公称(法向)齿厚sn(mm)",sn)
Esns=-0.064
print("齿厚上极限偏差Esns(mm)",Esns)
Esni=-0.14
print("齿厚下极限偏差Esni(mm)",Esni)

print("---计算基础参数---")
mt=mn/cos(beta)
print("端面模数mt(mm):",mt)
alphat=atan(tan(alphan)/cos(beta))
print("端面压力角alphat(°):",degrees(alphat))
betab=atan(tan(beta)*cos(alphat))
print("基圆螺旋角betab(°):",degrees(betab))

print("---已知齿厚求其他---")
if wainiehe==1:xn=(sn/mn-pi/2)/2/tan(alphan)
else:xn=(pi/2-sn/mn)/2/tan(alphan)
print("法向变位系数xn:",xn)
zp=z*inv(alphat)/inv(alphan)
if (k % 2)==0:k=round(zp/pi*(((1+2*xn/zp)**2-(cos(alphan))**2)**0.5/cos(alphan)-2*xn/zp*tan(alphan)-inv(alphan))+0.5)
print("计算跨齿(槽)数k",k)
wxkn=cos(alphan)*(pi*(k-0.5)+zp*inv(alphan))
delwxn=2*xn*sin(alphan)
wkn=(wxkn+delwxn)*mn
print("公法线长度wkn(mm)",wkn)
Ebns=Esns*cos(alphan)
print("公法线长度上极限偏差Ebns(mm)",Ebns)
Ebni=Esni*cos(alphan)
print("公法线长度下极限偏差Ebni(mm)",Ebni)

if dp==0:dp=1.44*mn
print("计算量柱(球)直径dp(mm)",dp)
if wainiehe==1:alpmt=rinv(inv(alphat)+dp/mn/z/cos(alphan)-pi/2/z+2*xn*tan(alphan)/z)
else:alpmt=rinv(inv(alphat)-dp/mn/z/cos(alphan)+pi/2/z+2*xn*tan(alphan)/z)
if (z % 2)==0:
    if wainiehe==1:M=mt*z*cos(alphat)/cos(alpmt)+dp
    else:M=mt*z*cos(alphat)/cos(alpmt)-dp
else:
    if wainiehe==1:M=mt*z*cos(alphat)/cos(alpmt)*cos(90/z)+dp
    else:M=mt*z*cos(alphat)/cos(alpmt)*cos(90/z)-dp
print("跨距M(mm)",M)
if (z % 2)==0:Eyns=Esns*cos(alphat)/sin(alpmt)/cos(betab)
else:Eyns=Esns*cos(alphat)*cos(90/z)/sin(alpmt)/cos(betab)
print("量柱(球)测量跨距上极限偏差Eyns(mm)",Eyns)
if (z % 2)==0:Eyni=Esni*cos(alphat)/sin(alpmt)/cos(betab)
else:Eyni=Esni*cos(alphat)*cos(90/z)/sin(alpmt)/cos(betab)
print("量柱(球)测量跨距下极限偏差Eyni(mm)",Eyni)