# 필수조건 n>=1
# 1부터 n까지 합을 반환
def sum(n: int) -> int:
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret

# 재귀버전
def recursion_sum(n: int) -> int:
    if n == 1:
        return 1
    return n + recursion_sum(n-1)
