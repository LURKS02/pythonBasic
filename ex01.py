
# print ============================
print('출력문 - 홀따옴표')
print("출력문 - 쌍따옴표")
print(0)
print("문자 ", "연결")

print("%d" % 10)
print("%.2f" % 10.0)
print("%c" % "a")
print("%s" % "string")
print("%d, %c" % (10, "a"))


# 연산자 ============================
# +, -, *, /, //(몫), %(나머지)
# >, <, ==, !=, >=, <=
# and, or


# 변수 ==============================
num = 10
print(num)


# input =============================
age = input()
print(age)
print(type(age)) #데이터 타입
print(type(int(age))) #형변환

age = int(input("나이를 입력하세요. : "))


# if ================================
if True :
    print ("True")
elif False :
    print("False")
else:
    print("Error")

