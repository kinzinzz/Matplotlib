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

# # 04. 스타일

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

plt.plot(x, y, linewidth=5)

# ## 마커(marker)

plt.plot(x, y, marker='o')

plt.plot(x, y, marker='o', linestyle='None')

plt.plot(x, y, marker='v', markersize=10)

plt.plot(x, y, marker='x', markersize=10)

plt.plot(x, y, marker='x', markersize=20, markeredgecolor='red')

plt.plot(x, y, marker='o', markersize=20, markeredgecolor='red', markerfacecolor='yellow')

# ## 선 스타일

plt.plot(x, y, linestyle=':')

plt.plot(x, y, linestyle='--')

plt.plot(x, y, linestyle='-.')

# ## 색깔

plt.plot(x, y, color='pink')

plt.plot(x, y, color='#ff0000')

plt.plot(x, y, color='b')

plt.plot(x, y, color='g')

# ## 포맷

plt.plot(x, y, 'ro--') # color, marker, linestyle

plt.plot(x, y, 'bv:')

plt.plot(x, y, 'go')

# ## 축약어

plt.plot(x, y, marker='o', mfc='red', ms='10', mec='blue', ls=':')

# ## 투명도

plt.plot(x, y, marker='o', mfc='red', ms='10', alpha=0.3) # alpha : 투명도(0~1)

# ## 그래프 크기

plt.figure(figsize=(10, 5)) # width, height
plt.plot(x, y)

plt.figure(figsize=(5, 10))
plt.plot(x, y)

plt.figure(figsize=(10, 5), dpi=200) # dpi 확대
plt.plot(x, y)

# ## 그래프 배경색

plt.figure(facecolor='yellow') # color picker
plt.plot(x, y)
