import math
freq=[3,7,5,4,1]
x=[18,30,42,54,66]
fx=[54,210,210,216,66]

print("Frequency is =",freq)
print("fx =",fx)
n=sum(freq)
sfx=sum(fx)
sx=sum(x)

mean = sfx/n

a_list=[]
b_list=[]
c_list=[]
d_list=[]

print("Mean = ",sfx,"/",n,"=",mean)
##### 1 #####
print("[x-mean]")
for i in x:
    a = i-mean
    a_list.append(a)
    print(a)
suma = sum(a_list)
print("Summation of ^1 is",round(suma))
print("---------------")

##### 2 #####
print("[x-mean]^2")
for j in x:
    b = pow(j-mean,2)
    b_list.append(b)  
    print(b)
sumb = sum(b_list)
print("Summation of ^2 is",sumb)
print("---------------")

##### 3 #####
print("[x-mean]^3")
for k in x:
    c = pow(k-mean,3)
    c_list.append(c)
    print(c)
sumc = sum(c_list)
print("Summation of ^3 is",sumc)
print("---------------")

##### 4 #####
print("[x-mean]^4")
for l in x:
    d = pow(l-mean,4)
    d_list.append(d)
    print(d)
sumd = sum(d_list)
print("Summation of ^4 is",sumd)
print("---------------")


#fx(x-mean)^power

l1=[]
for m in range(len(freq)):
    l1.append(freq[m]*a_list[m])
print("f*(x-mean) is")
for m in range(len(l1)):
    print(l1[m])
print("Summmation is =",sum(l1))
print("----------------")

l2=[]
for m in range(len(freq)):
    l2.append(freq[m]*b_list[m])
print("f*(x-mean)^2 is")
for m in range(len(l2)):
    print(l2[m])
print("Summmation is =",sum(l2))
print("----------------")

l3=[]
for m in range(len(freq)):
    l3.append(freq[m]*c_list[m])
print("f*(x-mean)^3 is")
for m in range(len(l3)):
    print(l3[m])
print("Summmation is =",sum(l3))
print("----------------")

l4=[]
for m in range(len(freq)):
    l4.append(freq[m]*d_list[m])
print("f*(x-mean)^4 is")
for m in range(len(l4)):
    print(l4[m])
print("Summmation is =",sum(l4))
print("----------------")


#other calculations

#variance
v = sum(l2)/(n-1)
print("Sample Variance =",v)

#standard deviation
sd = math.sqrt(v)
print("Standard Deviation is",sd)

#skewness
print("SD^3 =",pow(sd,3))
print("SD^4 =",pow(sd,4))
sk=(sum(l3)/((n-1)*pow(sd,3)))
print("Skewness =",sk)

#kurtosis
k=(sum(l4)/((n-1)*pow(sd,4)))
print("Kurtosis = ",k)

#coefficient of variance
coe=(sd/mean)*100
print("The Coefficient of Variation = ",coe)

#mean deviation
abs_list=[]    #absolute value list
for i in l1:
    apnd=abs(i)
    abs_list.append(apnd)
print("")
print("Absolute Values for list (x-mean)")
for i in abs_list:
    print(i)
md = sum(abs_list)/n
print("Mean Deviation is ",sum(abs_list),"/",n,"=",md)
