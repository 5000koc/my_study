# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, -, *, /)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력 받은 후 결과를 print 한다
# 계산식 결과를 calculator_result.txt 파일에 기록한다
# 사용자가 'q'를 누르면 종료한다


def add(a, b):
    result = str(a)+" + "+str(b)+" = "+str(a+b)
    print(result)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(str(result))
def sub(a, b):
    result = str(a)+" - "+str(b)+" = "+str(a+b)
    print(result)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
         f.write(str(result))
def mul(a, b):
    result = str(a)+" * "+str(b)+" = "+str(a+b)
    print(result)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(str(result))
def div(a, b):
    result = str(a)+" / "+str(b)+" = "+str(a+b)
    print(result)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(str(result))
while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 계산을 입력하세요:")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    if operator == "1":
        add(a, b)
    elif operator == "2":
        sub(a, b)
    elif operator == "3":
        mul(a, b) 
    elif operator == "4":
        div(a, b) 

