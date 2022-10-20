import itertools

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Infinite iterators <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

 *** count => make a counter ex: count(start=n,step=n) it can be ifinite loop must put a condition >>> you can put anything count(tuple,list,dict)

# Program for creating a list of
# even and odd list of integers
# using count()


from itertools import count

# creates a count iterator object
iterator =(count(start = 0, step = 2))

# prints a odd list of integers
print("Even list:",
	list(next(iterator) for _ in range(5))) => 2,3,4,6

# creates a count iterator object
iterator = (count(start = 1, step = 2))

# prints a odd list of integers
print("Odd list:",
	list(next(iterator) for _ in range(5))) => 1,3,5,7


*** cycle => make a cycle of anything it can be infinite must put a condition it separate the thing and print it ex: cycle("fady")

import itertools
x=0
for i in itertools.cycle("fady"):
    print(i)
    x+=1
    if x==13:
        break



*** repeat => to repeat something a n of times ex: repeat(10,3) =>> 10,10,10

import itertools
for i in itertools.repeat(10,2):
    print(i)


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Iterators terminating on the shortest input sequence<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

*** accumulate => to accumulate the list , tuple with your opinion ex : accumulate([1,2,3,4,5]) =>>> 1,3,6,10,15

import itertools

import operator

print(list(itertools.accumulate([1,2,3,4,5,6],operator.mul))) return a multiple of numbers

print(list(itertools.accumulate([1,2,3,4,1,2,6],min))) it will be return the numbers but when apper a numer uder the last one =>> [1, 1, 1, 1, 1, 1, 1]

print(list(itertools.accumulate([1,2,3,4,1,2,6],max))) // / /////////////////////////////////////////////// upper /////////// =>> [1, 2, 3, 4, 4, 4, 6]

print(list(itertools.accumulate([1,2,3,4,5,6]))) to sum the numbers one by the behined =>> [1,3,6,10,15]

print(list(itertools.accumulate([1,2,3,4,5,6],initial=200))) it start from the initial number ==>> [200, 201, 203, 206, 210, 215, 221]


*** chain => it make for loop  the elements like list tuple ex : chain(list,tuple,...) ==>> elemet,......


*** chain.from_iterable(one_element) => to make a for loop into an elemet of the list , tuble ,... ex : cahin.from_iterable(list) ==>> e l e m e n t ......

*** compress => data selector you give him a list , tuple , .. and the list for selected places ex : compress( list , [1,0,0,0,1,1,0]) 1 or any num =>  for ture  0 => for false 

*** dropwhile => it check if the data follow the lambda fun one by one until it get false it stop ( it print the true elemets) ex :   dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1  || ex : dropwhile(lambda x : x <  5 ,[2,6,7,1,2,3] ) ---> 2  

*** filterfalse => like drowhile but it print the false value ex : print(*itertools.filterfalse(lambda x : x=="fady",["fady","is","here","so_don't_fuck_with_me"])) --> is here so_don't_fuck_with_me


*** groupby => to make groubs by key or delete repeted elements 

*** pairwise => to make like that [1,2,3,4] = 1,1 1,2 2,3 3,4 4,4 

*** starmap => fun to make it in iterators 

*** tee ( iter , n ) => tee to make a list number repeated

*** zip_longest(iterators,fillvalue='') => mix the iterators and the fillvalue will be as you like 

*** product (iteratos,repeat=n) => to mix the iterators and reapeat *n of them 

*** permutations(iterator,n) => split the eterator you give it into all mix and n is the length 

*** compination => like permutations

*** 






"""