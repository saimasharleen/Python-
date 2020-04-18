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


# In[ ]:


# Find the smallest Number out of 3 values
n1 = 2
n2 = 60
n3 = 78

