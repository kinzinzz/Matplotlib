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

# # 원 그래프(기본)

# +
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

# +
values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'etc']

plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False) # 소수점 첫번째 자리까지 
plt.show()

# +
values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'etc']

plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False) # 소수점 첫번째 자리까지 
plt.show()

# +
values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'etc']
# explode = [0.2, 0.1, 0, 0, 0, 0]
explode = [0.05] * 6

plt.pie(values, labels=labels, explode=explode)
plt.show()
# -

plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2, 0.3), title='언어별 선호도')
plt.show()
