#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import os

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    else: 
        _ = os.system('clear') 

time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print('======Thingsboard Front End Custom Builder======')
time.sleep(0.5)
print('===========v1_DPTE UPI - @l0wpassfilter=========')
time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print()
print()

input('Press enter to continue...')
clear()


# In[ ]:


time.sleep(0.5)
print("Make sure you've put your compiled ui-ngx.jar")
time.sleep(0.5)
print("file to put_ui-ngx_here folder")
time.sleep(0.5)
input('Press enter to continue...')


# In[ ]:


#Get thingsboard.jar and thingsboard.yml

time.sleep(0.5)
print("Getting thingsboard.jar and thingsboard.yml files")

os.system('./script.sh getFile')
time.sleep(0.5)
print("Done, copied to copied_file")
time.sleep(0.5)
print('================================================')


# In[ ]:


#Extract thingsboard.jar

time.sleep(0.5)
print("Extracting thingsboard.jar files")

os.system('./script.sh extractFile')
time.sleep(0.5)
print("Done")
time.sleep(0.5)
print('================================================')$


# In[ ]:


#Putting ui-ngx and thingsboard.yml to thingsboard_extract

time.sleep(0.5)
print("Putting all the necessary files")

os.system('./script.sh putFile')
time.sleep(0.5)
print("Done")
time.sleep(0.5)
print('================================================')


# In[ ]:


#Repack as .jar

time.sleep(0.5)
print("Repacking")

os.system('./script.sh pack')
time.sleep(0.5)
print("Done")
time.sleep(0.5)
print("Repacked to thingsboard.jar on generated_file directory")
time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print('===============Have a Nice Day==================')
time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print('exiting program..')


# In[ ]:




