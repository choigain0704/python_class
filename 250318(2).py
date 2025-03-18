#외부모듈 : 파이썬이 기본적으로 제공하는 모듈이 아닌 개발자가 추가로 설치해서 사용하는 모듈
#PIP(Python Installer for Package )
#pip 기본 명령어 mpm
#pandas : CSV,Excel 다양한 데이터 파일 쉽게 처리하고 분석
#numpy : 다차원 배열, 행렬 연산, 과학 계산 등에 사용
#matplotilib & seaborn : 그래프 및 차트를 그려서 데이터를 시각적으로
#openpyxl
#flask
#tensorflow & torch : 딥러닝, 머신러닝

import requests

response = requests.get("https://www.naver.com/")
print(response.status_code)
print(response.text)

import pandas as pd

df = pd.read_csv("data.csv")
print(df)
print(df.describe())

"""
count - 해당 열의 데이터 갯수
mean - 평균값
std - 표준 편차 (데이터의 분산 정도)
min - 최솟값
25% - 데이터의 25% 지점
max - 최대값
"""

# print(df["Age"])
# print(df[["Age", "Salary"]])
#
import matplotlib.pyplot as plt
#
# df.groupby("Age")["Salary"].mean().plot(kind="bar")
# plt.show()

import numpy as np
# #
# # arr1 = np.array([1,2,3,4,5]) #1차원 배열(리스트와 (,)콤마 유무 차이)
# # print(arr1)
# #
# # arr2 = np.array([[1,2,3],[4,5,6]])
# # print(arr2)
#
# #0으로 채운 다차원 배열
#
# zeros = np.zeros((3,4))
# print(zeros)
#
# #1로 채운 다차원 배열
# ones = np.ones((3,4))
# print(ones)
#
# #특정 값으로 채운 다차원 배열
# filled = np.full((3,4),5)
# print(filled)
#
# #연속된 값으로 채운 1차원 배열
# arr = np.arange(1,10,2)
# print(arr)
#
# #랜덤값으로 채운 다차원 배열
# random_arr = np.random.randint(1,100,(3,4))
# print(random_arr)
#
# #행열 계산
# arr1 = np.array([1,3,5])
# arr2 = np.array([2,5,8])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
#

import seaborn as sns

df = pd.read_csv("tips.csv")
plt.figure(figsize=(8,5))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data = df, palette= "Set1")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()
