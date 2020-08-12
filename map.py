# map (function , iterable)
# iterable의 데이터들이 function의 입력 인자로 들어가 수행
# iterable 객체 : 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체 (list, str, tuple, dict)

def tenfold(a) :
    return a*10

# 16진수의 map 객체는 알아보기 어려우므로 list 객체로 변환
print(list(map(tenfold, [1,2,3,4,5])))

# map을 사용하지 않았을 경우
def tenfold(a):
    result = []
    for i in a:
        result.append(i*10)
    return result

print(tenfold([1,2,3,4,5]))
