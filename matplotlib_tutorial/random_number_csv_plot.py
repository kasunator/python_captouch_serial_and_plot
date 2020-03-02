import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
x_value = 0
total_1 = 1000
total_2 = 1000

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()

def animate(i):
    data = pd.read_csv('random_data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    plt.cla()
    plt.plot(x,y1, label = 'channel 1')
    plt.plot(x,y2, label = 'cahnnel 2')
    plt.legend(loc='upper left')




ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()
