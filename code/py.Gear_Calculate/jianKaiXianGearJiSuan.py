from hanShuKu import * 

#基础参数输入
wainiehe= 1
mn= 3
alphan= radians(20)
beta= radians(9)
z1= 22
z2= 19
#计算参数输入
b= 120
hanx= 1
cnx= 0.25
xn1= 0.01
xn2= 0
ai= 62.3
Q= 8
k1= 0
k2= 0
dp= 5

#基础参数计算
u= z2/ z1
mt= mn/ cos(beta)
alphat= atan(tan(alphan)/ cos(beta))
betab= atan(tan(beta)* cos(alphat))
zv1= z1/ (cos(betab))** 2/ cos(beta)
zv2= z2/ (cos(betab))** 2/ cos(beta)
d1= z1* mt
d2= z2* mt
db1= d1* cos(alphat)
db2= d2* cos(alphat)
if wainiehe== 1: a= (d2+ d1)/ 2
else: a= (d2- d1)/ 2

#求总变位系数
#xn2=0不能表示为空没填，也可能表示值为0！表示值为0时，此处算式不对了！
if xn2== 0:
    #已知中心距
    alphawt= acos(a/ ai* cos(alphat))
    if wainiehe== 1:
        xnsigma= (z2+ z1)* (inv(alphawt)- inv(alphat))/ 2/ tan(alphan)
        xn2= xnsigma- xn1
    else:
        xnsigma= (z2- z1)* (inv(alphawt)- inv(alphat))/ 2/ tan(alphan)
        xn2= xnsigma+ xn1
else:
    #已知变位系数
    if wainiehe== 1: xnsigma= xn2+ xn1
    else: xnsigma= xn2- xn1

#法向参数转换为端面参数
hatx= hanx* cos(beta)
ctx= cnx* cos(beta)
xt1= xn1* cos(beta)
xt2= xn2* cos(beta)
xtsigma= xnsigma* cos(beta)

if wainiehe== 1: alphawt= rinv(2* xnsigma* tan(alphan)/ (z2+ z1)+ inv(alphat))
else: alphawt= rinv(2* xnsigma* tan(alphan)/ (z2- z1)+ inv(alphat))
print("端面啮合角alphawt(°):",degrees(alphawt))
if wainiehe== 1: yt=(z2+ z1)/ 2* (cos(alphat)/ cos(alphawt)- 1)
else: yt= (z2- z1)/ 2* (cos(alphat)/ cos(alphawt)- 1)
yn= yt/ cos(beta)
ap= a+ yt* mt
print("变位中心距a'(mm):",ap)
if wainiehe== 1: dp1= 2* ap/ (u+ 1) 
else: dp1= 2* ap/ (u- 1)
print("节圆直径d'1(mm):",dp1)
dp2= dp1* u
print("节圆直径d'2(mm):",dp2)
deltayn= xnsigma- yn
if wainiehe== 1: ha1= (hanx+ xn1- deltayn)* mn
else: ha1= (hanx+ xn1+ deltayn)* mn
print("齿顶高ha1(mm):",ha1)
if wainiehe== 1: ha2= (hanx+ xn2- deltayn)* mn
else: ha2= (hanx- xn2+ deltayn)* mn
print("齿顶高ha2(mm):",ha2)
hf1= (hanx+ cnx- xn1)* mn
print("齿根高hf1(mm):",hf1)
if wainiehe== 1: hf2= (hanx+ cnx- xn2)* mn
else: hf2= (hanx+ cnx+ xn2)* mn
print("齿根高hf2(mm):",hf2)
h1= ha1+ hf1
print("全齿高h1(mm):",h1)
h2= ha2+ hf2
print("全齿高h2(mm):",h2)
da1= d1+ 2* ha1
print("齿顶圆直径da1(mm):",da1)
if wainiehe== 1: da2= d2+ 2* ha2
else: da2= d2- 2* ha2
print("齿顶圆直径da2(mm):",da2)
df1= d1- 2* hf1
print("齿根圆直径df1(mm):",df1)
if wainiehe== 1: df2= d2- 2* hf2
else: df2= d2+ 2* hf2
print("齿根圆直径df2(mm):",df2)
alphaat1= acos(db1/ da1)
print("端面齿顶压力角alphaat1(°):",degrees(alphaat1))
alphaat2= acos(db2/ da2)
print("端面齿顶压力角alphaat2(°):",degrees(alphaat2))
if wainiehe== 1: epsilonalpha= 1/2/pi*(z1*(tan(alphaat1)-tan(alphawt))+z2*(tan(alphaat2)-tan(alphawt)))
else: epsilonalpha=1/2/pi*(z1*(tan(alphaat1)-tan(alphawt))-z2*(tan(alphaat2)-tan(alphawt)))
print("端面重合度epsilonalpha:",epsilonalpha)
epsilonbeta=b*sin(beta)/pi/mn
print("纵向重合度epsilonbeta:",epsilonbeta)
epsilongamma=epsilonalpha+epsilonbeta
print("总重合度epsilongamma:",epsilongamma)
jbnmin=2/3*(0.06+0.0005*ai+0.03*mn)
print("最小法向侧隙jbnmin(mm):",jbnmin)
eta1max=(z1+z2)*(tan(alphaat2)-tan(alphawt))/((z1+z2)*tan(alphawt)-z2*tan(alphaat2))
print("最大滑动率eta1max:",eta1max)
eta2max=(z1+z2)*(tan(alphaat1)-tan(alphawt))/((z1+z2)*tan(alphawt)-z1*tan(alphaat1))
print("最大滑动率eta2max:",eta2max)
dSAP1=2*((da2/2)**2+ap**2-2*ap*da2/2*cos(alphaat2-alphawt))**0.5
print("渐开线起始圆直径dSAP1(mm):",dSAP1)
dSAP2=2*((da1/2)**2+ap**2-2*ap*da1/2*cos(alphaat1-alphawt))**0.5
print("渐开线起始圆直径dSAP2(mm):",dSAP2)

print("---渐开线圆柱齿轮精度等级及偏差---")
mfd1=[0.5,2,3.5,6,10,16,25,40,70]
mnjp1=gmean( nearest( mfd1,mn))
mfd2=[0.2,0.5,0.8,1,1.5,2.5,4,6,10]
mnjp2=gmean( nearest( mfd2,mn))
dfd=[5,20,50,125,280,560,1000,1600,2500,4000,6000,8000,10000]
d1jp=gmean( nearest( dfd,d1))
d2jp=gmean( nearest(dfd,d2))
bfd=[4,10,20,40,80,160,250,400,650,1000]
bjp=gmean( nearest(bfd,b))
if epsilongamma<4:Kjd=0.2*(epsilongamma+4)/epsilongamma
else:Kjd=0.4
fpt1=(0.3*(mnjp1+0.4*(d1jp)**0.5)+4)*10**(-3)*2**(0.5*(Q-5))
print("单个齿距偏差fpt1(mm)",fpt1)
Fpk1=fpt1+1.6*((z1/8-1)*mnjp1)**0.5*10**(-3)*2**(0.5*(Q-5))
print("齿距累积偏差Fpk1(mm)",Fpk1)
Fp1=(0.3*mnjp1+1.25*(d1jp)**0.5+7)*10**(-3)*2**(0.5*(Q-5))
print("齿距累积总偏差Fp1(mm)",Fp1)
Falp1=(3.2*(mnjp1)**0.5+0.22*(d1jp)**0.5+0.7)*10**(-3)*2**(0.5*(Q-5))
print("齿廓总偏差Falp1(mm)",Falp1)
ffalp1=(2.5*(mnjp1)**0.5+0.17*(d1jp)**0.5+0.5)*10**(-3)*2**(0.5*(Q-5))
print("齿廓形状偏差ffalp1(mm)",ffalp1)
fHalp1=(2*(mnjp1)**0.5+0.14*(d1jp)**0.5+0.5)*10**(-3)*2**(0.5*(Q-5))
print("齿廓倾斜偏差fHalp1(mm)",fHalp1)
Fbet1=(0.1*(d1jp)**0.5+0.63*(bjp)**0.5+4.2)*10**(-3)*2**(0.5*(Q-5))
print("螺旋线总偏差Fbet1(mm)",Fbet1)
ffbet1=(0.07*(d1jp)**0.5+0.45*(bjp)**0.5+3)*10**(-3)*2**(0.5*(Q-5))
print("螺旋线形状偏差ffbet1(mm)",ffbet1)
fHbet1=ffbet1
print("螺旋线倾斜偏差fHbet1(mm)",fHbet1)
fpi1=Kjd*(4.3*10**(-3)*2**(0.5*(Q-5))+fpt1+Falp1)
print("一齿切向综合偏差fpi1(mm)",fpi1)
Fpi1=Fp1+fpi1
print("切向综合总偏差Fpi1(mm)",Fpi1)
Fr1=0.8*Fp1
print("径向圆跳动公差Fr1(mm)",Fr1)
fppi1=(2.96*mnjp2+0.01*(d1jp)**0.5+0.08)*10**(-3)*2**(0.5*(Q-5))
print("一齿径向综合偏差fppi1(mm)",fppi1)
Fppi1=Fr1+fppi1
print("径向综合总偏差Fppi1(mm)",Fppi1)

fpt2=(0.3*(mnjp1+0.4*(d2jp)**0.5)+4)*10**(-3)*2**(0.5*(Q-5))
print("单个齿距偏差fpt2(mm)",fpt2)
Fpk2=fpt2+1.6*((z2/8-1)*mnjp1)**0.5*10**(-3)*2**(0.5*(Q-5))
print("齿距累积偏差Fpk2(mm)",Fpk2)
Fp2=(0.3*mnjp1+1.25*(d2jp)**0.5+7)*10**(-3)*2**(0.5*(Q-5))
print("齿距累积总偏差Fp2(mm)",Fp2)
Falp2=(3.2*(mnjp1)**0.5+0.22*(d2jp)**0.5+0.7)*10**(-3)*2**(0.5*(Q-5))
print("齿廓总偏差Falp2(mm)",Falp2)
ffalp2=(2.5*(mnjp1)**0.5+0.17*(d2jp)**0.5+0.5)*10**(-3)*2**(0.5*(Q-5))
print("齿廓形状偏差ffalp2(mm)",ffalp2)
fHalp2=(2*(mnjp1)**0.5+0.14*(d2jp)**0.5+0.5)*10**(-3)*2**(0.5*(Q-5))
print("齿廓倾斜偏差fHalp2(mm)",fHalp2)
Fbet2=(0.1*(d2jp)**0.5+0.63*(bjp)**0.5+4.2)*10**(-3)*2**(0.5*(Q-5))
print("螺旋线总偏差Fbet2(mm)",Fbet2)
ffbet2=(0.07*(d2jp)**0.5+0.45*(bjp)**0.5+3)*10**(-3)*2**(0.5*(Q-5))
print("螺旋线形状偏差ffbet2(mm)",ffbet2)
fHbet2=ffbet2
print("螺旋线倾斜偏差fHbet2(mm)",fHbet2)
fpi2=Kjd*(4.3*10**(-3)*2**(0.5*(Q-5))+fpt2+Falp2)
print("一齿切向综合偏差fpi2(mm)",fpi2)
Fpi2=Fp2+fpi2
print("切向综合总偏差Fpi2(mm)",Fpi2)
Fr2=0.8*Fp2
print("径向圆跳动公差Fr2(mm)",Fr2)
fppi2=(2.96*mnjp2+0.01*(d2jp)**0.5+0.08)*10**(-3)*2**(0.5*(Q-5))
print("一齿径向综合偏差fppi2(mm)",fppi2)
Fppi2=Fr2+fppi2
print("径向综合总偏差Fppi2(mm)",Fppi2)

print("---渐开线圆柱齿轮齿厚测量与计算---")
#按分度圆计算标准公差值，d≤3150,精度等级Q=【3,4,5,6,7,8,9,10】。GBT 1800.1
d1IT7= tolerance_IT( d1,7)* 0.001
d1IT8= tolerance_IT( d1,8)* 0.001
d1IT9= tolerance_IT( d1,9)* 0.001
d1IT10= tolerance_IT( d1,10)* 0.001
d2IT7= tolerance_IT( d2,7)* 0.001
d2IT8= tolerance_IT( d2,8)* 0.001
d2IT9= tolerance_IT( d2,9)* 0.001
d2IT10= tolerance_IT( d2,10)* 0.001
if Q==3:
    br1=d1IT7
    br2=d2IT7
elif Q==4:
    br1=1.26*d1IT7
    br2=1.26*d2IT7
elif Q==5:
    br1=d1IT8
    br2=d2IT8
elif Q==6:
    br1=1.26*d1IT8
    br2=1.26*d2IT8
elif Q==7:
    br1=d1IT9
    br2=d2IT9
elif Q==8:
    br1=1.26*d1IT9
    br2=1.26*d2IT9
elif Q==9:
    br1=d1IT10
    br2=d2IT10
elif Q==10:
    br1=1.26*d1IT10
    br2=1.26*d2IT10

sn1=mn*(pi/2+2*xn1*tan(alphan))
print("公称(法向)齿厚sn1(mm)",sn1)
if wainiehe==1:sn2=mn*(pi/2+2*xn2*tan(alphan))
else:sn2=mn*(pi/2-2*xn2*tan(alphan))
print("公称(法向)齿厚sn2(mm)",sn2)
Tsn1=2*(Fr1**2+br1**2)**0.5*tan(alphan)
print("齿厚公差Tsn1(mm)",Tsn1)
Tsn2=2*(Fr2**2+br2**2)**0.5*tan(alphan)
print("齿厚公差Tsn2(mm)",Tsn2)
Esns1=-0.5*jbnmin/cos(alphan)
print("齿厚上极限偏差Esns1(mm)",Esns1)
Esns2=Esns1
print("齿厚上极限偏差Esns2(mm)",Esns2)
Esni1=Esns1-Tsn1
print("齿厚下极限偏差Esni1(mm)",Esni1)
Esni2=Esns2-Tsn2
print("齿厚下极限偏差Esni2(mm)",Esni2)

zp1=z1*inv(alphat)/inv(alphan)
zp2=z2*inv(alphat)/inv(alphan)
if k1==0:k1=round(zp1/pi*(((1+2*xn1/zp1)**2-(cos(alphan))**2)**0.5/cos(alphan)-2*xn1/zp1*tan(alphan)-inv(alphan))+0.5)
print("计算跨齿(槽)数k1",k1)
if k2==0:k2=round(zp2/pi*(((1+2*xn2/zp2)**2-(cos(alphan))**2)**0.5/cos(alphan)-2*xn2/zp2*tan(alphan)-inv(alphan))+0.5)
print("计算跨齿(槽)数k2",k2)
wxkn1=cos(alphan)*(pi*(k1-0.5)+zp1*inv(alphan))
wxkn2=cos(alphan)*(pi*(k2-0.5)+zp2*inv(alphan))
delwxn1=2*xn1*sin(alphan)
delwxn2=2*xn2*sin(alphan)
wkn1=(wxkn1+delwxn1)*mn
print("公法线长度wkn1(mm)",wkn1)
wkn2=(wxkn2+delwxn2)*mn
print("公法线长度wkn2(mm)",wkn2)
Ebns1=Esns1*cos(alphan)
print("公法线长度上极限偏差Ebns1(mm)",Ebns1)
Ebns2=Esns2*cos(alphan)
print("公法线长度上极限偏差Ebns2(mm)",Ebns2)
Ebni1=Esni1*cos(alphan)
print("公法线长度下极限偏差Ebni1(mm)",Ebni1)
Ebni2=Esni2*cos(alphan)
print("公法线长度下极限偏差Ebni2(mm)",Ebni2)

if dp==0:dp=1.44*mn
print("计算量柱(球)直径dp(mm)",dp)
if wainiehe==1:alpmt1=rinv(inv(alphat)+dp/mn/z1/cos(alphan)-pi/2/z1+2*xn1*tan(alphan)/z1)
else:alpmt1=rinv(inv(alphat)-dp/mn/z1/cos(alphan)+pi/2/z1+2*xn1*tan(alphan)/z1)
if wainiehe==1:alpmt2=rinv(inv(alphat)+dp/mn/z2/cos(alphan)-pi/2/z2+2*xn2*tan(alphan)/z2)
else:alpmt2=rinv(inv(alphat)-dp/mn/z2/cos(alphan)+pi/2/z2+2*xn2*tan(alphan)/z2)
if (z1 % 2)==0:
    if wainiehe==1:M1=mt*z1*cos(alphat)/cos(alpmt1)+dp
    else:M1=mt*z1*cos(alphat)/cos(alpmt1)-dp
else:
    if wainiehe==1:M1=mt*z1*cos(alphat)/cos(alpmt1)*cos(radians(90/z1))+dp
    else:M1=mt*z1*cos(alphat)/cos(alpmt1)*cos(radians(90/z1))-dp
print("跨距M1(mm)",M1)
if (z2 % 2)==0:
    if wainiehe==1:M2=mt*z2*cos(alphat)/cos(alpmt2)+dp
    else:M2=mt*z2*cos(alphat)/cos(alpmt2)-dp
else:
    if wainiehe==1:M2=mt*z2*cos(alphat)/cos(alpmt2)*cos(radians(90/z2))+dp
    else:M2=mt*z2*cos(alphat)/cos(alpmt2)*cos(radians(90/z2))-dp
print("跨距M2(mm)",M2)
if (z1 % 2)==0:
    Eyns1=Esns1*cos(alphat)/sin(alpmt1)/cos(betab)
    Eyni1=Esni1*cos(alphat)/sin(alpmt1)/cos(betab)
else:
    Eyns1=Esns1*cos(alphat)*cos(radians(90/z1))/sin(alpmt1)/cos(betab)
    Eyni1=Esni1*cos(alphat)*cos(radians(90/z1))/sin(alpmt1)/cos(betab)
print("量柱(球)测量跨距上极限偏差Eyns1(mm)",Eyns1)
print("量柱(球)测量跨距下极限偏差Eyni1(mm)",Eyni1)
if (z2 % 2)==0:
    Eyns2=Esns2*cos(alphat)/sin(alpmt2)/cos(betab)
    Eyni2=Esni2*cos(alphat)/sin(alpmt2)/cos(betab)
else:
    Eyns2=Esns2*cos(alphat)*cos(radians(90/z2))/sin(alpmt2)/cos(betab)
    Eyni2=Esni2*cos(alphat)*cos(radians(90/z2))/sin(alpmt2)/cos(betab)
print("量柱(球)测量跨距上极限偏差Eyns2(mm)",Eyns2)
print("量柱(球)测量跨距下极限偏差Eyni2(mm)",Eyni2)

delta1=pi/2/zv1+2*xn1*tan(alphan)/zv1
if wainiehe==1:delta2=pi/2/zv2+2*xn2*tan(alphan)/zv2
else:delta2=pi/2/zv2-2*xn2*tan(alphan)/zv2
hhan1=ha1+zv1*mn/2*(1-cos(delta1))
print("分度圆弦齿高hhan1(mm)",hhan1)
if wainiehe==1:hhan2=ha2+zv2*mn/2*(1-cos(delta2))
else:
    dela2=pi/2/z2-inv(alphat)-2*xn2*tan(alphat)/z2+inv(alphaat2)
    delhh2=da2/2*(1-cos(dela2))
    hhan2=ha2-zv2*mn/2*(1-cos(delta2))+delhh2
print("分度圆弦齿高hhan2(mm)",hhan2)
shn1=zv1*mn*sin(delta1)
print("分度圆弦齿厚shn1(mm)",shn1)
shn2=zv2*mn*sin(delta2)
print("分度圆弦齿厚shn2(mm)",shn2)

hhcn1=ha1-mn*(pi/8*sin(2*alphan)+xn1*(sin(alphan))**2)
print("固定弦齿高hhcn1(mm)",hhcn1)
if wainiehe==1:hhcn2=ha2-mn*(pi/8*sin(2*alphan)+xn2*(sin(alphan))**2)
else:hhcn2=ha2-mn*(pi/8*sin(2*alphan)+xn2*(sin(alphan))**2)+delhh2
print("固定弦齿高hhcn2(mm)",hhcn2)
shcn1=mn*(pi/2*(cos(alphan))**2+xn1*sin(2*alphan))
print("固定弦齿厚(法向弦齿厚)shcn1(mm)",shcn1)
if wainiehe==1:shcn2=mn*(pi/2*(cos(alphan))**2+xn2*sin(2*alphan))
else:shcn2=mn*(pi/2*(cos(alphan))**2-xn2*sin(2*alphan))
print("固定弦齿厚(法向弦齿厚)shcn2(mm)",shcn2)
Escns1=Esns1*(cos(alphan))**2
print("法向弦齿厚上极限偏差Escns1(mm)",Escns1)
Escns2=Esns2*(cos(alphan))**2
print("法向弦齿厚上极限偏差Escns2(mm)",Escns2)
Escni1=Esni1*(cos(alphan))**2
print("法向弦齿厚下极限偏差Escni1(mm)",Escni1)
Escni2=Esni2*(cos(alphan))**2
print("法向弦齿厚下极限偏差Escni2(mm)",Escni2)

dy1=d1+2*mn*xn1
print("测量位置dy1(mm)",dy1)
dy2=d2+2*mn*xn2
print("测量位置dy2(mm)",dy2)
bety1=atan(dy1/d1*tan(beta))
bety2=atan(dy2/d2*tan(beta))
alpyt1=acos(d1/dy1*cos(alphat))
alpyt2=acos(d2/dy2*cos(alphat))
syt1=dy1*(sn1/d1/cos(beta)+inv(alphat)-inv(alpyt1))
syt2=dy2*(sn2/d2/cos(beta)+inv(alphat)-inv(alpyt2))
syn1=syt1*cos(bety1)
syn2=syt2*cos(bety2)
dyn1=dy1-d1+d1/(cos(betab))**2
dyn2=dy2-d2+d2/(cos(betab))**2
sync1=dyn1*sin(syn1/dyn1)
print("弦齿厚sync1(mm)",sync1)
sync2=dyn2*sin(syn2/dyn2)
print("弦齿厚sync2(mm)",sync2)
hy1=(da1-dy1)/2
hy2=(da2-dy2)/2
hyc1=hy1+dyn1*(1-cos(syn1/dyn1))/2
print("弦齿顶高hyc1(mm)",hyc1)
hyc2=hy2+dyn2*(1-cos(syn2/dyn2))/2
print("弦齿顶高hyc2(mm)",hyc2)


print("---渐开线圆柱齿轮传动计算---")
import datetime
print("当前日期时间：" +datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

print("---输入基本参数---")
if wainiehe == 1:print("齿轮类型: 外齿轮")  
else:print("齿轮类型: 内齿轮")
print("法向模数mn(mm):",mn)
print("法向压力角alphan(°):",degrees(alphan))
print("螺旋角beta(°):",degrees(beta))
print("齿数z1:",z1)
print("齿数z2:",z2)
print("---输入其他参数---")
print("齿宽b(mm):",b)
print("法向齿顶高系数hanx:",hanx)
print("法向顶隙系数cnx:",cnx)
print("法向变位系数xn1:",xn1)
print("最小中心距ai(mm):",ai)
print("精度等级Q:",Q)

print("---计算基础参数---")
print("端面模数mt(mm):",mt)
print("端面压力角alphat(°):",degrees(alphat))
print("基圆螺旋角betab(°):",degrees(betab))
print("当量齿数zv1:",zv1)
print("当量齿数zv2:",zv2)
print("齿数比(传动比)u:",u)
print("分度圆直径d1(mm):",d1)
print("分度圆直径d2(mm):",d2)
print("基圆直径db1(mm):",db1)
print("基圆直径db2(mm):",db2)
print("未变位中心距a(mm):",a)

print("---渐开线圆柱齿轮几何尺寸计算---")
print("总变位系数xnsigma:",xnsigma)
print("变位系数xn2:",xn2)