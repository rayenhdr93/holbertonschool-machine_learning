#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

y1 = np.array(fruit[0])
y2 = np.array(fruit[1])
y3 = np.array(fruit[2])
y4 = np.array(fruit[3])
N = np.arange(3)
plt.bar(N, y1, width=0.5, color='red', label='apples')
plt.bar(N, y2, width=0.5, bottom=y1, color='yellow', label='bananas')
plt.bar(N, y3, width=0.5, bottom=y1+y2, color='#ff8000', label='oranges')
plt.bar(N, y4, width=0.5, bottom=y1+y2+y3, color='#ffe5b4', label='peaches')
plt.xticks(N, ('Farrah', 'Fred', 'Felicia'))
plt.yticks(np.arange(0, 90, 10))
plt.ylabel('Quantity of Fruit')
plt.legend()
plt.title('Number of Fruit per Person')
plt.show()
