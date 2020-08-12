# iterable 객체 : 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체 (list, str, tuple, dict)
# sequence 객체 : int 타입 인덱스를 통해 원소에 접근 가능한 iterable 객체 (list, str, tuple)
#                dict는 다양한 타입을 통해 원소에 접근 가능하므로 sequence에 속하지 않음

list = [1, 2, 3, "숫자"]
str = "문자열"
tuple = (1, 2, 3, "숫자")
# tuple = 멤버요소를 변경할 수 없는 배열

dict = {"key" : "value"}
set = {1, 2, 3, 1, 2, 3}
# set = 멤버의 인덱스가 일정하지 않고 중복을 허용하지 않는 배열
print(dict["key"])
print(set)