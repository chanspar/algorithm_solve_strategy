# 중첩 반복문 대체하기
n = 7
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                print(i, j, k, l)

# 만약 5개를 골라야 하면? 5중반복문이 필요하다
'''
 이걸 재귀로 생각해봅시다.
 위 코드 조각이 하는 작업은 4개의 조각으로 나눌 수 있다.
 각 조각에서 하나의 원소를 고르는 것. 이렇게 원소를 고른뒤 남은 원소들을 고르는 작업을 재귀함수로 구현할 수 있다.
 
 - 원소들의 총 개수
 - 더 골라야 할 원소들의 개수
 - 지금까지 고른 원소들 번호
'''

def pick(n: int, to_pick: int, picked: list[int]):
    if to_pick == 0:
        print(picked)
        return
    smallest = picked[-1] if picked else -1
    for i in range(smallest + 1, n):
        picked.append(i)
        pick(n, to_pick - 1, picked)
        picked.pop()

pick(n, 4, [])
    