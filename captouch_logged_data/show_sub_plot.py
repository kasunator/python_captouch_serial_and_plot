import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')



data = pd.read_csv('python_captouch_data_1.csv')
x_values = data['time']
y1_values = data['diff']
y2_values = data['baseline']
y3_values = data['raw']
y4_values = data['avg']
y5_values = data['result']
y6_values = data['result_original']

"""

fig, axs = plt.subplots(nrows= 3,ncols =1,sharex = True);
axs[0].plot(x_values, y2_values,label='baseline',color = 'blue')
axs[0].set_ylabel('baseline')
axs[0].legend(loc='upper left')

axs[1].plot(x_values, y3_values,label='raw',color = 'orange')
axs[1].set_ylabel('raw')
axs[1].legend(loc='upper left')

axs[2].plot(x_values, y4_values,label='avg', color = 'yellow')
axs[2].set_ylabel('avg')
axs[2].legend(loc='upper left')


plt.tight_layout()
plt.show()
"""

fig, axs = plt.subplots(nrows= 3,ncols =1,sharex = True);

axs[0].cla()
axs[0].plot(x_values, y2_values,label='baseline')
axs[0].plot(x_values, y3_values,label='raw')
axs[0].plot(x_values, y4_values,label='avg')
axs[0].set_ylabel('readings')
axs[0].legend(loc='upper left')

axs[1].cla()
axs[1].plot(x_values, y1_values,label='diff')
axs[1].set_ylabel('diff')
axs[1].legend(loc='upper left')

axs[2].cla()
axs[2].plot(x_values, y5_values,label='result')
axs[2].plot(x_values, y6_values,label='result original')
axs[2].set_ylabel('result state')
axs[2].legend(loc='upper left')
axs[2].set_xlabel('Time')

plt.tight_layout()
plt.show()
