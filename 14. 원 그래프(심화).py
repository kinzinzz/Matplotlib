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

# # 14. 원 그래프(심화)

# +
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

# +
values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'etc']
# colors = ['b', 'g', 'r', 'c', 'm', 'y']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
explode = [0.05] * 6

plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, explode=explode) # 소수점 첫번째 자리까지 
plt.show()
# -

wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':5}
plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops) # 소수점 첫번째 자리까지 
plt.show()


# +
def custom_autopct(pct):
    return ('%.1f%%' % pct) if pct >= 10 else ''

plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops, pctdistance=0.7) # 소수점 첫번째 자리까지 
plt.show()
# -

# ## DateFrame 활용

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')
df

grp = df.groupby('학교')
grp

grp.size()['북산고']

# +
values = [grp.size()['북산고'], grp.size()['능남고']]
labels = ['북산고', '능남고']

plt.pie(values, labels=labels)
plt.title('소속학교')
plt.show()
