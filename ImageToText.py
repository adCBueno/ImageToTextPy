#!/usr/bin/env python
# coding: utf-8

# In[16]:

# This was developed in JUPYTER, each "ln[]" you see is a cell where you run an individual piece of code
get_ipython().system('pip install tesseract')


# In[2]:


get_ipython().system('pip3 install --upgrade Pillow')


# In[3]:


get_ipython().system('pip install Pillow==9.1.0')


# In[4]:


get_ipython().system('pip install pytesseract')


# uploaded = files.upload()![imagen.jpg](attachment:imagen.jpg)

# ![imagen.jpg](attachment:imagen.jpg)

# In[30]:


# import image module
from IPython.display import Image

# get the image
Image(url="imagen.jpg", width=300, height=300)


# In[31]:


import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#%matplotlib inline


# In[32]:


texto_largo = plt.imread('imagen.jpg')
plt.figure(figsize=(15,5))
plt.imshow(texto_largo)
plt.axis(False)


# In[33]:


img = plt.imread('imagen.jpg')


# In[34]:


plt.imshow(img)


# In[41]:


get_ipython().system('pip install tesseract')
get_ipython().system('pip install pytesseract')


# In[57]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #Download it on your PC and put the path, it might change
print(pytesseract.image_to_string(r'imagen.jpg')) #With the name of your image
