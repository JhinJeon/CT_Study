# 치킨 배달
from itertools import combinations
import math
from sys import stdin
n, m = map(int, stdin.readline().split())
# 그래프 그리기
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
# 집과 치킨집 좌표 저장해 두기
house = []
restaurant = []
for y in range(n):  # 세로 인덱스
    for x in range(n):  # 가로 인덱스
        # 집(1)인 경우
        if graph[y][x] == 1:
            house.append([y, x])
        # 치킨집(2)인 경우
        elif graph[y][x] == 2:
            restaurant.append([y, x])

# 치킨집 목록 중에서 경우의 수 선정
answer = math.inf   # 거리 비교 대상 설정
for store in combinations(restaurant, m):
    temp = 0    # 경우의 수 마다 거리 계산
    for h in house:
        distance = []
        for i in range(m):  # 집에서 가장 가까운 치킨집만 계산
            distance.append(abs(store[i][0]-h[0])+abs(store[i][1]-h[1]))
        temp += min(distance)
    if temp < answer:   # 최단 거리가 경신되면 해당 값으로 대체
        answer = temp
print(answer)
