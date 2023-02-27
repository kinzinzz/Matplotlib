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

# # 9. 막대 그래프(심화)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

# +
labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키

plt.barh(labels, values)
plt.xlim(175, 195)
# -

bar = plt.bar(labels, values)
bar[0].set_hatch('/')
bar[1].set_hatch('x')
bar[2].set_hatch('..')

# +
bar = plt.bar(labels, values)
plt.ylim(175,195)

for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height() +0.5, values[idx], ha='center', color='blue')
