#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[ ]:


"def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line


# In[11]:




def factorial(number): 
    if number==1: 
        return(1)
    
    else: 
        return (number * factorial(number-1))
    
x=int(input("number "))
    
result=factorial(x)
    
print(result)



# In[ ]:





# # 2.

# In[ ]:


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line


# In[58]:



def classify_grade(number_grade):

    if number_grade<60:return("F")
    elif number_grade<67:return("D")
    elif number_grade<74:return("C")
    elif number_grade<80:return("C+")
    elif number_grade<86:return("B")
    elif number_grade<92:return("B+")
    elif number_grade<101:return("A")

x=float(input("grade "))
    
result=classify_grade(x)

print(result)


# # 3.

# In[ ]:


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line


# In[99]:


def average_weight(w,x,y,z):
   return (((w*x)+(y*z))/(w+y))

item_quantity_1=int(input("item 1 quantity: "))
item_weight_1=float(input("item 1 weight: "))
item_quantity_2=int(input("item 2 quantity: "))
item_weight_2=float(input("item 2 weight: "))

result=average_weight(item_quantity_1,item_weight_1,item_quantity_2,item_weight_2)

print(result)


# 

# # 4.

# In[ ]:


def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line


# In[157]:


def string_sum(string):
    a = 0
    for x in string:
        if x.isdigit() == True:
            z = int(x)
            a = a + z

    return a

y=str(input("string: "))

result=string_sum(y)

print(result)

     


# 

# # 5. is this pythagorian  

# In[ ]:


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line


# In[110]:


import math
def distance(x_1, y_1, x_2, y_2):
    a=x_2-x_1
    b=y_2-y_1
    sum=a**2+b**2
    return math.sqrt(sum)

x1=float(input("first x-coordinate:"))
y1=float(input("first y-coordinate:"))
x2=float(input("second x-coordinate:"))
y2=float(input("second y-coordinate:"))

result=distance(x1,y1,x2,y2)

print(result)


# In[ ]:





# # 6.

# In[ ]:


def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line


# In[215]:



a = 0
b = 0
c = 0
d = 0
e = 0
i= int(input("enter the amount, in centavos, to make change for "))


if i>=100:
        a = i/100
        i %= 100

if i>=25:
    b = i/25
    i %= 25
    
if i>=10:
    c = i/10
    i%=10
    
if i>=5:
    d = i/5
    i %= 5
    
if i>0:
    e = i/1
    i = 0

    
print (" 1P: %i / 25C: %i / 10C: %i / 5C: %i / 1C: %i " %(a , b, c, d, e))


# In[ ]:





# In[ ]:





# In[ ]:




