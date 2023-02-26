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

# # Matplotlib
# 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리

import matplotlib.pyplot as plt

# ## 1. 그래프 기본

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)

print(plt.plot(x, y))

plt.plot(x, y)
plt.show()

# ## Title 설정

plt.plot(x, y)
plt.title('Line Graph')

# ## 한글 폰트 설정

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용 가능한 폰트 확인
[f.name for f in fm.fontManager.ttflist]

plt.plot(x, y)
plt.title('꺽은선 그래프')

plt.plot([-1, 0, 1],[-5, -1, 2])






