# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rHJYYtsCSst5iCtb7yUrGczO7pVlDnaY
"""

# a = [1,2,3,4,5]
# swap_value(a[1], a[2])

# def swap_value(x, y):
#   temp = x
#   x = y
#   y = temp
# print(a)

a = [1,2,3,4,5]
swap_offset(1,2)

def swap_offset(offset_x, offset_y):
  temp = a[offset_x]
  a[offset_x] = a[offset_y]
  a[offset_y] = temp
print(a)

a = [1,2,3,4,5]
swap_reference

def swap_reference(list,offset_x, offset_y):
  temp = list[offset_x]
  list[offset_x] = list[offset_y]
  list[offset_y] = temp

# 이 함수는 두 개의 숫자를 input으로 받으면 작은 구로 큰 수를 난 몫과 나머지를 반환하는 함수이다
# 반환값은 튜플로 되어 있으며, 몫, 나머지 순으로 되어있다.
# 단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은 수가 0이라면 화면에 '0은 사용할 수 없습니다'를 출력하고 종료되어야 한다.

def div3(a, b):
  if a < b:
    big = b
    small = a
  elif b <= a:
    big = a
    small = b
  else:
    print('정수가 아닙니다')
  if small == 0:
    print('0은 사용할 수 없습니다')
  elif abs(big) < 0 or abs(small) < 0:
    print('정수를 입력해주세요')
  else:
    q = big // small
    r = big % small
    return (q, r)

div3(3, 5)

# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력을 하는 함수를 짜보자
# 끊는 단위는 따로 정하지 않으면 2로 설정해보자

def func(string, unit = 2):
  i = 0
  while i < len(string):
    print(string[i:i + ])

add_all([1,2,3,4,5,6,7,8,9,10])

def add_all3(*inputs):
  s = 0
  for i in args:
    for j in i:
      s += j
    return s

def add_all2(*inputs):

def add_all4(*args):
  temo = 0
  for i in range(len(args)):
    if type(args[i]) == list:
      for j in args[i]:
        temp += j
      else:
        temp += args[i]
  return temp

# 1부터 시작해서 어떤 범위에 있는 모든 정수를 곱하는 것
# Ex) 5! = 120

# 재귀적으로 하지 않은 것
def fact(n):
  f = 1 # 곱을 계산할 변수의 초기값
  for i in range(1, n+1): # 1부터 n까지 반복
    f = f * i # 곱셈연산
  return f

# 재귀적으로 하는 것
def fact(n):
  if n <= 1: # n이 1 이하이면 종료조건
    return 1
  return n * fact(n-1)

people = ['펭수', '뽀로로', '뚝딱이', '텔레토비']

def func1(line):
    new_lines = []
    i = 1 # 대기번호를 트랙킹하는 변수
    for x in lines:
        print("대기번호 %d번 : %s" %(i, x))
        new_lines.append((i, x__))
        i += 1
    return new_lines

lines = func1(people)

str_list = ['one', 'two', 'three' 'four']
num_list = [1, 2, 3, 4]


a = 2
b= plus_two(a)

def plus_two(num):
    return num + 2

print(b)

lambda x : x + 2

func2 = lambda x : x + 2

c = func2(2)

c

items = [1, 2, 3, 4, 5]

squared = []
for i in items :
    squared.append(i * i)
print(squared)

squared_map = list(map(lambda x : x ** 2, items))
print(squared_map)

# p.251
items = [1, 24, 3, 6, 7]

str_items = list(map(lambda x:str(x), items))
print(str_items)

# p.254
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 = []
for x in range(10):
    list_2.append(x)
print(list_2)

# p.255 답

# 1 구구단 2단

tables = [2 *x for x in range(1,10)]
print(tables)

# 2 코로나
sentence = '코로나바이러스를 예방하기 위해 사회적 거리두기와 마스크 쓰기와 손씻기를 생활화 합시다'

len_sent = [len(s) for s in sentence.split()]
print(len_sent)

# p.256
# 10부터 20까지의 숫장 중 짝수만 담은 리스트를 만들어보자

list3 =[]
for x in range(10, 21):
    if x % 2 == 0:
      list3.append(x)
print(list3)

lc_2 = [x for x in range(10, 21) if x % 2 == 0]
print(lc_2)

lc_3 = [x ** 2 for x in range(1, 11) if x ** 2 < 50]
print(lc_3)

# for + if + else
# 1부터 10까지의 숫자 중 홀수이면, 어떤 제곱수를 짝수이면 세제곱수를 담은 리스트를 만들어보시오

list_4=[]
for x in range(1, 11):
  if x % 2 == 1:
    list_4.append(x ** 2)
  else:
    list_4.append(x ** 3)
print(list_4)

# p.259 를 간결하게
[x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]

# p.260
# for문+for문

word_1 = 'hello'
word_2 = 'world'

result = [i + j for i in word_1 for j in word_2]
result

import numpy as np

n = 1000000
numpy_arr = np.arange(n)
python_list = list(range(n))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# python_list = [x**3+10 for x in python_list]

# Commented out IPython magic to ensure Python compatibility.
# %%time
# numpy_arr = numpy_arr**3+10

# 벡터화
# 배열은 for문을 작성하지 않고 데이터를 일괄처리하는 것

arr = np.array([[1,2,3],[4,5,6]])
arr

arr + arr

arr/arr

# 브로드캐스팅
# 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy의 기능

arr

10 - arr

arr * 3

arr/3

arr2 = np.array([100,200,300])

arr3 = np.array([100,200])

arr_1 = np.array([1,2,3])
arr_1 + arr_1

arr2 = np.array([100,200,300])

# dtype
# 배열에 담긴 원소의 자료형

arr.dtype
dtype('int64')

arr.ndim # ndim - 배열의 차원의 갯수

arr.shape

# 0차원 = 상수

import numpy as np
a = np.array(10)
print(a)
print(a.ndim)

a = np.array([1,2,3])
print(a)
print(a.ndim)

# 2차원

a = np

# 3 차원

a = np.array([[[1,2],[3,4]]])
print(a)
print(a.ndim)
print(a.shape)

# range 함수를 이용

arr1 = np.array(range(20))
arr1

arr2 = np.arange(20)
arr2

np.zeros(10)

np.empty((2,3),dtype = np.float32)

np.arange(-3,3)

np.arange(3, 50, 3)

np.linspace(0, 1, 6)

# 로또번호 생성기
import numpy as np
def make_lotto(count):
  for i in range(count):
    lotto_num = [] # 로또 번호가 담길 리스트형 변수
    for j in range(6): # 6번 반복
      lotto_num = np.random.choice(range(1,46),6,replace = False)
      lotto_num.sort() # 값 정렬
  print('{}.로또번호:{}'.format(i+1,lotto_num))

count = int(input('로또번호를 몇개 생성할까요?'))
make_lotto(count)