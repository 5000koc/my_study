# 1 계단형, n을 입력받아, n만큼 줄을 만들고 계단 형태로 별찍기
# n = int(input('n:'))
# for i in range(n):
#    print(' '*i, end=' ')
#    print('*'*n)

# # 2 삼각형, 왼쪽 아래가 직각인 n만큼의 높이를 가지는 직각삼각형
# n = int(input('n:'))
# for i in range(1, n+1):
#    print('*'*i)
   
# 2-1 오른쪽 아래가 직각인 n만큼의 높이를 가지는 직각삼각형
# n = int(input('n:'))
# for i in range(1, n+1):
#    print(' '*(n-i), end=' ')
#    print('*'*i)

# # 3 역삼각형, 왼쪽 위가 직각인 n만큼의 높이를 가지는 직각삼각형
# n = int(input('n:'))
# for i in range(n):
#    print('*'*(n-i))

# 3-1 오른쪽 위의 직각인 n만큼의 높이를 가지는 직각삼각형
# n = int(input('n:'))
# for i in range(n):
#    print(' '*i, end=' ')
#    print('*'*(n-1))

# 4 피라미드, n만큼의 높이를 가지는 홀수개의 별 피라미드
# n = int(input('n:'))
# for i in range(1,n+1):
#    print(' '*(n-i), end=' ')
#    print('*'*(2*i-1))

# 5 x = [3, 6, 9, 20, -7, 5]의 값의 모든 요소에 10을 곱한 뒤 출력하세요
# x = [3, 6, 9, 20, -7, 5]
# for i in x:
#     print(i*10)
# 심화 : 출력과 리스트 x의 값에도 모두 10을 곱해주세요
# for i in range(0, len(x)):
#     x[i] = x[i]*10
# print(x)

# y = {"math":70, "science":80, "english":20}의 값의 모든 요소에 10을 더한 뒤 출력하세요
# 심화 : 출력과 딕셔너리 y의 값에도 모두 10을 더해주세요
# y = {"math":70, "science":80, "english":20}
# for key in y:
#     val = y[key]
#     y[key] = y[key]+10
#     print('%s : %d' %(key,val+10))

# 1~100 임의의 숫자를 맞추시오
# import random

# true_value = random.randint(1,100)
# input_value=99

# print('숫자를 맞춰보세요(1~100)')

# while true_value != input_value:
#     input_value = int(input())
#     if input_value > true_value: # 사용자의 입력값이 true_value 클 때
#         print('숫자가 너무 큽니다')
#     else:
#         print('숫자가 너무 작습니다') # 사용자의 입력값이 true_value 보다 작을 때
# print(f'정답입니다. 입력한 숫자는 {true_value} 입니다')

# word =["School", "game", "piano", "science", "hotel", "mountain"] 에서 글자 6개 이상의 단어를 모으시오
# word =["School", "game", "piano", "science", "hotel", "mountain"]
# a = list()
# for i in range(len(word)):
#     if len(word[i])>=6:
#         a.append(word[i])
# print(a)

# 1 ~ 100 까지의 숫자 중 3과 5의 공배수일 경우 3과 5의 공배수
# 나머지 숫자 중 3의 배수일 경우 "3의 배수"
# 나머지 숫자 중 5의 배수일 경우 "5의 배수"
# 모두 해당되지 않을 경우 그냥 숫자를 출력하세요
# 심화 1~ 입력한 숫자까지의 숫자 중


# b = int(input('정수를 입력하시오'))
# if b <= 0:
#     print('음수는 정의하지 않음')
# else:
#     for a in range(1, b+1):
#         if a % 3 == 0 and a % 5 == 0:
#             print('3과 5의 공배수')
#         elif a % 3 == 0:
#             print('3의 배수')
#         elif a % 5 == 0:   
#             print('5의 배수')
#         elif 1 <= a <= 100:
#             print(a)
#         else:
#             print('1과 100 사이의 숫자가 아닙니다')


# 사용자로부터 숫자를 계속 입력받다가 S or s 를 입력하면 합을 구라

# c = 0
# d = 1

# while (d == 1):
#     a = input()
#     if (a == 's' or a == 'S'):
#         d = 0
#     else:
#         a = int(a)
#         c += a
# print(c)

student_score = [0,0,0,0,0]
i = 0
for subject in mideterm_score: # 과목선택
    for score in subject: # 과목선택 후
        student_score[i] += score # 각 학생마다 개별로 교과점수를 저장
        # print(subject, score, 'i:', i, student_score) #kor -> math -> eng
        i += 1 # 학생 inde구분
    i = 0
else:
    a,b,c,d,e = student_score # 학생별 점수를 unpacking
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)


