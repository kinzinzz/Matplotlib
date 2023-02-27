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

# # 16. 여러 그래프

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

# +
fig, axs = plt.subplots(2, 2, figsize=(15, 10)) # 2 x 2 에 해당하는 plot 들을 생성
fig.suptitle('여러 그래프 넣기')

# 첫 번째 그래프
axs[0, 0].bar(df['이름'], df['국어'], label='국어 점수')
axs[0, 0].set_title('첫 번째 그래프')
axs[0, 0].legend() # 범례
axs[0, 0].set(xlabel='이름', ylabel='점수') # x, y 축 label
axs[0, 0].set_facecolor('lightyellow') # 전경 색
axs[0, 0].grid(ls='--', lw=0.5)

# 두 번째 그래프
axs[0, 1].plot(df['이름'], df['수학'], label='수학 점수')
axs[0, 1].plot(df['이름'], df['영어'], label='영어 점수')
axs[0, 1].legend()

# 세 번째 그래프
axs[1, 0].barh(df['이름'], df['키'])

# 네 번째 그래프
axs[1, 1].plot(df['이름'], df['사회'], color='green', alpha=0.5)
