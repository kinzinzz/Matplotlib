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

# # 10. DataFrame 활용

# +
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
# -

df = pd.read_excel('../Pandas/score.xlsx')
df

plt.plot(df['지원번호'], df['키'])

plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])

# +
plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])

plt.grid(axis='y', color='purple', alpha=0.5, ls='--', lw=2)
