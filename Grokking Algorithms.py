#!/usr/bin/env python
# coding: utf-8

# ### Binary Search

# In[2]:


def binary_search(list, item):
    
    low = 0
    high = len(list) - 1
    
    while(low <= high):
        
        mid = round((low + high)/ 2)
        guess = list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))        


# ### Selection Sort

# In[3]:


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([1, 5, 3, 6, 2, 10]))
            


# ### Recursion

# In[4]:


def countdown(i):
    print(i)
    if (i <= 0):
        return
    else:
        countdown(i - 1)
countdown(3)


# ### Stack

# In[5]:


def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name): 
    print("How are you, " + name + '?')
    
def bye():
    print("Ok, bye!")
    
greet("Ishika")  


# In[6]:


def fact(x):
    if (x == 1):
        return 1
    else:
        return x * fact(x - 1)

fact(3)


# ### Divide and Conquer

# In[11]:


#Without Recursion
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

sum([1, 2, 3, 4, 5])


# In[14]:


#With recursion
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])
    
sum([1, 2, 3, 4, 5])


# In[15]:


#Count no. of items in the list

def count_items(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + count_items(arr[1:])
    
count_items([1, 2, 3, 4, 5])


# In[17]:


#Find maximum number from a list
def max_number(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_number(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

max_number([1, 3, 10, 5, 8])


# In[1]:


#Find maximum number from a list
def max_num(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        return max(arr[0], max_num(arr[1:]))

max_num([9, 5, 12, 6, 1])


# ### Quick Sort

# In[19]:


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([1, 8, 3, 7, 5, 6]))


# ### Hash function

# In[22]:


# Who get's to vote
# Check for duplicate voters
voted = {}
def check_voter(name):
    if voted.get(name):
        print("Already you've voted! " + name)
    else:
        voted[name] = True
        print("Yes, you can vote! " + name)

check_voter("Ishika")
check_voter("Sukalyan")
check_voter("Ishika")


# ### Bread-first search

# In[25]:


graph = {}
graph["You"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Peggy"] = []
graph["Anuj"] = []
graph["Thom"] = []
graph["Jonny"] = []

from collections import deque
def find_mango_seller():
    search_queue = deque()
    search_queue += graph["You"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False

def person_is_seller(name):
    return name[-1] == 'm'

find_mango_seller()


# In[26]:


#Taking into account no elements are searched more than once!
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("You")


# ### Greedy Algorithm

# In[ ]:


states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {}
stations['kone'] = set(["id", "nv", "ut"])
stations['ktwo'] = set(["wa", "id", "mt"])
stations['kthree'] = set(["or", "nv", "ca"])
stations['kfour'] = set(["nv", "ut"])
stations['kfive'] = set(["ca", "az"])
final_stations = set()
best_station = None
states_covered = set()

