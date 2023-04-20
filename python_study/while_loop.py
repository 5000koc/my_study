# while 반복문
"""
while 조건 :
    반복할 조건 
"""
# 조건이 참(True)인 경우에 코드를 계속 반복

# n = 1
# while n <= 10:
#     print(n)
#     n += 1 # n = n+1 과 같은 의미

#     # += 연산자
#     # 더하기 연산 후 할당
#     # n += 1 은 n = n+1 이라는 의미
#     # -= *= /= **= //= %= 산술연산자 다른 것들 모두 가능

# s1 = "안녕"
# s1 += "하세요" #문자로도 가능

# while 반복문을 활용하여 10부터 1까지 출력

# n = 10
# while n > 0: # while n >= 1: 과 같음
#     print(n)
#     n -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price:
#         print("커피를 구매했습니다")
#     money -= price
#     coffee -= 1
#     print("남은 커피 :", coffee)
#     if coffee == 0:
#         break

# break
# 반복문을 즉시 종료한다

# 1부터 10까지 홀수만 출력한다
# a = 1
# while a <= 10:
#      if a % 2 == 1:
#         print(a)
#         a += 1

# continue
# 반복문의 제일 처음으로 돌아감
# b = 0
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)
           

# 무한반복문
# 무한 루프
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다
# while True:
#     print("hi")

# while True:
#     user_input = input("종료하려면 1을 누르세요")
#     if user_input == "1":
#         break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a + b
# while True:
#     print("""
#        계산기
#     ===========
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)
    
#     operator = input("계산을 선택하세요 : ")
#     a = int(input("숫자를 입력하세요"))
#     b = int(input("숫자를 입력하세요"))
#     if operator == "1":
#         print(a, "+", b, "=", a + b)

#     elif operator == "2":
#         print(a, "-", b, "=", a - b)

#     elif operator == "3":
#         print(a, "*", b, "=", a * b)

#     elif operator == "4":
#         print(a, "/", b, "=", a / b)

#     user_input = input("종료하려면 q를 누르세요")
#     if user_input == "q":
#         break


# 사용자가 가지고 있는 돈을 입력받는다
# 구매할 수 있는 커피의 갯수와 잔돈을 출력한다
# 구매할 수 있는 음료수의 갯수와 잔돈을 출력한다
# 구매할 수 있는 콜라의 갯수와 잔돈을 출력한다
# 커피 500원 음료수 700원 콜라 930원
# 물품의 갯수는 무한하다 가정
# while 반복문 사용하여 작성

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈"))
# while idx < len(prices):
#     # while idx < 3:
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1

# while 반복문을 사용해서 scores 리스트에 시험점수 5개를 정수형으로 입력 받으시오

# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수:"))
#     scores.append(score)
#     n += 1
# print(scores)

# while 반복문을 사용하여 구구단 2단을 출력하세요

# n = 1
# while n < 10:
#     print("2 *", n, "=", 2*n) 
#     n += 1
