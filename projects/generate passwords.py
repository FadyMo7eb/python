import itertools
import subprocess
import argparse
from  os  import chdir
import sys
class password_generator:
    def __init__(self,int=0,alpah=None,size_of_the_password=0,phones_number=0,name=None,family_names=None,family_phones=0):
        self.__int=int
        self.__alpah=alpah
        self.__size=size_of_the_password
        self.__phone=phones_number
        self.__name=name
        self.__family=family_names
        self.__phones_family=family_phones
        self.__family.append(self.__name)
        chdir(R'D:\programs data\vs\PYTHON')                                       # put your path 
        #sys.stdout = open("password_list_generator.txt", "w")                      # put your file name 
    def num_with_size(self):
        the_int_passwords=list(itertools.product(self.__int,repeat=self.__size)) 
        for i in the_int_passwords:
            print(int("".join(map(str,i))))
    def num_with_alpha(self):
        the_passwords_int_with_alpha=list(itertools.product(self.__int,self.__alpah,repeat=self.__size))
        the_passwords_alpha_with_int=list(itertools.product(self.__alpah,self.__int,repeat=self.__size))
        for i in  the_passwords_int_with_alpha :
            for s in the_passwords_alpha_with_int:
                print(str("".join(map(str,i)))+'\n'+str("".join(map(str,s))))
    def expect_all_numbers_from_one_company(self):
        the_expect=itertools.product(range(0,10),repeat=11)
        for i in the_expect:
            print(self.__phone+''.join(map(str,i)))
    def spesfic_passwords_from_name_and_numbers(self):
        spesfic_years=itertools.product(self.__family,range(1990,2031))
        for i in spesfic_years:
            print(''.join(map(str,i)))
    def specific_passwords_from_family_name_and_their_numbers(self):
        family_and_numbers=itertools.product(self.__family,self.__phones_family)
        for i in family_and_numbers:
            print(''.join(map(str,i)))
    def specific_passwords_with_len_capital_and_small_len8(self):
        nums='012345678'
        for i in self.__family:
            print(nums.replace(nums[:len(i)],i))
            print(nums.replace(nums[:len(i)],i.upper()))
            print(nums.replace(nums[:len(i)],i)+i)
            print(nums.replace(nums[:len(i)],i)+i.upper())
            print(i+nums[len(i):])
    def characher_only(self):
        ch_only=itertools.product(self.__alpah,repeat=5)
        for i in ch_only:
            print("".join(map(str,i)))
    def chracter_num(self):
        for i in self.__family:
            pass
    #sys.stdout.close()



s=password_generator((1,2,3),('a','b','c','d'),5,'010','fady',['koko','baba','mama'],["01063556262",'01200402249'])
s.num_with_size()
