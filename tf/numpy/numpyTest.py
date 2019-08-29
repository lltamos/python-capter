# coding: utf-8

# # np.random.seed()的作用

# ### 当我们设置相同的seed时，每次生成的随机数也相同，如果不设置seed，则每次生成的随机数都会不一样

# In[1]:

from numpy.random import rand
import numpy as np

# 不使用seed
a = rand(5)
print('第一次列表a：', a)

# In[2]:

a = rand(5)
print('第二次列表a：', a)

# In[3]:

# 使用seed
np.random.seed(3)
b = rand(5)
print('第一次列表b：', b)

# In[4]:

np.random.seed(3)
b = rand(5)
print('第二次列表b：', b)
