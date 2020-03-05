import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')



data = pd.read_csv('python_captouch_data_from_wakeup.csv')
x_values = data['time']
y1_values = data['diff']
y2_values = data['baseline']
y3_values = data['raw']
y4_values = data['avg']


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



plt.tight_layout()
plt.show()
