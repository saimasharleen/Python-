#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=2


# # changing variable
# I am going to change my variable

# In[2]:


# change the value of a
a=3


# In[3]:


print(a)


# In[4]:


print ("Welcome to the world of python!")


# In[5]:


print("Hello \n Let's learn about new world!")


# In[6]:


print("Hello \nLet's learn about new world!")


# In[7]:


print("Hello\nLet's learn about new world!")


# # Variable

# In[8]:


x=5
y= "tech"


# In[9]:


x


# In[10]:


#it's case sensetive
X


# In[ ]:


#you can't use keywords as variable
try =1


# In[2]:


#address
print(id(x))


# In[1]:


#get all keywords 
import keyword
print(keyword.kwlist)
print("Total number of keywords",len(keyword.kwlist))


# In[ ]:


#can't use special characters
a@=1


# In[ ]:


#return Type
z=1
type(z)


# In[ ]:


z=1


# In[ ]:


type(z)


# In[2]:


z=1.076655
type(z)


# In[1]:


z="Burger"
type(z)


# In[3]:


#print Mutiple variables
a,b,c = 2,2,2
a,b,c


# In[4]:


a,b,c =2
a,b,c


# In[5]:


a,b,c =2
a


# In[6]:


a,b,c = 2,2,2
a


# In[7]:


a,b,c = 5,2,0
c


# # Numeric Operations

# In[8]:


a = 10
b = 20
print (a+b)
print (a-b)
print (a/b)
#floor division
print (a//b)
print (a % b)
print (a ** b)


# In[11]:


# BODMAS
print (4 * 5 - 9 + 6 / 7)


# In[1]:


a = 9
a += 1
print (a)


# In[2]:


a -= 1
print (a)


# In[3]:


import math
x = 2
math.log(x)


# In[4]:


math.sin(x)


# # Logical

# In[5]:


#logical
print (3<4)
print (True and False)
print (True or False)


# In[6]:


print (a!=b)


# In[7]:


print (3<4)
print(a!=b)


# In[8]:


print (True and not False)


# In[9]:


a = True
type (a)


# In[10]:


not a


# # Looping

# # If else loop

# In[1]:


a = 5
if a>50:
    print('a is larger than 50')
else:
    difference=50-a
    print('a is smaller than 50 by '+str(difference)+'units')


# In[1]:


a = 5
if a>50:
    print('a is larger than 50')
else:
    difference=50-a
    print(+str(difference)+')


# In[2]:


a = 5
if a>50:
    print('a is larger than 50')
else:
    difference=50-a
    print(''+str(difference)+'')


# In[2]:


#elif
num = int(input ('Enter a number:'))
if num>0 :
    print("positive number")
elif num ==0 :
    print("It is a zero")
else:
    print("Negative Number")


# In[2]:


# Find the smallest Number out of 3 values
n1 = 2
n2 = 60
n3 = 78

if (n1 <= n2) and (n1 <= n3):
    smallest = n1
elif (n2 <= n1) and (n2 <= n3):
    smallest = n2
else:
    smallest = n3
print ("smallest element among three number is : {}".format(smallest))


# In[3]:


if None:
    print ("Is True")
else:
    print("Is False")


# # For Loop

# In[10]:


subjects = ["maths", "science", "hindi", "history"]


# In[11]:


print(len(subjects[0]))
print(len(subjects[1]))
print(len(subjects[2]))
print(len(subjects[3]))


# In[12]:


for i in range(4):
    print(len(subjects[i]))


# In[13]:


for i in range(1,10,3):
    print(i)


# In[25]:


str1=''
for i in range(0,9):
    if i<5:
        str1 += '*'
        print(str1)
    elif i>4:
        str1 = str1[:-2]
        print(str1) 


# In[27]:


my_string = "Hello from Bangladesh"
for n,alphabet in enumerate(my_string):
    print(alphabet,n)


# # While Loop

# In[32]:


num = int(input("Enter a number:"))         #convert string to int 
isDivisible = False;
i = 2;
while i < num:
    if num % 1 == 0:
        isDivisible = True;
        print ("{} is divisble by {}".format(num,i))
        i +=1;
if isDivisible:
    print("{} is NOT a Prime number".format(num))
else:
    print("{} is a Prime number".format(num))
        


# # Creating Functions

# In[33]:


# Check function-bangladesh doc


# In[5]:


def hello_world():
    print('Hello World')
hello_world()


# In[6]:


def cube(num):
    out = num**3
    return(out)


# In[7]:


cube1 = cube(3)
print(cube1)


# In[9]:


q = cube(4)
print("Q is " +str(q))


# In[10]:


# Calculate factorial
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n
fact = factorial(5)
print(fact)


# In[11]:


def submition(*args):
    print(args)
    return(sum(args))


# In[12]:


print(submition(1,2,3,4))


# In[13]:


captain = "Shakib Al Hasan"
string_to_list = lambda x: x.split()
print(string_to_list(captain))
print(type(string_to_list))


# In[14]:


multiply = lambda x, y : x*y
print(multiply(4,4))


# In[15]:


# Documentation
def triple(num):
    """
    function to triple the number
    """
    return 3 * num


# In[1]:


triple(10)


# # String Values and Operator

# In[3]:


x = 'AIUB'
y = "Bhallagenabhai"
x,y


# In[4]:


len(x), len(y)


# In[5]:


small = "hello lets convert it to upper"
print(small.upper())


# In[7]:


large = "HELLO LETS CONVERT IT TO LOWER"
print(large.lower())


# In[8]:


some_sentence = "There is a space at the end     "
print(len(some_sentence))


# In[9]:


print(len(some_sentence.rstrip()))


# In[10]:


print(some_sentence.rstrip())


# In[14]:


increment = '4%'
print(increment.rstrip('%'))


# In[15]:


start = " There is a space at the start"
print(start)


# In[16]:


start = "  There is a space at the start"
print(start)
print(start.lstrip())


# In[17]:


num_with_chars = '*444#'
print(num_with_chars.rstrip('#'))
print(num_with_chars.lstrip('*'))
print(num_with_chars.rstrip('#').lstrip('*'))


# In[22]:


val = '4 apples'
no_of_apples = val[0]
print(no_of_apples)
print('number of apples is', no_of_apples)


# In[23]:


what = val [2]
print(what)


# In[24]:


what = val [2:]
print(what)


# In[25]:


what.replace('a','*%')


# In[27]:


print(val[2:5])


# In[32]:


batch = '5 oranges 3 monkeys and'
fruits = batch [ :9]
print(fruits)


# In[33]:


print(batch[ :-2])


# In[34]:


animals = batch[10:-2]
print(animals)


# In[35]:


nums = '123456789'
even_nums = nums[1::2]
print(even_nums)


# In[36]:


odd_nums = nums[0::2]
print(odd_nums)


# In[38]:


odd_nums_again = nums[ ::2]
print(odd_nums_again)


# In[40]:


first_name = 'pissed'
last_name = 'off'
name = first_name+""+last_name
print(name)


# In[41]:


name = first_name + " " + last_name
print(name)


# In[43]:


name = first_name + " " + last_name + " huru "
print(name)


# In[45]:


"""Let's also understand
examples of 
multiline comments"""
first_name.capitalize()


# In[46]:


age = 20
my_age = ("I am "+ str(age) + " years old")
print(my_age)


# In[49]:


My_age = "I am {0} years old".format(age)
My_age


# In[50]:


A = "Data"
B = "Analysis"
C = "Numpy"

print("{0} {1} using {2}".format(A,B,C))


# In[51]:


#concat and update
name += ' ' + my_age
print(name)


# In[52]:


x="as"
y="assignment"

x in y


# # Lists

# In[53]:


a = []
print(a)


# In[54]:


type(a)


# In[55]:


languages = ['R','Python', 'SAS', 'Scala', 42]
print(languages)


# In[56]:


type(languages)


# In[57]:


print(languages[0])


# In[58]:


print(languages[2])


# In[59]:


print(languages[1:4])


# In[60]:


print(languages[-2])


# In[61]:


print(languages[1:])


# In[66]:


print(languages[:-2])


# In[67]:


languages = ['R','Python', 'SAS', 'Scala', 42]
languages.append('ML')
print(languages)


# In[68]:


languages.pop()


# In[69]:


print(languages)


# In[71]:


languages.pop(0)
print(languages)


# In[72]:


languages.pop(1)
print(languages)


# In[73]:


languages.append('Deep Learning')
#languages.remove('Deep Learning')
print(languages)


# In[74]:


languages.remove('Deep Learning')


# In[75]:


languages


# In[76]:


new_list = languages
languages.append('Java')
print(new_list)


# In[77]:


print(id(languages))


# In[78]:


print(id(new_list))


# In[79]:


new_list = languages[:]
print(id(new_list))


# In[80]:


#not going to share same memory address
another_list = languages.copy()
print(id(another_list))


# In[83]:


new_list1 = languages.copy()
languages.append('food')
print(new_list1)


# In[84]:


print(id(new_list1))


# In[86]:


mail = "Amuu jamuu khamuu. okayyyy byee byee."
words = mail.split() 
print(words)


# In[87]:


sentences_in_mail = mail.split('.')
print(sentences_in_mail)


# In[89]:


new_mail = " ".join(sentences_in_mail)
print(new_mail)


# In[90]:


list1 = ["Lol"]
print(list1*6)


# In[91]:


print(list1 + list1)


# In[92]:


nums = [2,6,9,3,2,10]
print(len(nums))


# In[93]:


print(nums[1::2])


# In[94]:


nums[2]="!!!"
nums


# In[95]:


nums = [2,6,9,3,2,10]
print(sorted(nums))


# In[96]:


print(max(nums))


# In[97]:


print(min(nums))


# In[98]:


#nested list
n = [[1, 2, 3, 4], [ 5, 6, 7], [8, 9, 10]]

print(n[1])


# In[99]:


print(n[0][1])


# # Tuples

# In[ ]:




