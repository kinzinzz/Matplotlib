# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 2. 축

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)
plt.title('꺽은선 그래프', fontdict={'size':20})

plt.plot(x, y)
plt.xlabel('X축')
plt.ylabel('Y축')

plt.plot(x, y)
plt.xlabel('X축', color='red')
plt.ylabel('Y축', color='#00aa00')

plt.plot(x, y)
plt.xlabel('X축', color='red', loc='right') # left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top') # top, center, bottom

plt.plot(x, y)
plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()
