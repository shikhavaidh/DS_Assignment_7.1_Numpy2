
# coding: utf-8

# In[19]:

#Assignment 7.1
#Write a function to find moving average in an array over a window:
#Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
#Approach 1
import numpy as np
lst = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print (lst)
arr=np.array(lst)
print("Length of array") 

print(len(arr))
k=3 #Window Size
for n in range(len(arr)-k+1):
  print("Mean Average for iteration {} is {}".format(n,np.mean(arr[n:n+k])))  
print("\n")

#Approach 2
#Using np.repeat and convolve
window = 3
weights = np.repeat(1.0, window)/window
smas = np.convolve(lst, weights, 'valid')
print("Solution using numbpy repeat and convolve function: ")
print (smas)


# In[ ]:




# In[ ]:




# In[ ]:



