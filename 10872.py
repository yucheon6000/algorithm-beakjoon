# 팩토리얼 재귀 함수
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

# 결과
k = int(input())
result = factorial(k)
print(result)