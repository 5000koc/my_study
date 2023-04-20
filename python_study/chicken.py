age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다")
if money >= beer and age >= 20:
    print("맥주를 마신다")
if money >= drink:
    print("음료를 마신다")

if money >= chicken + beer + drink and age >= 20:
    print("모두 먹고 마신다")
elif money >= chicken + beer and age >= 20:
    print("치킨과 맥주를 마신다")
elif money >= chicken + drink:
    print("치킨과 음료를 마신다")
elif money >= chicken:
    print("치킨 먹는다")
elif money >= beer + drink and age >= 20:
    print("맥주와 음료를 마신다")

# if문에서 추가로 if 문을 넣기 위해서는 코드블럭을 넣어서 작성