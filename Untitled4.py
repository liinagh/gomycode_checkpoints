#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=2000
b=3200
c=7
d=5
x=[]
for i in range (a,b,1) :
    if i%c==0 and i%d!=0 :
        x.append(i)
print (x)


# In[2]:


x=int(input('Enter a !negative integer :'))
if x<0:
    print ('It must be a !negative integer : ')
else : 
    f=1
    for i in range (x,1,-1) :
        f=f*i
    print (f)


# In[3]:


n=int(input('Enter a number: '))
d={}
for i in range (1,n+1) :
    d[i]=i*i
print(d)


# In[5]:


n=int(input('Enter n :'))
s=input('Enter a string : ')
if n>=len(s):
    print ('n must be <length(s)')
else :
    b=s[0:n]
    c=s[n+1:len(s)]
    r=b+c
    print (r)


# In[6]:


import numpy as np
a1=np.array([0,1,2])
a2=np.array([2,1,0])
cm=np.cov(a1, a2)
print(cm)


# In[ ]:




