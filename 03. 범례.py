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

# # 3. 범례(legend)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y, label='무슨 데이터')
plt.legend()

plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='upper right')

plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='lower right')

plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='best')

plt.plot(x, y, label='범례')
plt.legend(loc=(0.5,0.5))
