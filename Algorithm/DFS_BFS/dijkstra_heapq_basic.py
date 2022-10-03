# heapq를 이용한 다익
# https://brownbears.tistory.com/554

# 다익스트라 문제집 - https://www.acmicpc.net/workbook/view/3265

import heapq
import sys

INF = sys.maxsize


def dijstra(start):
    # 거리 넣을 배열 설정
    distance = {node:INF for node in graph}

    # 시작 노드의 거리는 0으로 설정
    distance[start] = 0
    queue = [] #우선 순위큐
    heapq.heappush(queue, (distance[start], start)) #heapq는 첫번째 데이터 기준으로 정렬해줌 -> 우선순위 고려 x (알아서 해줌)

    while queue:
        current_distance, node = heapq.heappop(queue)

        if distance[node] < current_distance:
            continue

        #해당 노드와 link 되어있는 노드 순회
        for next_node, next_distance in graph[node].items():
            # 현재노드 - 다음노드까지 사이거리
            gap_distance = current_distance + next_distance
            if gap_distance < distance[next_node]:
                # 사이거리가 작은걸로 업데이트 해줌
                distance[next_node] = gap_distance
                heapq.heappush(queue, (gap_distance, next_node))
    return distance
                
    
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9},
}

result = dijstra('A')
print(result)


