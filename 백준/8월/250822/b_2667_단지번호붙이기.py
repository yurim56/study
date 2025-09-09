# 예시 지도 (원본을 유지하기 위해 복사해서 사용)
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

rows, cols = len(grid), len(grid[0])
count = 0

# 델타 배열 정의: 상, 하, 좌, 우
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# DFS 함수 정의
def dfs(r, c):
    # 유효성 검사: 범위, 바다('0') 여부
    if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == '1'):
        return

    # 방문했음을 표시하기 위해 '1'을 '0'으로 변경
    grid[r][c] = '0'

    # 델타 배열을 사용해 4방향 재귀 호출
    for dr, dc in deltas:
        dfs(r + dr, c + dc)

# 메인 로직 시작
for r in range(rows):
    for c in range(cols):
        # 아직 방문하지 않은 '1'을 발견하면
        if grid[r][c] == '1':
            count += 1      # 새로운 섬을 발견했으니 카운트 증가
            dfs(r, c)       # DFS로 해당 섬 전체를 방문 (지우기)

# 최종 결과 출력
print(f"지도의 섬의 개수: {count}")