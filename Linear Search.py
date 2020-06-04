#!/usr/bin/env python
# coding: utf-8

# In[32]:


def linear_search(arr, search):
    
    found = False
    for i in range (0, len(arr)): 
        if (arr[i] == search):
            print(search, " is present at index ", i)
            found = True
    if found == False:
        print(search, " is not found")

def main():
    arr = [10, 5, 4, 29, 77, 81]
    print("Original array = ", arr)
    #Best case: Key element present at the starting index; O(1)
    search = 10
    linear_search(arr, search) 
    #Worst case: Key element present at the last index; O(n)
    search = 81
    linear_search(arr, search) 
    #Element not in array
    search = 100
    linear_search(arr, search)
    
    
if __name__ == "__main__":
    main()


# In[ ]:





# 
