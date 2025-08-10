T = int(input())
 
for tc in range(1, T+1):
    width = int(input())
    heights = list(map(int, input().split()))
    answer = 0
    max_height =0
 
    for i in range(width):
        if heights[i] <= max_height:
            continue
 
        max_height = heights[i]
        lower_count = 0
        for j in range(i+1, width):
            if heights[i] > heights[j]:
                lower_count += 1
 
        answer = max(answer, lower_count)
 
    print(f'#{tc} {answer}')