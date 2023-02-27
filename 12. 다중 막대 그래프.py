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

# # 12. 다중 막대 그래프

# +
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('../Pandas/score.xlsx')
df
# -

import numpy as np

np.arange(5)

np.arange(3, 6)

arr = np.arange(5)
arr + 100

arr * 3

df.shape # (row, column)

N = df.shape[0]
N

index = np.arange(N)
index

# +
w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')

plt.legend(ncol=3)

# +
plt.figure(figsize=(10,5))
plt.title('학생별 성적')

w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)

plt.xticks(index, df['이름'], rotation=45)
plt.show()
