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

x_values.append(0)
y1_values.append(0)
y2_values.append(0)
y3_values.append(0)
y4_values.append(0)
y5_values.append(0)

index = count()


def animate(i):
    data = pd.read_csv('python_captouch_data.csv')
    x_values = data['time']
    y1_values = data['diff']
    y2_values = data['baseline']
    y3_values = data['raw']
    y4_values = data['avg']
    #y5_values = data['result']



    #print("x_values=" + str(x_values))
    #print("y_values" + str(y_values))

    plt.cla()
    #plt.plot(x_values, y1_values,label='diff')
    plt.plot(x_values, y2_values,label='baseline')
    plt.plot(x_values, y3_values,label='raw')
    plt.plot(x_values, y4_values,label='avg')
    plt.xlabel('Time')

    plt.legend(loc='upper left')
    #plt.title('catouch data')
    #plt.gcf().autofmt_xdate()
    #plt.tight_layout()


data = pd.read_csv('python_captouch_data.csv')
x_values = x_values.append(int(data['time']))
print(str(data['time']))
print(str(x_values))
y1_values = y1_values.append(int(data['diff']))
print(str(y1_values))
y2_values = y2_values.append(data['baseline'])
y3_values = y3_values.append(data['raw'])
y4_values = y4_values.append(data['avg'])
y5_values = y5_values.append(data['result'])

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
axs[2].plot(x_values, y1_values,label='result')
axs[2].set_ylabel('result state')
axs[2].legend(loc='upper left')
axs[2].set_xlabel('Time')


def animate_subplot(i):
    global x_values
    global y1_values
    global y2_values
    global y3_values
    global y4_values
    global y5_values

    data = pd.read_csv('python_captouch_data.csv')
    x_values = x_values.append(data['time'])
    y1_values = y1_values.append(data['diff'])
    y2_values = y2_values.append(data['baseline'])
    y3_values = y3_values.append(data['raw'])
    y4_values = y4_values.append(data['avg'])
    y5_values = y5_values.append(data['result'])


ani = FuncAnimation(plt.gcf(), animate_subplot, 5000)

plt.tight_layout()
plt.show()
