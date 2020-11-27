#!/usr/bin/env python
# coding: utf-8

# In[4]:


#! = python3
# - the mode() function takes in a list and returns the Mode and its frequency
''' 
This code uses an algorithm of reversing the list and calculating the mode based on the First occurence of the number
in the reversed list
'''


# - Function Start ------------------------------------------
def mode(lst):
    import copy
    reverse_lst = lst.copy()
    reverse_lst.reverse() # - reversing the list
    list_size = len(lst)
    cummulative_frequency = 0
    values = []
    frequencies = []
    
    while (cummulative_frequency != list_size):
        current_X = lst[cummulative_frequency]
        # - Mechnism of calculating the modal Frequency -----
        X_frequency = list_size - reverse_lst.index(current_X) - cummulative_frequency
        # ---------------------------------------------------
        values.append(current_X)
        frequencies.append(X_frequency)
        cummulative_frequency += X_frequency
        
    modal_frequency = max(frequencies)
    mode = values[frequencies.index(modal_frequency)]
    
    return (mode, modal_frequency)
# - End of Function -----------------------------------------


# In[ ]:




