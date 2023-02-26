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

# # 8. 막대 그래프

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키
plt.bar(label, values)

labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키
plt.bar(label, values, color='r')

# +
labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키
colors = ['r', 'g', 'b']

plt.bar(label, values, color=colors, alpha=0.5)

# +
labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키

plt.bar(label, values)
plt.ylim(175, 195)
# -

plt.bar(label, values, width=0.5)

plt.bar(labels, values, width=0.3)
plt.xticks(rotation=45) # x 축의 이름 데이터를 각도를 45도로 설정
plt.yticks(rotation=45)

# +
labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184] # 키
ticks = ['1번', '2번', '3번']

plt.bar(labels, values)
plt.xticks(labels, ticks, rotation=90)
