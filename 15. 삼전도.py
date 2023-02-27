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

# # 삼전도 그래프

# +
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
# -

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')
df

df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]
df

plt.scatter(df['영어'], df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

import numpy as np
sizes = np.random.rand(8) * 1000
sizes

plt.scatter(df['영어'], df['수학'], s=sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

sizes = df['학년'] * 500 # 1학년 = 500, 2학년 = 1000, 3학년 =1500

plt.scatter(df['영어'], df['수학'], s=sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3) # 학년에 따라 색깔을 적용
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

plt.figure(figsize=(10, 10))
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3) # 학년에 따라 색깔을 적용
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.5, orientation='horizontal')
