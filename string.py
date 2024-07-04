# hello_world = "엄마가 말했다. '밥 먹었니?'"
# print(hello_world)
# #
# # name = "홍길동"
# # money = 100
# print("안녕하세요. ", name, "님 반갑습니다.")
# print("입력하신 금액은", money, "원 입니다.")

# 데이터 출력 시, % 기호 사용하는 방법
print("안녕하세요. 저의 이름은 %s입니다." %"최아진")

name = "최아진"
print("안녕하세요. 저의 이름은 %s입니다." %name)

money = 10000
print("입력하신 금액은 %d 원 입니다." %money)


a= 7
b = 3
result = a + b
print(result)

hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

# 문자열 슬라이싱
자유로운_문자열 = "집에 가고 싶다. 두시간 남았다. 그런데 저는 더 빨리 집에 가고 싶어요."
print(len(자유로운_문자열))
print(자유로운_문자열[0:9])

date = "2001.12.12"
print("바꾸기 전의 데이터 : ", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터 : ", date)

# 연습문제 6.
ENG = 'abcd'
print("바꾸기 전의 영어 : ", ENG)

ENG = ENG.replace("a", "A")
print("바꾼 후의 데이터 : ", ENG)

pyt = 'Python'
print(len(pyt))
# 슬라이싱 해보기
new = pyt[5]+pyt[4]+pyt[3]+pyt[2]+pyt[1]+pyt[0]
print(new)

# 문자열 여러 줄 출력하기





