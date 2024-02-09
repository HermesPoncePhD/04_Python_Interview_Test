import os
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.random((200,1))
y = x ** 2

plt.plot(x,y)
plt.xlabel('Dis')
plt.ylabel('Force')
plt.title('Damper')

fig = plt.figure()
plt.subplot(3,3,1)
plt.plot(x,y)
plt.xlabel('Dis')
plt.ylabel('Force')
plt.title('Damper 1')
plt.subplot(3,3,2)
plt.plot(x*-4,y,'r')
plt.xlabel('Dis')
plt.ylabel('Force')
plt.title('Damper 2')







