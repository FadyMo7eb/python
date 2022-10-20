
import re

"""
*** () ==> if you but smt in them will return you tem only ***

Element	Description

.	This element matches any character except \n

\d	This matches any digit [0-9]

\D	This matches non-digit characters [^0-9]

\s	This matches whitespace character [ \t\n\r\f\v]

\S	This matches non-whitespace character [^ \t\n\r\f\v]

\w	This matches alphanumeric character [a-zA-Z0-9_]

\W	This matches any non-alphanumeric character [^a-zA-Z0-9]

\b detect the dobulecated worlds 

Quantifiers to use

Quantifier	Description	Example	Sample match

+	one or more	\w+	ABCDEF097

{2}	exactly 2 times	\d{2}	01

{1,}	one or more times	\w{1,}	smiling

{2,4}	2 to 4 times	\w{2,4}	1234

*	0 or more times	A*B	AAAAB

?	once or none(lazy)	\d+?	1 in 12345 ==> thats mean ? is the end of the line  

Note : we use r"------" to avoid / \ 

"""
name="fa"

nom="fady"

re.match(name,nom) # return you the match character and the span of their position   and if you change places give you none  First, a re.match matches the pattern only at the beginning of the string.

re.match(name,nom,2,4) # if we want to set start and end pos

re.match(name,nom).span() # return positon the they are match

re.match(name,nom).group(0) # return charater  the they are match

re.match(name,nom).start() # return the start of match

re.match(name,nom).end() # return the end of match 

patt = re.compile(r'fady') # using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.

paty=re.compile(r'fady',re.MULTILINE) # re.MULTILINE is ignore \n

patt.match("fady")

"""
import re 
li=['89999999999','899999999999','899999-9999','899999999x']
for i in li :
    if re.match(r"[8-9]{1}[0-9]{10}",i) and len(i)==11:
        print('match')
    else:
        print(" NONE OF MATCH ")
        
"""

re.search(name,nom) # return like match but it look no in the beging it look for hole string

"""
you can make if statement in the regex

import re

li=re.search(r"\w+(?=\shere)","is fady here ? ")

print(li)

"""
re.findall(name,nom) # find the string in the hole line

"""
ex for findall

import re 
line=r"fady is here so watchout becouse fady want fady to kill him so be secure"
gmail="fmoheb6@gmail.com"
salary="122 123 1234 12345 123456"
html='''<tr align="center"><td>1</td> <td>Noah</td> <td>Emma</td></tr>
      <tr align="center"><td>2</td> <td>Liam</td> <td>Olivia</td></tr>
      <tr align="center"><td>3</td> <td>Mason</td> <td>Sophia</td></tr>
      <tr align="center"><td>4</td> <td>Jacob</td> <td>Isabella</td></tr>
      <tr align="center"><td>5</td> <td>William</td> <td>Ava</td></tr>
      <tr align="center"><td>6</td> <td>Ethan</td> <td>Mia</td></tr>
      <tr align="center"><td>7</td> <td HTML>Michael</td> <td>Emily</td></tr>'''
l="Hello world,we lives here"
print(re.findall("fady",line)) # search about fady in the whole string
print(re.findall(".",line))    # return the hole line in split with spaces
print(re.findall("\w+",line))    # return the hole line in split only words
print(re.findall("\w*",line))    # like \w+
print(re.findall("^\w+",line))    # frist world without /n
print(re.findall("\w+$",line))    # last world withuout /n
print(re.findall("\w+$",line))    # last world withuout /n
print(re.findall("\w\w",line))==print(re.findall(r"\b\w.",line)) # to print tow chracter of all the line
print(re.findall("\w+@\w+.(\w+)",gmail)) # you can use () to print the elment you want
print(re.findall("\d{5,6}",salary)) # you can use {} to make range 
print(re.findall("[fs]\w+",line))  # you can choose specific chracters
print(re.findall("[^fs]\w+",line))  # you can choose specific chracters in beging
s=re.findall(r'<td>(\w+)</td>\s<td>(\w+)</td></tr>',html) # we can use it with html tags 
print(re.findall('(\w+) (\w+)',l)) != print(re.findall('(\w+)(\w+)',l) # frist one will split the line and return you a line split but secound one will split world and return the chracter of the one into the number of \w+


"""
re.split(name,nom,maxsplit=2)

"""
ex of split 

import re 

line="fadyxisxherexnow"
line2="fady is;here>now"
line3="fady is here now "
print(re.split(r"x",line))             # to split line per x
print(re.split(r"x",line,maxsplit=2))  # we use maxsplit to count split we make 
print(re.split(r"[:;>\s]",line2))      # we can but some special chracters to split
print(re.split(r"\s+",line3))          # to split string only with spaces 


"""

re.sub("fad","dod",name)

"""
s=fady
k=re.sub("fad","dod",s)
print(k) ==> dodo

"""

# if you have a string and the pattern next each togther use (?<=(the somthing )) like print(re.sub(r'(?<=\s)(\|\|)(?=\s)',r"or",re.sub(r'(?<=\s)(&&)(?=\s)',r"and",i)))


# a way to check if we have somthing in our string print(re.search(r" **** ([A-Z or any pattern ].*){2 at least  or any number} ******",f))

# print(re.findall(r"(?=((\d)\d\2))",num))

"""
import re 
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())


"""