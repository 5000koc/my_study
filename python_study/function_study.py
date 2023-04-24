# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다

# 내장 함수(bulit-in) - 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list() 등등

# abs()
# absolute의 약자
# 입력한 숫자형 데이터의 절대값을 반환한다
# print(abs(100)) #100
# print(abs(-100)) #100
# print(abs(3.15)) #3.15
# print(abs(-3.15)) #3.15

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다
# print(sum([1, 2, 3, 4, 5]))

# max(리스트)
# 리스트 안의 최대값을 찾아 반환한다
# print(max([1, 2, 3, 4, 5]))

# min(리스트)
# 리스트 안의 최소값을 찾아 반환한다
# print(min([1, 2, 3, 4, 5]))

# chr()
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다
# print(chr(65)) # A 출력

# ord()
# 문자 1개를 입력받고 해당하는 정수를 반환한다 - 문자는 대소문자 구분할 것
# print(ord('A')) # 65 출력

# round(값)
# round(값, 소수자리수=0) 
# 반올림 함수
# print(round(1.234)) # 1
# print(round(1.234, 2)) # 1.23
# print(round(1.369, 1)) # 1.4

# 함수 정의(define) 함수를 만든다
# 함수 이름
# 함수 입력값 parameter
# 함수 결과값 return value
"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결과값
"""
# def 함수를 정의하는 명령어
# 함수 이름을 만등 때도 변수 이름처럼 영어, 숫자, _만 사용
# 숫자, 띄워쓰기, 기본명령어 사용하면 안됨
# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")
# print_names()    

# def get_name():
#     return "권오천"
# def print_my_name():
#     print(get_name())

# print_my_name()
# a = print_my_name() # 리턴이 없음
# b = get_name() # 리턴이 있음
# print(a)
# print(b)

# def add(a, b): # add 괄호 안에 들어간 a,b를 parameter, 매개변수, argument 하고 함
#     return a + b   
# def print_add(a, b):
#     print(a + b)
# # result = add(1, 2)
# # print(result)
# # print_add("안녕", "하세여")
# print_add(b = "하세요", a="안녕")

# def swap_number(a, b): 
#     temp = a  # a, b는 로컬(지역) 변수
#     a = b
#     b = temp
#     print(a, b)
#     return a, b

# a = 1 # 이 변수값은 swap_number와는 다른 변수로 지정된 글로벌(전역) 변수
# b = 2
# print("함수 호출 전", a, b)
# a, b = swap_number(a, b)
# print("함수 호출 후", a, b)   

# 연습문제
# 다음 함수를 정의하세요
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수2개의 곱
# def mul(a, b): # 변수인 b 에 추가로 값을 지정할 수 있음 default value parameter라고 함 함수호출시 변수인 b에 입력된 값이 없으면 기본값 사용가능
#     return a * b           # b=1 입력하면 됨 그러면 결과값은 1이 나옴
# print(mul(1, 2))          

# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# d, e, f = [4, 5, 6]
# g, h, i = (7, 8, 9)
# 파이썬에만 있는 기능으로 변수를 한줄에 하나씩이 아닌 한줄에 여러개 지정 가능함
# 가독성이 떨어져서 추천은 하지 않지만 저렇게 3개 정도라면 가능

# def test_func(x, test=[]): # 기본값을 사용할 때 리스트[]를 기본값으로 사용하지 말 것
#     test.append(x)
#     print(x, test)

# test_func(1)
# test_func(2)

# def test_func(x, test=5): 
#     test = test
#     print(x, test)

# test_func(1)
# test_func(2)

# def def test_func(x, test=None): 
#     if test == None
#         test = []
#     test.append(x)    
#     print(x, test)

# def sub(n1, n2, n3=0):  # 기본값이 있는 매개변수인 n3=0은 무조건 맨 뒤에 위치해야함
#     print(n1 - n2 - n3)

# 1 ~ 10까지 더한다
# *를 사용한 매개변수
# 입력값이 정해지지 않았을 때(모를때)
# def add_many(*args):
#     # 튜플처럼 사용가능
#     # 인덱싱, 슬라이싱 사용가능
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1 = add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(5, 4, 3, 2, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)

# def calc_many(n1, *args):
#     result = n1for i in args:
#         result += if
#     return n1

# 키워드 매개변수
# **kwargs <- 이렇게 씀 Keyward arguments의 줄임말
# 딕셔너리로 사용 변수의 입력이 유동적일 때 사용
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name="이름", age=10)    

# # 함수의 반환
# # return 반환값
# # return을 만나면 반환값을 반환함과 동시에 함수가 종료된다
# def test_func5():
#     print(1)
#     print(2)
#     return # 여기 아래에 있는 겻들은 모두 사용불가
#     print(3)
#     print(4)
#     print(5)
# # 함수의 반환값은 무조건 1개이다
# def test_func6(a, b):
#     return a + b, a * b # return (a + b, a * b) 와 같음
# result = test_func6(1, 2)
# res_add, res_mul = test_func6(1,2)
# # res_add, res_mul = (a+b, a*b)
# print(result)
# print(res_add, res_mul)

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수 True, 짝수 False

# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
# is_odd_number(5)

# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False

# def is_odd_number(n):
#     return n % 2 == 1

# 3가지 방법으로 가능 아래로 내려갈수록 간소화됨


# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 테두리와 함께 문자를 출력
# 함수이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None(함수가 return하는 값)

# def get_bordered_str(message):
#     message = str(message)
#     n = len(message) 
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str("hello")
# get_bordered_str(12345)

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면 km/h 단위로 변환한다
# 함수이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환되는 속도

# def convert_velocity(velocity):
#     # 1초에 1m가면 -> 1m/s
#     # 1m/s로 1시간동안 가면 몇m?
#     # 1m/s * 3600초 = 3600m/h
#     # 1m/s ==> 3.6km/h
    
#     result = velocity * 3.6
#     return result
# velocity = convert_velocity(10)
# print(velocity)

"""
n -> 4
*
**
***
****
"""

# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수줄의 별을 화면에 출력한다
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None

def print_stars(n):
    for i in range(n): # 0 ~ n-1
        for j in range(i+1): # 0 ~ i
            print("*", end="")
        print()

print_stars(4)

i = 0
while i < 0:
    j = 0
    while j < i+1:
        print("*", end="")
        j += 1
        print()
        i += 1