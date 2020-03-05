import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')



data = pd.read_csv('python_captouch_data_from_wakeup.csv')
x_values = data['time']
print(type(x_values))
y1_values = data['diff']
print(type(y1_values))
y2_values = data['baseline']
y3_values = data['raw']
y4_values = data['avg']
#y5_values = data['result']


#print("x_values=" + str(x_values))
#print("y_values" + str(y_values))

#plt.cla()
#plt.plot(x_values, y1_values,label='diff')
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


#plt.title('catouch data')
#plt.gcf().autofmt_xdate()
plt.tight_layout()



#plt.tight_layout()
plt.show()
