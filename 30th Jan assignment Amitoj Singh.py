#!/usr/bin/env python
# coding: utf-8

# # Assignment 30th Jan AMITOJ SINGH

# ### Write a program to accept percentage from user and display the grade according to given criteria
# 

# In[2]:


a=int(input("Enter the percentage you got:"))
if a>90:
    print("A")
elif a>80 and a<=90:
    print("B")
elif a>=60 and a<=80:
    print("C")
else:
    print("D")


# ### Q2

# In[12]:


i = float(input("Enter the cost price of the bike:"))
if i>100000:
    print("Your tax will be:",(0.15*i))
elif i>50000 and i<=100000:
    print("Your tax will be:",(0.1*i))
elif i<=50000:
    print("Your tax will be:",(0.05*i))


# # Q3

# In[4]:


Mycity_place = {"Delhi" : "Redfort","Agra" : "Taj Mahal","Jaipur" : "Jal Mahal"}
a=input("Enter the city :")
b=Mycity_place.get(a)
print("You can visit "+b)


# # Q4

# In[1]:


num = int(input("Enter a number: "))
i = 0

while num > 10:
    num = num / 3
    i += 1
    

print( i, "times before it is less than or equal to 10.")


# # Q5
# In python while loop is a control flow statement that allows code to be executed repeatedly while a certain condition is true.
# The loop will continue executing the code inside the loop as long as the condition remains true.Once the condition inside it becomes false the loop terminates and program continues.
# While loops are useful in many situations where you need to repeat a block of code multiple times until a certain condition is met. Here are a few examples of when you might use a while loop in Python:
# 1.Repeating code until a user provides valid input: You might use a while loop to repeatedly prompt the user for input until they provide a valid input that meets certain criteria.
# 2.Iterating over a list or other iterable until a certain condition is met: You might use a while loop to iterate over a list or other iterable until a certain condition is met, such as finding the first item in the list that meets a certain criterion.
# 

# # Q6

# In[2]:


i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j +=1
        
    print(" ")
    i+=1


# In[3]:


n = 5
i = 1
while i <= n:
    # print spaces before asterisks
    j = 1
    while j <= n-i:
        print(' ', end='')
        j += 1
    
    # print asterisks
    j = 1
    while j <= (2*i-1):
        print('*', end='')
        j += 1
    
    # go to the next line
    print('')
    i += 1


# # Q7

# In[2]:


i=10
while i in range(1,11):
    print(i)
    i-=1
    
    

