a= 'anime'
b='big boss'
print(f"i watch {a}&{b}")
is_s=0
if is_s:
 print(f' you a student')
else: 
  print('not a')
'sndainsdands'#multiline comment 

#type casting - conversion of data type
name = ''
age = 1
cgpa = 2.5
male = True
age = float(age)
print(age)
age = str(age)
print(type(age))
name = bool(name)
print(name)
cgpa = bool(cgpa)
print(cgpa)

#user input - return data as string 
'''name = input(' your name:')
age = int(input('how old are you :'))
age = age + 4
print(f'i am{age}years old ')
print('hello',name)
print(f'how are you {name}')'''

print(10==10)#boolean question

#arithemetic and maths 
'''f = int(input())
f**=2
print(f)
f%=3
print(f)'''
x=2.46
y=-6
z=3
#result = round(x) roundoff
#result = abs(y) absolute
#result = pow(4,3)
# result = min/max(x,y,z)
import math
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.1))#round off no to upward
print(math.floor(9.9))#round off no to downward

#if statements
'''age = int(input("your age :"))
if age>=100:
 print('too old')
elif age<=0:
 print('not even born ')
elif age <=18 :
 print('must be 18 ')
else   :
  print('you are signed up')'''

#logical operators or/and/not
t=25
m=True
if 10>t>0 :
  print('hex')
elif 20>t>10 and m:
  print('lex')
elif t>20 and m:
  print('max')

#conditional expression -one line if else (ternar operator )
t=36 
#print('HOT'if t>35 else 'warm')
R= 'divisible' if t%3==0 else ' not divisible'
print(R )

#string method 
'''name=input('Enter name:')
print(len(name))
r= name.find('t')#find from first 
q=name.rfind('a')#find from last
c=name.capitalize()#capitalize the first letter 
u=name.upper()
l=name.lower()
print(name.isdigit())#boolean function
print(name.isalpha())#boolean check for alpha only 
#gives negative if not found 
print(r,q)
pn=input('enter :')
  p=pn.count('e')#counts only a single thing 
print(p)
   pn=pn.replace('-',' ')#replaces a single thing 
print(pn)
print(help(str))'''

#validate user input 
N= input('enter your name:')
s=N.find(' ')
N.isalpha()
if len(N)>12:
  print(f'Name must be in 12 letters')
elif s>=1:
  print(f'name must not contain any space')
elif not N.isalpha():
  print(f'name must not contain any digit')
else:
   print(f'name succesfully entered.')  

#string indexing accesing element of a sequence using[]=>[start:end:step]
cn ='123-456-789-0'
'''print(cn[3]) # element at 3rd
print(cn[4:])# from 4th pos
print(cn[2:6])#from 2nd to 6
print(cn[:5])#till 5th
print(cn[-1])#last
print(cn[::2])#at every 2nd 
print(cn[-4:])
print(cn[::-1])#reverse the entire string'''

#format specifiers {value:flag}  format a value based on what flag is inserted 
# .(number)f= round to that many decimal places
# :(number) = allocate that many spaces
#:01 = allocate and add zero pad to that  many spaces 
#:< =left aalignment 
#:> = right allignment 
#:^ = centre allignment 
#:+ =use a plus sign to indicate a postive value 
#:= = place sign to left most position 
#: = insert space before positvie no 
#:, = comma seperator 
p1= 31.1214242
p2=-231.2312
p3 = 13001000.252311
print(f'no1 {p1:.2f}')#decimal up to 2
print(f'no2{p3:10}')
print(f'no3{p3:010}')
print(f'no4{p1:<10}')#left alignment 
print(f'no5 {p2:<10}')
print(f'no 6{p3:<10}')
print(f'no 7{p2:>10}')#right alignment 
print(f'no8 {p3:>10}')
print(f'no9 {p1:^10}')#centre
print(f'no10 {p2:^10}')
print(f'no11 {p3:^10}')
print(f'no12 {p1:+}')
print(f'no13 {p2:+}')
print(f'no14 {p1:=10}')
print(f'no15 {p2:=10}')
print(f'no16 {p1: }')
print(f'no17 {p2: }')
print(f'no18 {p1:,}')
print(f'no19 {p2:,}')
print(f'no {p3:+,.1f}')# 3 format in one 

#while loop 
age = int(input(f'Enter:'))
while age<0:
  print(f'Provide proper age')
  age = int(input(f'Enter:'))

print(f'you are {age}year old')  

while age<0 or age >100 :
  print(f'enter valid age ')
  age=int(input('enter'))
print(f'{age} year old')  

#for loops 
for i in reversed(range(1,10)):
  print(i)

for i in range (1,20,2):
  print(i)

m='2123-2132-23134'
for i in m:
  print(i)  

#nested loop 
r=int(input(f'rows'))
c=int(input(f'column'))
s=input(f'symbol:')
for x in range (r):
 for y in range (c):
  print(f'{s} ')
 print() 

