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

# # 5. 파일 저장

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)
plt.savefig('graph.png', dpi=100)

plt.figure(dpi=200)
plt.plot(x, y)
plt.savefig('graph_200', dpi=100)
