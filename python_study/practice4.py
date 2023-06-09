# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 반환하는 함수
# 함수 이름 : sum_3_5

def sum_3_5(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

# def sum_3_5(n):
#     result = 0
#     for i in range(1, n):
#         if i % 3 == 0:
#             result += i
#         if i % 5 == 0:
#             result += i # 잘못된 코드 if가 2번 들어가므로 2번 모두 실행 두번째 if를 elif로 수정해야함
#     return result

# 정육면체 주사위 2개가 있다
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 모두 print하는 함수를 정의하시오
# 함수이름 : double_dice
# 출력 예시  : 1, 2    6, 3

# 2중 for문으로 작성
def double_dice():
    for i in range(1, 7): # 1 ~ 6
        for j in range(1, 7): # 1 ~ 6
            print(i, j)

# while로 작성
i = 1
while i < 7:
    j = 1
    while j < 7:
        print(i, j)
        j += 1
    i += 1

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하시오
# 함수이름 : get_diff

def get_diff(a, b):
    result = abs(a - b)
    if a > b:
        result = a - b
    else:
        result = b - a
    return result

# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개의 정수(0 ~ 9, 중복가능)를 사용하여 만들 수 있는 가장 큰 수를 반환하는 함수를 정의하세요
# 함수이름 : get_biggest
# 파라미터 : a, b, c, d, e
# 반환값 : result

def get_biggest(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    numbers.sort()
    result = 0
    for i in range(len(numbers)) :
        result += numbers[i] * (10 ** i)   
    return result

def get_biggest(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    numbers.sort(reverse=True) # 리버스 명령어로 정렬한 뒤 str로 문자열로 바꾸고 등록
    result = ""
    for i in numbers:
        result += str(i)
    return int(result)   

# 별 찍기 2
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다
# 함수이름 : print_stars2

def print_stars2(n):
    for i in range(1, n+1): # 1 ~ n
        print(" ", * (n - 1) + "*" * i)

print_stars2(10)