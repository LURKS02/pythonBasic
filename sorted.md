### sorted()
```python
# 오름차순
sorted(list)
# 내림차순
sorted(list, reverse=True)
```

### lambda
```python
# y축 기준으로 오름차순
sorted(list, key=lambda x:x[1])
# y축 기준으로 내림차순
sorted(list, reverse=True, key=lambda x:x[1])
```
기본적으로 2차원 배열에 sorted()를 적용시킬 경우 x축을 기준으로 정렬된다. 이를 y축 기준으로 정렬시키기 위한 방법
