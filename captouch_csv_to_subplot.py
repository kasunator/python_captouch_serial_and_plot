import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y1_values = []
y2_values = []
y3_values = []
y4_values = []
y5_values = []
y6_values = []
index = count()

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


def animate_subplot(i):
    """
    global x_values
    global y1_values
    global y2_values
    global y3_values
    global y4_values
    global y5_values
    """

    data = pd.read_csv('python_captouch_data.csv')
    x_values = data['time']
    y1_values = data['diff']
    y2_values = data['baseline']
    y3_values = data['raw']
    y4_values = data['avg']
    y5_values = data['result']
    y6_values = data['result_original']
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

ani = FuncAnimation(plt.gcf(), animate_subplot, 5000)

plt.tight_layout()
plt.show()
