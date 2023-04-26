def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__": # 이 명령어 아래로는 모듈화해서 import할 때 가져올 때 실행 안되게 함
    print(add(1, 2))
    print(sub(3, 4))
else:
    print(__name__)