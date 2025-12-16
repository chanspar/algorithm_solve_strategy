# 필수조건 n>=1
# 1부터 n까지 합을 반환
def sum(n: int) -> int:
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret

# 재귀버전
# 조각중 n만 때어보고 + (n-1) 조각들이 남는데 1~n-1합입니다.
# n + recursion_sum(n-1)이 결국 1~n합이 됩니다.
def recursion_sum(n: int) -> int:
    if n == 1: # 더이상 쪼개지지 않는 작업: 기저 사례(base case)가 필요하다.
        return 1
    return n + recursion_sum(n-1)
