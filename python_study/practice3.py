# 2 ~ 9 사이의 숫자를 입력받아 해당하는 단의 구구단을 출력하세요
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우, 잘못 입력되었다고 출력하게 하고 다시 입력받으세요

# n = int(input("단"))
# # 2 ~ 9 사이의 값이 아닐 때
# if n < 2 or n > 10:
#     # 다시 입력받기
#     pass 
# # 2 ~ 9 사이의 값일 때 True
# if n >= 2 and n <= 9:
#     pass
# if 2 <= n <= 9:
#     pass

# n = int(input("몇단"))
# while not 2 <= n <= 9:
#     print("2 ~ 9 사이의 숫자를 입력하세요")
#     n = int(input("단수"))

# for i in range(1, 10): # range()에 9를 넣어도 됨 코드를 다르게 짜면 됨
#     print(n, "*", i, "=", n*i)

# 정수를 입력받고 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하시오
# 10이면 9
# 11도 9

# n = int(input("정수 :"))
# i = 1
# while True:
#     # i * i
#     if i ** 2 >= n:
#         break
#     answer = i ** 2
#     i += 1
# print(answer)

# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요

# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]
# for i in range(5):
#     print(li_1[i] + li_2[i] + li_3[i])

# # zip()
# # 길이가 같은 list를 묶어서 for문 등으로 사용가능한 iterable을 반환된다
# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]    
# for x, y, z in zip(li_1, li_2, li_3):
#     print(x + y + z)

# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]
# i = 0
# while i < 5:
#      print(li_1[i] + li_2[i] + li_3[i])
#      i += 1

# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하시오
# 단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 '짝' 이라고 출력하시오

# n = int(input("정수 :"))
# for i in range(1, n + 1):
#     # str 함수는 숫자형를 문자형으로 바꿔줌
#     answer = i
#     for j in str(i):
#         if int(j) % 3 == 0 and j != "0":
#             answer = "짝"
#             continue
#     print(answer)       

# 정수를 입력받고 그 정수의 약수를 모두 출력하세요
# 약수 : 나누었을 때 나머지가 0으로 떨지게 하는 수

n = int(input("정수 :"))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)  

i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1