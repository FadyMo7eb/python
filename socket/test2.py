name="kerolos"
age=12
rank=19
print("My name is %s and my age is %d and my rank is %d"%(name,age,rank))
print("My name is {} and my age is {} and my rank is {}".format(name,age,rank))
print(f"MY name is{name} and my age is {age} and my rank is {rank}")
print("My name is {:s} and my age is{:f} and my rank is {:.2f} ".format(name,age,rank))
#format with [old way,new way,3.6+versionof editor]
j="i love python"
print(j.upper())

jj="I LOVE KERO"
print(jj.lower())

u="i love kero"
print(u.title())

uu="i love 4g"
print(uu.capitalize())

c=(1,"kero",1)
print(c.count(1))

g="### I love kero ###"
print(g.strip("#"))

h="I love kero but i don't love kero kero kero kero kero"
print(len(h))

k="kero"
print(k.center(8,"#"))

kk="i LOVe kero"
print(kk.swapcase())

jkj="I love kero"
print(jkj.index("k"))

cc="kero"
print(cc.rjust(10))
print(cc.rjust(10,"@"))

#list[]
mylist=["kero","fady"]
mylist.append("Osama")
print(mylist)

gk=[1,-1,2,5,6,4]
gk.sort()
print(gk)

hj=["Kero","fady"]
kjkj=["alaa","ahmed"]
hj.extend(kjkj)
print(hj)

hjhjhj=["kero",1,2]
hjhjhj.remove(1)
print(hjhjhj)

fh=[1,2,3,4,5,6,7,8,9,10]
fh.reverse()
print(fh)

fhh=[1,2,3]
fhh.clear()
print(fhh)

v=[1,2,3]
ccc=v.copy()
print(v)
print(ccc)

fhfh=["kero","fady"]
print(fhfh.index("fady"))

fgh=["kero","fady"]
fgh.insert(0,"Alaa")
print(fgh)

#Tuples()
aa=(1,2)
bn=(2,3)
print(aa+bn)

#methods :
#index
#count
#Tuple destruct

#{set}
