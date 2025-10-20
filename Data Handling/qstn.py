import math
f=[67, 34,57,44,1,29,61,56]
list = sorted(f)
print(list)
sum_list=sum(list)
len_list=len(list)

mean = sum_list/len_list

a_list=[]
b_list=[]
c_list=[]
d_list=[]

print("Mean = ",sum_list,"/",len_list,"=",mean)
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

v = sumb/(len_list-1)
print("Sample Variance =",v)

sd = math.sqrt(v)
print("Standard Deviation is",sd)

print("SD^3 =",pow(sd,3))
print("SD^4 =",pow(sd,4))
sk=(sumc/((len_list-1)*pow(sd,3)))
print("Skewness =",sk)

k=(sumd/((len_list-1)*pow(sd,4)))
print("Kurtosis = ",k)

coe=(sd/mean)*100
print("The Coefficient of Variation = ",coe)

