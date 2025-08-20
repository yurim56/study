graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 수정된, 더 안전한 코드
def dfs_recursive(graph, node, visited):
    # 1. 현재 노드를 방문 처리
    visited.append(node)
    print(f"방문: {node}, 현재까지 방문 기록: {visited}") # 이해를 돕기 위한 print문

    # 2. 현재 노드와 연결된 다른 노드들을 순회
    for neighbor in graph[node]:
        # 3. 아직 방문하지 않은 노드라면
        if neighbor not in visited:
            # 4. 그 노드를 시작점으로 다시 DFS 함수를 호출 (재귀!)
            dfs_recursive(graph, neighbor, visited)
    return visited

# 실행
visited_nodes = dfs_recursive(graph, 'A', []) # 처음에 빈 리스트를 전달
print(f"\n최종 방문 순서: {visited_nodes}")