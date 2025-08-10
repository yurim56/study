for tc in range(1, 11):
    N = int(input())
    dump_box = list(map(int, input().split()))
    for i in range(N):  
        diff = max(dump_box) - min(dump_box)

        if diff <= 1:
            break
        
        dump_box[dump_box.index(max(dump_box))] -= 1
        dump_box[dump_box.index(min(dump_box))] += 1
      
    result = max(dump_box) - min(dump_box)
    print(f'{tc} {result}')