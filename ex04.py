
# for ================================
text = "python"
for i in text:
    # end = : print함수가 끝난 후 넣을 문자를 지정
    print(i, end=" ")

print()

for i in range(5):
    # 0 ~ 4
    print(i, end = " ")

print()

for i in range(1, 10, 2):
    # 1 ~ 10 2씩 증가
    print(i, end = " ")

print()


# string ==============================
str = "hello"
print(str * 3)
print(str + str)



# indexing ============================
text = "python"
# 이상 ~ 미만
print(text[0:3])
print(text[:3])
print(text[3:])
