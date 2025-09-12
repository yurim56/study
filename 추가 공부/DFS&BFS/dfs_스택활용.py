graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start_node):
    need_visited, visited = list(), list() # 빈 리스트 만들어두기
    
    need_visited.append(start_node) # 시작 노드 넣어주기

    while need_visited: # 방문이 필요한 노드가 있다면 -> need_visited가 비어있지 않으면 while 계속 진행
        node = need_visited.pop() # 맨 뒤에 있는 값 빼기
        if node not in visited: # 방문 리스트에 없으면
            visited.append(node) # 넣어주기
            need_visited.extend(graph[node]) # graph에 있는 값 넣어주기
            need_visited.extend(graph[node][::-1]) # -> 이렇게 하면 ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J'] 이렇게 출력

    return visited 
            
print(dfs(graph, 'A'))

# 출력값
# ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
            
            
            
# extend를 사용하는 이유 -> 지금 그래프가 []리스트로 묶여있는데 요소 하나 하나 넣어줘야해서
'''
<append>
>>> nums = [1, 2, 3]
>>> nums.append(4)
[1, 2, 3, 4]

>>> nums.append([5, 6])
[1, 2, 3, 4, [5, 6]] # 리스트가 하나의 객체로 추가되었음
'''

'''
<extend>
>>> nums = [1, 2, 3]
>>> nums.extend([4, 5])
[1, 2, 3, 4, 5]  #리스트로 주어진 [4, 5]의 요소가 각각 추가 되었음

>>> a = [10]
>>> nums.extend(a) 
[1, 2, 3, 4, 5, 10]
'''
            