#!/usr/bin/env python
# coding: utf-8

# In[8]:


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

def main():
    my_list = [1, 3, 5, 7, 9]
    print("Original array: ", my_list)
    search = 3
    print(binary_search(my_list, search))
    search = 10
    print(binary_search(my_list, search))  
    
    
if __name__ == "__main__":
    main()


# In[ ]:




