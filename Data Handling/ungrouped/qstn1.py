import math

f = [65,76,78,80,85,88,93,95,96,118]
sum_list=sum(list)
n=len(list)

mean = sum_list/n

a_list=[]
b_list=[]
c_list=[]
d_list=[]
##### 1 #####
print("[x-mean]")
for i in list:
    a = i-mean
    a_list.append(a)
    print(a)
suma = sum(a_list)
print("Summation of ^1 is",round(suma))
print("---------------")

##### 2 #####
print("[x-mean]^2")
for j in list:
    b = pow(j-mean,2)
    b_list.append(b)  
    print(b)
sumb = sum(b_list)
print("Summation of ^2 is",sumb)
print("---------------")

##### 3 #####
print("[x-mean]^3")
for k in list:
    c = pow(k-mean,3)
    c_list.append(c)
    print(c)
sumc = sum(c_list)
print("Summation of ^3 is",sumc)
print("---------------")

##### 4 #####
print("[x-mean]^4")
for l in list:
    d = pow(l-mean,4)
    d_list.append(d)
    print(d)
sumd = sum(d_list)
print("Summation of ^4 is",sumd)
print("---------------")

#other calculations

#variantion
v = sumb/(n-1)
print("Sample Variance =",v)

#std dev
sd = math.sqrt(v)
print("Standard Deviation is",sd)

#skewness
print("SD^3 =",pow(sd,3))
print("SD^4 =",pow(sd,4))
sk=(sumc/((n-1)*pow(sd,3)))
print("Skewness =",sk)

#kurtosis
k=(sumd/((n-1)*pow(sd,4)))
print("Kurtosis = ",k)

#coefficient of variation
coe=(sd/mean)*100
print("The Coefficient of Variation = ",coe)

#mean deviation
abs_list=[]    #absolute value list
for i in a_list:
    apnd=abs(i)
    abs_list.append(apnd)
print("")
print("Absolute Values for list (x-mean)")
for i in abs_list:
    print(i)
md = sum(abs_list)/n
print("Mean Deviation is ",sum(abs_list),"/",n,"=",md)