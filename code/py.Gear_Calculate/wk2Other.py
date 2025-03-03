from hanShuKu import * 


print("---已知公法线求其他---")
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

dp=5

k=3
print("计算跨齿(槽)数k",k)
wkn=23.119
print("公法线长度wkn(mm)",wkn)
Ebns=-0.06
print("公法线长度上极限偏差Ebns(mm)",Ebns)
Ebni=-0.13
print("公法线长度下极限偏差Ebni(mm)",Ebni)

print("---计算基础参数---")
mt=mn/cos(beta)
print("端面模数mt(mm):",mt)
alphat=atan(tan(alphan)/cos(beta))
print("端面压力角alphat(°):",degrees(alphat))
betab=atan(tan(beta)*cos(alphat))
print("基圆螺旋角betab(°):",degrees(betab))

print("---已知公法线求其他---")
zp=z*inv(alphat)/inv(alphan)
xn=(wkn/mn-(cos(alphan)*(pi*(k-0.5)+zp*inv(alphan))))/2/sin(alphan)
print("法向变位系数xn:",xn)
if wainiehe ==1:sn=mn*(pi/2+2*xn*tan(alphan))
else:sn=mn*(pi/2-2*xn*tan(alphan))
print("公称(法向)齿厚sn(mm)",sn)
Esns=Ebns/cos(alphan)
print("齿厚上极限偏差Esns(mm)",Esns)
Esni=Ebni/cos(alphan)
print("齿厚下极限偏差Esni(mm)",Esni)
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