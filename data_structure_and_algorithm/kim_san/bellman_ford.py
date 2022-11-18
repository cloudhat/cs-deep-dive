import sys
input = sys.stdin.readline

INF = int(1e9) # 무한대 값

# 노드, 간선의 개수 입력
v, e = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트
edges = []

# 최단거리 테이블을 무한대로 초기화
distance = [INF] * (v + 1)

# 모든 간선의 정보 입력
for _ in range(e):
    sv, ev, cost = map(int, input().split())
    edges.append((sv, ev, cost))

# 벨만-포드 알고리즘
def bellmanFord(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # v번 edge relaxation을 반복.
    # v - 1번 탐색하고 마지막 한번은 Negative cycle 존재 확인
    for i in range(v):
        # 매 반복마다 모든 간선을 확인하며 갱신
        for j in range(e):
            curNode, nextNode, edgeCost = edges[j]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[curNode] != INF and distance[curNode] + edgeCost < distance[nextNode]:
                distance[nextNode] = distance[curNode] + edgeCost
                # v번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                if i == v - 1:
                    return False

    # 벨만-포드 정상종료
    return True

if bellmanFord(1):
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리를 출력
    for i in range(2, v + 1):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print("도달할 수 없다.")
        else:
            print(distance[i])
else:
    print("Negative Cycle Exist")


#출처 : https://headf1rst.github.io/algorithm/bellmanford/