#!/usr/bin/env python
# coding: utf-8

# In[10]:


# -*- coding: utf-8 -*- 


from z3 import * 

#import itertools 

c = [Bool('c%s' % (i)) for i in range(36)] 

 

#c[0]= 1 S, c[1 ]= 1 T1, c[2 ]= 1 T2,   c[3 ]= 1 T3,   c[4  ]= 1 b1, c[5  ]= 1 b2,  c[6  ]= 1 b3, c[7  ]= 1 z1 

#           c[8 ]= S T1, c[9 ]= S T2,   c[10]= S T3,   c[11]= S b1,  c[12]= S b2,   c[13]= S b3,  c[14]= S z1 

#                        c[15]=T1 T2,   c[16]=T1 T3,   c[17]=T1 b1,  c[18]=T1 b2,   c[19]=T1 b3,  c[20]=T1 z1 

#                                       c[21]=T2 T3,   c[22]=T2 b1,  c[23]=T2 b2,   c[24]=T2 b3,  c[25]=T2 z1 

#                                                      c[26]=T3 b1,  c[27]=T3 b2,   c[28]=T3 b3,  c[29]=T3 z1 

#                                                                    c[30]=b1 b2,   c[31]=b1 b3,  c[32]=b1 z1  

#                                                                                   c[33]=b2 b3, c[34]=b2 z1 

#                                                                                                c[35]=b3 z1 

 

s = Solver() # create a solver s 



#9 arbitrary phases
s.add(And(c[0]==True,c[4]==True,c[5]==True,c[6]==True,c[7]==True,c[11]==True,c[12]==True,c[13]==True,c[14]==True))
#Tachyon free conditions 

#T3{R} 

a = Xor(Xor(Xor(Xor(Xor(Xor(True,c[3]),c[16]),c[21]),c[26]),c[27]),c[28]) #xtilde proj
T3cond12 = Or(And(c[10], a),And(c[10], c[16]),And(c[10], c[21]),And(a, c[16]),And(a,c[21]),And(a, c[29]),And(c[16], c[21]),And(c[16],c[29]),And(c[21],c[29]))
T3cond3 = Implies(And(c[10],c[29]),Or(a,c[16],c[21]))

#T3cond1=c[10]+(1+c[3]+c[16]+c[21]+c[26]+c[27]+c[28])%2+c[16]+c[21]+c[29]!=1 
#T3cond2=c[10]+(1+c[3]+c[16]+c[21]+c[26]+c[27]+c[28])%2+c[16]+c[21]+c[29]!=0 
#T3cond3=Not(And(c[10]+(1+c[3]+c[16]+c[21]+c[26]+c[27]+c[28])%2+c[16]+c[21]+c[29]==2,c[10]+c[29]==2)) 

#T2{R} 
b = Xor(Xor(Xor(Xor(Xor(Xor(True,c[2]),c[15]),c[21]),c[22]),c[23]),c[24]) 
T2cond12 = Or(And(c[9], b), And(c[9], c[15]), And(c[9], c[21]), And(b, c[15]),And(b,c[21]),And(b, c[25]),And(c[15], c[21]),And(c[15],c[25]),And(c[21],c[25]))
T2cond3 = Implies(And(c[9],c[25]),Or(b,c[15],c[21]))

#T2cond1=c[9]+(1+c[2]+c[15]+c[21]+c[22]+c[23]+c[24])%2+c[15]+c[21]+c[25]!=1 
#T2cond2=c[9]+(1+c[2]+c[15]+c[21]+c[22]+c[23]+c[24])%2+c[15]+c[21]+c[25]!=0 
#T2cond3=Not(And(c[9]+(1+c[2]+c[15]+c[21]+c[22]+c[23]+c[24])%2+c[15]+c[21]+c[25]==2,c[9]+c[25]==2)) 

#T1{R} 
d = Xor(Xor(Xor(Xor(Xor(Xor(True,c[1]),c[15]),c[16]),c[17]),c[18]),c[19])
T1cond12 = Or(And(c[8], d),And(c[8], c[15]),And(c[8], c[16]),And(d, c[15]),And(d,c[16]),And(d, c[20]),And(c[15], c[16]),And(c[15],c[20]),And(c[16],c[20]))
T1cond3 = Implies(And(c[8],c[20]),Or(d,c[15],c[16]))

#T1cond1=c[8]+(1+c[1]+c[15]+c[16]+c[17]+c[18]+c[19])%2+c[15]+c[16]+c[20]!=1 
#T1cond2=c[8]+(1+c[1]+c[15]+c[16]+c[17]+c[18]+c[19])%2+c[15]+c[16]+c[20]!=0 
#T1cond3=Not(And(c[8]+(1+c[1]+c[15]+c[16]+c[17]+c[18]+c[19])%2+c[15]+c[16]+c[20]==2,c[8]+c[20]==2)) 

s.add(And(T1cond12,T1cond3,T2cond12,T2cond3,T3cond12,T3cond3)) 

z2tach=Or(Xor(Xor(c[30],c[31]),c[32]),Xor(Xor(c[30],c[33]),c[34]),Xor(Xor(c[31],c[33]),c[35]),Xor(Xor(c[32],c[34]),c[35]),       Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]))  

z2T1=Or(Xor(Xor(Xor(Xor(True,c[30]),c[31]),c[32]),c[17]),Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[15]),     Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[16]),Xor(Xor(Xor(c[32],c[34]),c[35]),c[20])) 

z2T2=Or(Xor(Xor(Xor(Xor(True,c[30]),c[33]),c[35]),c[28]),Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[16]),     Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[21]),Xor(Xor(Xor(c[32],c[34]),c[35]),c[25]))


z2T3=Or(Xor(Xor(Xor(Xor(True,c[31]),c[33]),c[35]),c[28]),Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[15]),     Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[21]),Xor(Xor(Xor(c[32],c[34]),c[35]),c[29]))

s.add(And(z2tach,z2T1,z2T2,z2T3))         

z1tach=Or(c[20],c[25],c[29],c[32],c[34],c[35]) 
z1T1tach=Or(Xor(Xor(True,c[32]),c[17]),Xor(c[25],c[15]),Xor(c[29],c[16]),Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[32]),c[34]),c[35]))
z1T2tach=Or(Xor(Xor(True,c[34]),c[23]),Xor(c[20],c[15]),Xor(c[29],c[21]),Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[32]),c[34]),c[35]))
z1T3tach=Or(Xor(Xor(True,c[35]),c[28]),Xor(c[20],c[16]),Xor(c[25],c[21]),Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[32]),c[34]),c[35])) 

s.add(And(z1tach,z1T1tach,z1T2tach,z1T3tach)) 


#Condition on having a 16/16bar 

#BF1=b1+pT2+qT3 
BF1Proj=Or(And(c[17],c[32],Xor(Xor(c[30],c[31]),c[32])),And(Xor(c[17],c[16]),Xor(c[32],c[29]),Xor(Xor(c[30],c[31]),c[32]),Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29])),And(Xor(c[17],c[15]),Xor(c[32],c[25]),Xor(Xor(c[30],c[31]),c[32]),Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25])),And(Xor(Xor(c[17],c[15]),c[16]),Xor(Xor(c[32],c[25]),c[29]),    Xor(Xor(c[30],c[31]),c[32]),Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29])))

#BF1Proj=[(c[17]+p*c[15]+q*c[16])%2+(c[32]+p*c[25]+q*c[29])%2+(c[30]+c[31]+c[32]+p*(c[2]+c[22]+c[23]+c[24]+c[25])+\
          #q*(c[3]+c[26]+c[27]+c[28]+c[29]))%2 for p in range(0,2) for q in range(0,2)] 
#BF1ProjBools=[x==3 for x in BF1Proj] 

#s.add(BF1Proj) 

# conditions on projection of twisted bosons: vectorials 

#V6= T1+T2 
e = Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[2]),c[17]),c[22]),c[18]),c[23]),c[19]),c[24]),c[20]),c[25]) #z2proj
V6cond1 = Implies(Xor(c[8],c[9]),Or(And(Xor(c[20],c[25]),Xor(c[16],c[21])),And(Xor(c[16],c[21]),e),And(Xor(c[20],c[25]),e)))

#V6cond1=Not(And((c[20]+c[25])%2+(c[16]+c[21])%2+(c[1]+c[2]+c[17]+c[22]+c[18]+c[23]+c[19]+c[24]+c[20]+c[25])%2+\
        #+(1+c[8]+c[9])%2<=1,(1+c[8]+c[9])%2==0))     
V6cond2 = Implies(And(Not(Xor(c[8],c[9])),Xor(c[20],c[25])),Or(Xor(c[16],c[21]),e))

#V6cond2=Not(And((c[20]+c[25])%2+(c[16]+c[21])%2+(c[1]+c[2]+c[17]+c[22]+c[18]+c[23]+c[19]+c[24]+c[20]+c[25])%2+\
        #+(1+c[8]+c[9])%2!=2,(1+c[8]+c[9])%2+(c[20]+c[25])%2==2)) 
V6cond3 = Implies(And(Not(Xor(c[8],c[9])),e),Or(Xor(c[20],c[25]),Xor(c[16],c[21])))
     

#V6cond3=Not(And((c[20]+c[25])%2+(c[16]+c[21])%2+(c[1]+c[2]+c[17]+c[22]+c[18]+c[23]+c[19]+c[24]+c[20]+c[25])%2+\
        #+(1+c[8]+c[9])%2!=2,(1+c[8]+c[9])%2+(c[1]+c[2]+c[17]+c[22]+c[18]+c[23]+c[19]+c[24]+c[20]+c[25])%2==2)) 

#V5= T1+T3 
f=Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[3]),c[17]),c[26]),c[18]),c[27]),c[19]),c[28]),c[20]),c[29])
V5cond1 = Implies(Xor(c[8],c[10]),Or(And(Xor(c[20],c[29]),Xor(c[15],c[21])),And(Xor(c[15],c[21]),f),And(Xor(c[20],c[29]),f)))

V5cond2 = Implies(And(Not(Xor(c[8],c[10])),Xor(c[20],c[29])),Or(Xor(c[15],c[21]),f))

V5cond3 = Implies(And(Not(Xor(c[8],c[10])),f),Or(Xor(c[20],c[29]),Xor(c[15],c[21])))

#V5cond1=Not(And((c[20]+c[29])%2+(c[15]+c[21])%2+(c[1]+c[3]+c[17]+c[26]+c[18]+c[27]+c[19]+c[28]+c[20]+c[29])%2+\
        #+(1+c[8]+c[10])%2<=1, (1+c[8]+c[10])%2==0)) 
#V5cond2=Not(And((c[20]+c[29])%2+(c[15]+c[21])%2+(c[1]+c[3]+c[17]+c[26]+c[18]+c[27]+c[19]+c[28]+c[20]+c[29])%2+\
        #+(1+c[8]+c[10])%2!=2, (1+c[8]+c[10])%2+(c[20]+c[29])%2==2)) 
#V5cond3=Not(And((c[20]+c[29])%2+(c[15]+c[21])%2+(c[1]+c[3]+c[17]+c[26]+c[18]+c[27]+c[19]+c[28]+c[20]+c[29])%2+\
        #+(1+c[8]+c[10])%2!=2, (1+c[8]+c[10])%2+(c[1]+c[3]+c[17]+c[26]+c[18]+c[27]+c[19]+c[28]+c[20]+c[29])%2==2)) 

#V4= T2+T3 
g=Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[3]),c[22]),c[26]),c[23]),c[27]),c[24]),c[28]),c[25]),c[29])
V4cond1 = Implies(Xor(c[9],c[10]),Or(And(Xor(c[25],c[29]),Xor(c[15],c[16])),And(Xor(c[15],c[16]),g),And(Xor(c[25],c[29]),g)))

V4cond2 = Implies(And(Not(Xor(c[9],c[10])),Xor(c[25],c[29])),Or(Xor(c[15],c[16]),g))

V4cond3 = Implies(And(Not(Xor(c[9],c[10])),g),Or(Xor(c[25],c[29]),Xor(c[15],c[16])))

#V4cond1=Not(And((c[25]+c[29])%2+(c[15]+c[16])%2+(c[2]+c[3]+c[22]+c[26]+c[23]+c[27]+c[24]+c[28]+c[25]+c[29])%2\
#        +(1+c[9]+c[10])%2<=1,(1+c[9]+c[10])%2==0)) 
#V4cond2=Not(And((c[25]+c[29])%2+(c[15]+c[16])%2+(c[2]+c[3]+c[22]+c[26]+c[23]+c[27]+c[24]+c[28]+c[25]+c[29])%2+\
#        +(1+c[9]+c[10])%2==2, (1+c[9]+c[10])%2+(c[25]+c[29])%2==2)) 
#V4cond3=Not(And((c[25]+c[29])%2+(c[15]+c[16])%2+(c[2]+c[3]+c[22]+c[26]+c[23]+c[27]+c[24]+c[28]+c[25]+c[29])%2+\
#        +(1+c[9]+c[10])%2==2, (1+c[9]+c[10])%2+(c[2]+c[3]+c[22]+c[26]+c[23]+c[27]+c[24]+c[28]+c[25]+c[29])%2==2)) 

s.add(And(V4cond1,V4cond2,V4cond3,V5cond1,V5cond2,V5cond3,V6cond1,V6cond2,V6cond3)) 


#V3= b_1+b_2+T3 +pT1+qT2= chi^... [y/w] eta^12 {lambda_R^a}
m=Xor(Xor(c[32],c[34]),c[29])
n=Xor(Xor(c[26],c[27]),c[3])

o00=Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[31]),c[33]),c[32]),c[34])
o01=Xor(Xor(Xor(Xor(Xor(o00,c[2]),c[22]),c[23]),c[24]),c[25])
o10=Xor(Xor(Xor(Xor(Xor(o00,c[1]),c[17]),c[18]),c[19]),c[20])
o11=Xor(Xor(Xor(Xor(Xor(o10,c[2]),c[22]),c[23]),c[24]),c[25])

p00=Xor(Xor(c[31],c[33]),c[28])
p01=Xor(Xor(Xor(Xor(Xor(p00,c[24]),c[22]),c[23]),c[21]),c[2])
p10=Xor(Xor(Xor(Xor(Xor(p00,c[19]),c[17]),c[18]),c[16]),c[1])
p11=Xor(Xor(Xor(Xor(Xor(Xor(p10,c[15]),c[22]),c[23]),c[21]),c[15]),c[2]) # two c[15]s...

V3_00cond1=Not(And(m,n,Not(o00),Not(p00)))
V3_00cond2=Not(And(Not(m),Not(n),Not(o00),Not(p00)))
V3_00cond3=Not(And(Not(m),n,o00,Not(p00)))
V3_00cond4=Not(And(Not(m),n,Not(o00),p00))

V3_01cond1=Not(And(Xor(m,c[25]),Xor(n,c[21]),Not(o01),Not(p01)))
V3_01cond2=Not(And(Not(Xor(m,c[25])),Not(Xor(n,c[21])),Not(o01),Not(p01)))
V3_01cond3=Not(And(Not(Xor(m,c[25])),Xor(n,c[21]),o01,Not(p01)))
V3_01cond4=Not(And(Not(Xor(m,c[25])),Xor(n,c[21]),Not(o01),p01))

h=Xor(m,c[20])
i=Xor(n,c[16])

V3_10cond1=Not(And(h,i,Not(o10),Not(p10)))
V3_10cond2=Not(And(Not(h),Not(i),Not(o10),Not(p10)))
V3_10cond3=Not(And(Not(h),i,o10,Not(p10)))
V3_10cond4=Not(And(Not(h),i,Not(o10),p10))

V3_11cond1=Not(And(Xor(h,c[25]),Xor(i,c[21]),Not(o11),Not(p11)))
V3_11cond2=Not(And(Not(Xor(h,c[25])),Not(Xor(i,c[21])),Not(o11),Not(p11)))
V3_11cond3=Not(And(Not(Xor(h,c[25])),Xor(i,c[21]),o11,Not(p11)))
V3_11cond4=Not(And(Xor(h,c[25]),Xor(i,c[21]),Not(o11),p11))

#V3proj=[(c[32]+c[34]+c[29]+p*c[20]+q*c[25])%2+(c[26]+c[27]+1+c[3]+p*c[16]+q*c[21])%2 +\
        #(c[3]+c[26]+c[27]+c[28]+c[29]+c[31]+c[33]+c[32]+c[34]+p*(c[1]+c[17]+c[18]+c[19]+c[20])+ \
         #q*(c[2]+c[22]+c[23]+c[24]+c[25]))%2 +\
         #(p+q+c[31]+c[33]+c[28]+p*c[19]+q*c[24]+p*(c[17]+c[18]+c[16]+1+c[1]+q*c[15])+\
          #q*(c[22]+c[23]+c[21]+p*c[15]+1+c[2]))%2!=1 for p in range(0,2) for q in range(0,2)] 


#V2= b_1+b_3+T2 +pT1+qT3= chi^... [y/w] eta^13 {lambda_R^a} 
q = Xor(Xor(c[32],c[35]),c[25])
r = Xor(Xor(c[22],c[24]),c[2])
z00 = Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[30]),c[33]),c[32]),c[35])
z01 = Xor(Xor(Xor(Xor(Xor(z00,c[3]),c[26]),c[27]),c[28]),c[29])
z10 = Xor(Xor(Xor(Xor(Xor(z00,c[1]),c[17]),c[18]),c[19]),c[20])
z11 = Xor(Xor(Xor(Xor(Xor(z10,c[3]),c[26]),c[27]),c[28]),c[29])

t00 = Xor(Xor(c[30],c[33]),c[23])
t01 = Xor(Xor(Xor(Xor(Xor(t00,c[27]),c[26]),c[28]),c[21]),c[3])
t10 = Xor(Xor(Xor(Xor(Xor(t00,c[18]),c[17]),c[19]),c[15]),c[1])
t11 = Xor(Xor(Xor(Xor(Xor(Xor(t10,c[27]),c[26]),c[28]),c[21]),c[16]),c[3])

V2_00cond1=Not(And(q,r,Not(z00),Not(t00)))
V2_00cond2=Not(And(Not(q),Not(r),Not(z00),Not(t00)))
V2_00cond3=Not(And(Not(q),r,z00,Not(t00)))
V2_00cond4=Not(And(Not(q),r,Not(z00),t00))

V2_01cond1=Not(And(Xor(q,c[29]),Xor(r,c[21]),Not(z01),Not(t01)))
V2_01cond2=Not(And(Not(Xor(q,c[29])),Not(Xor(r,c[21])),Not(z01),Not(t01)))
V2_01cond3=Not(And(Not(Xor(q,c[29])),Xor(r,c[21]),z01,Not(t01)))
V2_01cond4=Not(And(Not(Xor(q,c[29])),Xor(r,c[21]),Not(z01),t01))

V2_10cond1=Not(And(Xor(q,c[20]),Xor(r,c[15]),Not(z10),Not(t10)))
V2_10cond2=Not(And(Not(Xor(q,c[20])),Not(Xor(r,c[15])),Not(z10),Not(t10)))
V2_10cond3=Not(And(Not(Xor(q,c[20])),Xor(r,c[15]),z10,Not(t10)))
V2_10cond4=Not(And(Not(Xor(q,c[20])),Xor(r,c[15]),Not(z10),t10))

V2_11cond1=Not(And(Xor(Xor(q,c[20]),c[29]),Xor(Xor(r,c[15]),c[21]),Not(z11),Not(t11)))
V2_11cond2=Not(And(Not(Xor(Xor(q,c[20]),c[29])),Not(Xor(Xor(r,c[15]),c[21])),Not(z11),Not(t11)))
V2_11cond3=Not(And(Not(Xor(Xor(q,c[20]),c[29])),Xor(Xor(r,c[15]),c[21]),z11,Not(t11)))
V2_11cond4=Not(And(Not(Xor(Xor(q,c[20]),c[29])),Xor(Xor(r,c[15]),c[21]),Not(z11),t11))

#V2proj=[(c[32]+c[35]+c[25]+p*c[20]+q*c[29])%2+(c[22]+c[24]+1+c[2]+p*c[15]+q*c[21])%2 +\
#        (c[2]+c[22]+c[23]+c[24]+c[25]+c[30]+c[33]+c[32]+c[35]+p*(c[1]+c[17]+c[18]+c[19]+c[20])+ \
#         q*(c[3]+c[26]+c[27]+c[28]+c[29]))%2 +\
#         (p+q+c[30]+c[33]+c[23]+p*c[18]+q*c[27]+p*(c[17]+c[19]+c[15]+1+c[1]+q*c[16])+\
#          q*(c[26]+c[28]+c[21]+p*c[16]+1+c[3]))%2!=1 for p in range(0,2) for q in range(0,2)] 

 

#V1= b_2+b_3+T1 +pT2+qT3= chi^... [y/w] eta^23 {lambda_R^a} 
u = Xor(Xor(c[34],c[35]),c[20]) #+p*c[25]+q*c[29])
v = Xor(Xor(Xor(c[18],c[19]),True),c[1]) #+p*c[15]+q*c[16])
w00 = Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[30]),c[31]),c[34]),c[35])
w01 = Xor(Xor(Xor(Xor(Xor(w00,c[3]),c[26]),c[27]),c[28]),c[29])
w10 = Xor(Xor(Xor(Xor(Xor(w00,c[2]),c[22]),c[23]),c[24]),c[25])
w11 = Xor(Xor(Xor(Xor(Xor(w10,c[3]),c[26]),c[27]),c[28]),c[29])
x00 = Xor(Xor(c[30],c[31]),c[17])
x01 = Xor(Xor(Xor(Xor(Xor(Xor(x00,c[26]),c[27]),c[28]),c[16]),True),c[3])
x10 = Xor(Xor(Xor(Xor(Xor(Xor(x00,c[22]),c[23]),c[24]),c[15]),True),c[2])
x11 = Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(x10,c[21]),c[26]),c[27]),c[28]),c[16]),c[21]),True),c[3])

V1_00cond1 = Not(And(u,Not(v),Not(w00),Not(x00)))
V1_00cond2 = Not(And(Not(u),v,Not(w00),Not(x00)))
V1_00cond3 = Not(And(Not(u),Not(v),w00,Not(x00)))
V1_00cond4 = Not(And(Not(u),Not(v),Not(w00),x00))

V1_01cond1 = Not(And(Xor(u,c[29]),Not(Xor(v,c[16])),Not(w01),Not(x01)))
V1_01cond2 = Not(And(Not(Xor(u,c[29])),Xor(v,c[16]),Not(w01),Not(x01)))
V1_01cond3 = Not(And(Not(Xor(u,c[29])),Not(Xor(v,c[16])),w01,Not(x01)))
V1_01cond4 = Not(And(Not(Xor(u,c[29])),Not(Xor(v,c[16])),Not(w01),x01))

V1_10cond1 = Not(And(Xor(u,c[25]),Not(Xor(v,c[15])),Not(w10),Not(x10)))
V1_10cond2 = Not(And(Not(Xor(u,c[25])),Xor(v,c[15]),Not(w10),Not(x10)))
V1_10cond3 = Not(And(Not(Xor(u,c[25])),Not(Xor(v,c[15])),w10,Not(x10)))
V1_10cond4 = Not(And(Not(Xor(u,c[25])),Not(Xor(v,c[15])),Not(w10),x10))

V1_11cond1 = Not(And(Xor(Xor(u,c[25]),c[29]),Not(Xor(Xor(v,c[15]),c[16])),Not(w11),Not(x11)))
V1_11cond2 = Not(And(Not(Xor(Xor(u,c[25]),c[29])),Xor(Xor(v,c[15]),c[16]),Not(w11),Not(x11)))
V1_11cond3 = Not(And(Not(Xor(Xor(u,c[25]),c[29])),Not(Xor(Xor(v,c[15]),c[16])),w11,Not(x11)))
V1_11cond4 = Not(And(Not(Xor(Xor(u,c[25]),c[29])),Not(Xor(Xor(v,c[15]),c[16])),Not(w11),x11))

#V1proj=[(c[34]+c[35]+c[20]+p*c[25]+q*c[29])%2+(c[18]+c[19]+1+c[1]+p*c[15]+q*c[16])%2 +\
#        (c[1]+c[17]+c[18]+c[19]+c[20]+c[30]+c[31]+c[34]+c[35]+p*(c[2]+c[22]+c[23]+c[24]+c[25])+ \
#         q*(c[3]+c[26]+c[27]+c[28]+c[29]))%2 +\
#         (p+q+c[30]+c[31]+c[17]+p*c[22]+q*c[26]+p*(c[23]+c[24]+c[15]+1+c[2]+q*c[21])+\
#          q*(c[27]+c[28]+c[16]+p*c[21]+1+c[3]))%2!=1 for p in range(0,2) for q in range(0,2)] 

s.add(V1_00cond1)
s.add(V1_00cond2)
s.add(V1_00cond3)
s.add(V1_00cond4)
s.add(V1_01cond1)
s.add(V1_01cond2)
s.add(V1_01cond3)
s.add(V1_01cond4)
s.add(V1_10cond1,V1_10cond2,V1_10cond3,V1_10cond4,V1_11cond1,V1_11cond2,V1_11cond3,V1_11cond4) 
s.add(V2_00cond1,V2_00cond2,V2_00cond3,V2_00cond4,V2_01cond1,V2_01cond2,V2_01cond3,V2_01cond4)
s.add(V2_10cond1,V2_10cond2,V2_10cond3,V2_10cond4,V2_11cond1,V2_11cond2,V2_11cond3,V2_11cond4) 
s.add(V3_00cond1,V3_00cond2,V3_00cond3,V3_00cond4,V3_01cond1,V3_01cond2,V3_01cond3,V3_01cond4)
s.add(V3_10cond1,V3_10cond2,V3_10cond3,V3_10cond4,V3_11cond1,V3_11cond2,V3_11cond3,V3_11cond4) 
# conditions on projection of twisted bosons: spinorials 

#B12=1+b1+b2+b3+z1+T1+T2=z2+T1+T2 

B12proj=Or(Xor(Xor(Xor(Xor(c[32],c[34]),c[35]),c[20]),c[25]),Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[16]),c[21]),c[26]),c[27]),c[28]),c[29]))

#B11=1+b1+b2+b3+z1+T1+T3=z2+T1+T3 

B11proj=Or(Xor(Xor(Xor(Xor(c[32],c[34]),c[35]),c[20]),c[29]),Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[15]),c[21]),c[22]),c[23]),c[24]),c[25])) 

#B10=1+b1+b2+b3+z1+T2+T3=z2+T2+T3 

B10proj=Or(Xor(Xor(Xor(Xor(c[32],c[34]),c[35]),c[25]),c[29]),Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[15]),c[16]),c[17]),c[18]),c[19]),c[20])) 

s.add(And(B10proj,B11proj,B12proj))
 

#B9=1+b3+T3+z1+pT1+qT2  
B9proj_00=Or(Xor(Xor(c[28],True),c[29]),Xor(c[35],c[29]),Xor(Xor(True,c[28]),c[35]))
B9proj_01=Or(Xor(Xor(Xor(c[28],True),c[29]),c[21]),Xor(Xor(c[35],c[29]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[28],c[35]),c[24]),c[2]),c[24]),c[21]),c[25]),True),c[2]))
B9proj_10=Or(Xor(Xor(Xor(c[28],True),c[29]),c[16]),Xor(Xor(c[35],c[29]),c[20]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[28],c[35]),c[19]),c[1]),c[19]),c[16]),c[20]),True),c[1]))
B9proj_11=Or(Xor(Xor(Xor(Xor(c[28],True),c[29]),c[16]),c[21]),Xor(Xor(Xor(c[35],c[29]),c[20]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[28]),c[35]),c[19]),c[1]),c[19]),c[16]),c[20]),True),c[1]),        c[15]),c[24]),c[2]),c[24]),c[21]),c[25]),c[15]),True),c[2]))

#B9proj_pq=[(c[28]+1+c[29]+p*c[16]+q*c[21])%2+(c[35]+c[29]+p*c[20]+q*c[25])%2 + \
        #(1+p+q+c[28]+c[35]+p*c[19]+q*c[24]+p*(c[1]+c[19]+c[16]+c[20]+(1+c[1])+q*c[15])+q*(c[2]+c[24]+c[21]+c[25]+p*c[15]+(1+c[2])))%2!=0 \
        #for p in range(0,2) for q in range(0,2)] 

#B8=1+b2+T2+z1+pT1+qT3  
B8proj_00=Or(Xor(Xor(c[23],True),c[25]),Xor(c[34],c[25]),Xor(True,c[23],c[34]))
B8proj_01=Or(Xor(Xor(Xor(c[23],True),c[25]),c[21]),Xor(Xor(c[34],c[25]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[23],c[34]),c[24]),c[2]),c[24]),c[21]),c[25]),True),c[2]))
B8proj_10=Or(Xor(Xor(Xor(c[23],True),c[25]),c[15]),Xor(Xor(c[34],c[25]),c[20]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[23],c[34]),c[18]),c[1]),c[18]),c[15]),c[20]),True),c[1]))
B8proj_11=Or(Xor(Xor(Xor(Xor(c[23],True),c[25]),c[15]),c[21]),Xor(Xor(Xor(c[34],c[25]),c[20]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[23],c[34]),c[18]),c[1]),c[18]),c[15]),c[20]),True),c[1]),        c[16]),c[27]),c[3]),c[27]),c[21]),c[29]),c[16]),True),c[3]))


#B8proj_pq=[(c[23]+1+c[25]+p*c[15]+q*c[21])%2+(c[34]+c[25]+p*c[20]+q*c[29])%2 + \
#           (1+p+q+c[23]+c[34]+p*c[18]+q*c[27]+p*(c[1]+c[18]+c[15]+c[20]+(1+c[1])+q*c[16])+q*(c[3]+c[27]+c[21]+c[29]+p*c[16]+(1+c[3])))%2!=0 \
#           for p in range(0,2) for q in range(0,2)] 


#B7=1+b1+T1+z1+pT2+qT3  
B7proj_00=Or(Xor(Xor(c[17],True),c[20]),Xor(c[32],c[20]),Xor(True,c[17]),c[32])
B7proj_01=Or(Xor(Xor(Xor(c[17],True),c[20]),c[16]),Xor(Xor(c[32],c[20]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[17],c[32]),c[26]),c[3]),c[26]),c[16]),c[29]),True),c[3]))
B7proj_10=Or(Xor(Xor(Xor(c[17],True),c[20]),c[15]),Xor(Xor(c[32],c[20]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[17],c[32]),c[22]),c[2]),c[22]),c[15]),c[25]),True),c[2]))
B7proj_11=Or(Xor(Xor(Xor(Xor(c[17],True),c[20]),c[15]),c[16]),Xor(Xor(Xor(c[32],c[20]),c[25]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[17]),c[32]),c[22]),c[26]),c[2]),c[22]),c[15]),c[25]),c[2]),        c[21]),c[3]),c[26]),c[16]),c[29]),c[21]),c[3]))


#B7proj_pq=[(c[17]+1+c[20]+p*c[15]+q*c[16])%2+(c[32]+c[20]+p*c[25]+q*c[29])%2 + \
#        (1+p+q+c[17]+c[32]+p*c[22]+q*c[26]+p*(c[2]+c[22]+c[15]+c[25]+(1+c[2])+q*c[21])+q*(c[3]+c[26]+c[16]+c[29]+p*c[21]+(1+c[3])))%2!=0 \
#        for p in range(0,2) for q in range(0,2)] 
   

s.add(B7proj_00,B7proj_01,B7proj_10,B7proj_11) 
s.add(B8proj_00,B8proj_01,B8proj_10,B8proj_11) 
s.add(B9proj_00,B9proj_01,B9proj_10,B9proj_11) 

#B6=z1+T1+T2 

B6proj=Or(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[2]),c[32]),c[17]),c[22]),c[34]),c[18]),c[23]),c[35]),c[19]),c[24]),c[20]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[32],c[17]),c[22]),c[34]),c[18]),c[23]),c[35]),c[19]),c[24]),c[20]),c[1]),c[25]),c[2]),        Xor(Xor(c[29],c[16]),c[21]))


#B5=z1+T1+T3 

B5proj=Or(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[3]),c[32]),c[17]),c[26]),c[34]),c[18]),c[27]),c[35]),c[19]),c[28]),c[20]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[32],c[17]),c[26]),c[34]),c[18]),c[27]),c[35]),c[19]),c[28]),c[20]),c[1]),c[29]),c[3]),        Xor(Xor(c[25],c[15]),c[21]))

#B4=z1+T2+T3 

B4proj=Or(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[3]),c[32]),c[22]),c[26]),c[34]),c[23]),c[27]),c[35]),c[24]),c[28]),c[25]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[32],c[22]),c[26]),c[34]),c[23]),c[27]),c[35]),c[24]),c[28]),c[25]),c[2]),c[29]),c[3]),        Xor(Xor(c[20],c[15]),c[16]))


s.add(And(B4proj,B5proj,B6proj)) 

#B3 b1+b2+z1+T3+pT1+qT2 
B3proj_00 = Or(Xor(Xor(Xor(Xor(c[26],c[27]),c[29]),True),c[3]),Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[31]),c[33]),c[35]),        Xor(Xor(Xor(Xor(True,c[31]),c[33]),c[35]),c[28]))
B3proj_01 = Or(Xor(Xor(Xor(Xor(Xor(c[26],c[27]),c[29]),True),c[3]),c[21]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[31]),c[33]),c[35]),c[2]),c[22]),c[23]),c[24]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[31]),c[33]),c[35]),c[28]),c[24]),c[22]),c[23]),c[25]),c[21]),True),c[2]))
B3proj_10 = Or(Xor(Xor(Xor(Xor(Xor(c[26],c[27]),c[29]),True),c[3]),c[16]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[31]),c[33]),c[35]),c[1]),c[17]),c[18]),c[19]),c[20]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[31]),c[33]),c[35]),c[28]),c[19]),c[17]),c[18]),c[20]),c[16]),True),c[1]))
B3proj_11 = Or(Xor(Xor(Xor(Xor(c[26],c[27]),c[29]),True),c[3]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[3],c[26]),c[27]),c[28]),c[29]),c[31]),c[33]),c[35]),                c[1]),c[17]),c[18]),c[19]),c[20]),c[2]),c[22]),c[23]),c[24]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[31]),c[33]),c[35]),c[28]),c[19]),c[24]),c[17]),c[18]),c[20]),c[16]),True),c[1]),                c[15]),c[22]),c[23]),c[25]),c[21]),c[15]),True),c[2]))


#B3proj_pq=[(c[26]+c[27]+c[29]+1+c[3]+p*c[16]+q*c[21])%2+ \
#      (c[3]+c[26]+c[27]+c[28]+c[29]+c[31]+c[33]+c[35]+p*(c[1]+c[17]+c[18]+c[19]+c[20])+q*(c[2]+c[22]+c[23]+c[24]+c[25]))%2 + \
#      (1+p+q+c[31]+c[33]+c[35]+c[28]+p*c[19]+q*c[24]+p*(c[17]+c[18]+c[20]+c[16]+1+c[1]+q*c[15])+ \
#      q*(c[22]+c[23]+c[25]+c[21]+p*c[15]+1+c[2]))%2!=0  for p in range(0,2) for q in range(0,2) ]
     

#B2 b1+b3+z1+T2+pT1+qT3 

#B2proj_pq=[(c[22]+c[24]+c[25]+1+c[2]+p*c[15]+q*c[21])%2+ \
#      (c[2]+c[22]+c[23]+c[24]+c[25]+c[30]+c[33]+c[34]+p*(c[1]+c[17]+c[18]+c[19]+c[20])+q*(c[3]+c[26]+c[27]+c[28]+c[29]))%2 + \
#      (1+p+q+c[30]+c[33]+c[34]+c[23]+p*c[18]+q*c[27]+p*(c[17]+c[19]+c[20]+c[15]+1+c[1]+q*c[16])+ \
#       q*(c[26]+c[28]+c[29]+c[21]+p*c[16]+1+c[3]))%2!=0  for p in range(0,2) for q in range(0,2) ] 


B2proj_00 = Or(Xor(Xor(Xor(Xor(c[22],c[24]),c[25]),True),c[2]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[30]),c[33]),c[34]),        Xor(Xor(Xor(Xor(True,c[30]),c[33]),c[34]),c[23]))
B2proj_01 = Or(Xor(Xor(Xor(Xor(Xor(c[22],c[24]),c[25]),True),c[2]),c[21]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[30]),c[33]),c[34]),c[3]),c[26]),c[27]),c[28]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[33]),c[34]),c[23]),c[27]),c[26]),c[28]),c[29]),c[21]),True),c[3]))
B2proj_10 = Or(Xor(Xor(Xor(Xor(Xor(c[22],c[24]),c[25]),True),c[2]),c[15]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[30]),c[33]),c[34]),c[1]),c[17]),c[18]),c[19]),c[20]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[33]),c[34]),c[23]),c[18]),c[17]),c[19]),c[20]),c[15]),True),c[1]))
B2proj_11 = Or(Xor(Xor(Xor(Xor(Xor(Xor(c[22],c[24]),c[25]),True),c[2]),c[15]),c[21]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[2],c[22]),c[23]),c[24]),c[25]),c[30]),c[33]),c[34]),c[1]),c[17]),                c[18]),c[19]),c[20]),c[3]),c[26]),c[27]),c[28]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[33]),c[34]),c[23]),c[18]),c[17]),c[19]),c[20]),c[15]),c[1]),                c[27]),c[26]),c[28]),c[29]),c[21]),c[3]))
# B1=b2+b3+z1+T1+pT2+qT3 
B1proj_00 = Or(Xor(Xor(Xor(Xor(c[18],c[19]),c[20]),True),c[1]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[30]),c[31]),c[32]),        Xor(Xor(Xor(Xor(True,c[30]),c[31]),c[32]),c[17]))
B1proj_01 = Or(Xor(Xor(Xor(Xor(Xor(c[18],c[19]),c[20]),True),c[1]),c[16]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[30]),c[31]),c[32]),c[3]),c[26]),c[27]),c[28]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[31]),c[32]),c[17]),c[26]),c[27]),c[28]),c[29]),c[16]),True),c[3]))
B1proj_10 = Or(Xor(Xor(Xor(Xor(Xor(c[18],c[19]),c[20]),True),c[1]),c[15]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[30]),c[31]),c[32]),c[2]),c[22]),c[23]),c[24]),c[25]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[31]),c[32]),c[17]),c[22]),c[23]),c[24]),c[25]),c[15]),True),c[2]))
B1proj_11 = Or(Xor(Xor(Xor(Xor(Xor(Xor(c[18],c[19]),c[20]),True),c[1]),c[15]),c[16]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(c[1],c[17]),c[18]),c[19]),c[20]),c[30]),c[31]),c[32]),c[2]),c[22]),        c[23]),c[24]),c[25]),c[3]),c[26]),c[27]),c[28]),c[29]),        Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(Xor(True,c[30]),c[31]),c[32]),c[17]),c[22]),c[23]),c[24]),c[25]),c[15]),True),c[2]),        c[21]),c[26]),c[27]),c[28]),c[29]),c[16]),c[21]),True),c[3]))

#B1proj_pq=[(c[18]+c[19]+c[20]+1+c[1]+p*c[15]+q*c[16])%2+ \
#      (c[1]+c[17]+c[18]+c[19]+c[20]+c[30]+c[31]+c[32]+p*(c[2]+c[22]+c[23]+c[24]+c[25])+q*(c[3]+c[26]+c[27]+c[28]+c[29]))%2 + \
#      (1+p+q+c[30]+c[31]+c[32]+c[17]+p*c[22]+q*c[26]+p*(c[23]+c[24]+c[25]+c[15]+1+c[2]+q*c[21])+q*(c[27]+c[28]+c[29]+c[16]+p*c[21]+1+c[3]))%2!=0 \
#          for p in range(0,2) for q in range(0,2) ] 

#B1projBools=[x==0 for x in B1proj_pq] 

 

s.add(B1proj_00,B1proj_01,B1proj_10,B1proj_11)
s.add(B2proj_00,B2proj_01,B2proj_10,B2proj_11)
s.add(B3proj_00,B3proj_01,B3proj_10,B3proj_11) 

 
#print(s.sexpr())
import timeit
import json 
start1 = timeit.default_timer()
print(s.check()) 
stop1 = timeit.default_timer()
print("Time to check sat:", stop1 - start1)
start2 = timeit.default_timer()

#from time import time
#t1 = time()



while s.check() == sat: 

    m = s.model () 
    
    if not m: 

        break 
    
    f = open('TestBoolType0bar2.txt','a')

    old_stdout = sys.stdout  #  store the default system handler to be able to restore it 

    sys.stdout = f 
    #t2 = time()
    #elapsed = t2 - t1
    #print(elapsed) # Print elapsed time
    print([m[c[i]] for i in range(36)])
    #print(type(modl))
    
    f.close() 

    sys.stdout=old_stdout
    
    #print(sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))) 
    #print(sorted ([(m[d]) for d in m], key = lambda x: str(x[0]))) 

    s.add(Not(And([v() == m[v] for v in m]))) 
    
stop2 = timeit.default_timer()
print("Time to get solns:", stop2 - start2)


 


# In[ ]:


30.3

