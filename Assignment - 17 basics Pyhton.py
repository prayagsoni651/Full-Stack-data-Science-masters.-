#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
1. assign the value 7 to the variable guess_me. then , write the conditional tests (if , else and elif) to print the string 'too low' if guess_me is less then 7 'too high' if grater then 7 , and 'just right' if equal to 7 

'''

guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')


# In[2]:


'''
2. Assign the value 7 to the variable guess_me and the value 1 to the
variable start . write a while loop that compress start with guess_me .
print too low if start is less than guess me . if start equals guess_me
, print ' found it'  and exit the loop. if start is greater then guess_me
, print "oops" and exit the loop . increment start at the end of the loop ////////////////////////
in pytho
'''

guess_me = 7
start = 1

while start <= guess_me:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start += 1


# In[3]:


'''
3. Print the following values of the list [3, 2, 1, 0] using a for loop.
'''

my_list = [3, 2, 1, 0]
for value in my_list:
    print(value)


# In[4]:


'''
4. Use a list comprehension to make a list of the even numbers in range(10)
'''
even_numbers = [num for num in range(10) if num % 2 == 0]
print(even_numbers)



# In[5]:


'''
5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
keys, and use the square of each key as its value.
'''
squares = {num: num**2 for num in range(10)}
print(squares)



# In[6]:


'''
6. Construct the set odd from the odd numbers in the range using a set comprehension (10).
'''

odd = {num for num in range(10) if num % 2 != 0}
print(odd)


# In[7]:


'''
7. Use a generator comprehension to return the string 'Got'; and a number for the numbers in
range(10). Iterate through this by using a for loop.
'''
generator = ('Got ' + str(num) for num in range(10))

for item in generator:
    print(item)



# In[1]:


'''
8. Define a function called good that returns tahe list ['Harry', 'Ron', 'Hermione'].

'''

def good():
    return ['Harry', 'Ron', 'Hermione']


# In[2]:


'''
9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
for loop to find and print the third value returned.

'''

def get_odds():
    for num in range(1, 10, 2):  # Start from 1, step by 2 (to get odd numbers), end at 9
        yield num

# Using a for loop to find and print the third value returned
count = 0
for odd_num in get_odds():
    count += 1
    if count == 3:
        print("The third odd number from range(10) is:", odd_num)
        break


# In[3]:


'''
10. Define an exception called OopsException. Raise this exception to see what happens. Then write
the code to catch this exception and print 'Caught an oops'.

'''

# Define the OopsException
class OopsException(Exception):
    pass

# Raise the OopsException
try:
    raise OopsException
except OopsException:
    print('Caught an oops')


# In[4]:


'''
11. Use zip() to make a dictionary called movies that pairs these lists: titles = [&#39;Creature of Habit&#39;,
&#39;Crewel Fate&#39;] and plots = ['A nun turns into a monster','A haunted yarn shop'].

'''

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

# Using zip() to pair the lists and creating a dictionary
movies = dict(zip(titles, plots))

print(movies)


# In[ ]:




