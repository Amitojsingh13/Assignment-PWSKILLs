#!/usr/bin/env python
# coding: utf-8

# # AMITOJ SINGH

# # Q1 Explain with an example each when to use a for loop and a while loop.
# Ans.
# While Loop: A while loop is used when the number of iterations are unknown to us but we know the end statement.
# For example we need to get something printed in reverse manner or in normal way from 1 to 5
# i=1
# while i<=5:
#      print(i)
#      i+=1
# In this we first initalised the statement then put the condition and condition is checked again and again until it becomes false and after this loop execution is succesfull.     
#      
# For Loop: A for loop is used when the number of iterations are known to us.And also in For loop the condition is checked first then it is executed.
# for i in range(1,10):
#        print("Hello")

# In[5]:


#Forloop
for i in range(1,10):
    print("Hello",i)


# In[6]:


#while
i=1
while i<=5:
     print(i,"Hi")
     i+=1


# # Q2 Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

# In[10]:


i=1
n=0
p=1
while i<=10:
    n=n+i
    p=p*i
    i=i+1
n,p 


# # Q3 Create a python program to compute the electricity bill for a household The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 perunit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# 
# 

# In[3]:


#taking input from user for the units consumed
units = int(input("Enter the units consumed: "))

#initializing the bill amount to zero
bill = 0

if units <= 100:
    bill = units * 4.5
elif units <= 200:
    bill = (100 * 4.5) + ((units - 100) * 6)
elif units <= 300:
    bill = (100 * 4.5) + (100 * 6) + ((units - 200) * 10)
else:
    bill = (100 * 4.5) + (100 * 6) + (100 * 10) + ((units - 300) * 20)


#printing the total bill amount
print("Total electricity bill: ", bill)
    


# # Q4 Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list.

# In[2]:


mynum_01=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]


# In[21]:


#using for loop
newnum_01=[]
for i in mynum_01:
    cube=i*i*i
    if cube%4==0 or cube%5==0:
        newnum_01.append(cube)
newnum_01        


# In[6]:


#using while loop
newnum_02=[]
i=1
while i in mynum_01:
    num=i*i*i
    if num%4==0 or num%5==0:
        newnum_02.append(num)
    i=i+1
newnum_02    


# # Q5. Write a program to filter count vowels in the below-given string.string = "I want to become a data scientist"

# In[8]:


strin="I want to become data scientist"
n1=strin.count("a",)
n2=strin.count("e")
n3=strin.count("i",)
n4=strin.count("o")
n5=strin.count("u")
n6=strin.count("A")
n7=strin.count("E")
n8=strin.count("I")
n9=strin.count("U")
count=n1+n2+n3+n4+n5+n6+n7+n8+n9
print("The vowels in the sentence are:",count)


# In[ ]:




