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

# # 7. 여러 데이터

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

# ## COVID-19 백신 종류별 접종 인구

# +
days = [1, 2, 3] # 1일,2일,3일
az = [2, 4, 8] # 단위: 만명
pfizer = [5, 1, 3]
moderna = [1, 2, 5]

plt.plot(days, az)
plt.plot(days, pfizer)
plt.plot(days, moderna)

# +
plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', ls='--')
plt.plot(days, moderna, label='moderna', marker='s', ls='-.')

plt.legend(ncol=3)
