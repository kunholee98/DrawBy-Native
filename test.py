from collections import deque
def solution(grid, clockwise):
    visited = []
    tri = []
    l = len(grid)
    for line in grid:
        tri.append(list(line))
        visited.append([False for _ in range(len(line))])
    print(tri)
    sols = [[
        [(0,-1),(1,1),(0,1)],
        [(1,1),(0,1),(0,-1)],
        [(0,1),(0,-1),(1,1)]
    ],[
        [(0,1),(-1,-1),(0,-1)],
        [(-1,-1),(0,-1),(0,1)],
        [(0,-1),(0,1),(-1,-1)]
    ]
    ] 
    def Find(sols,visited,x1,y1,x2,y2,x3,y3):
        result = []
        for sol in sols:
            dx1,dy1 = sol[0]
            cx1,cy1 = x1+dx1, y1+dy1
            print(visited[2][2])
            try:
                if 0<=cx1<l and 0<=cy1<2*cx1+1 and not visited[cx1][cy1]:
                    dx2,dy2 = sol[1]
                    cx2,cy2 = x2+dx2, y2+dy2
                    dx3,dy3 = sol[2]
                    cx3,cy3 = x3+dx3, y3+dy3
                    result.append((cx1,cy1,cx2,cy2,cx3,cy3))
            except: 
                print(cx1,cy1)
        return result
    
    def Change(grid, clock, x1,y1,x2,y2,x3,y3):
        if clock:
            grid[x1][y1], grid[x2][y2],grid[x3][y3] = grid[x2][y2],grid[x3][y3],grid[x1][y1]
        else:
            grid[x1][y1], grid[x2][y2],grid[x3][y3] = grid[x3][y3],grid[x1][y1],grid[x2][y2]
    
    q = deque([(0,0,l-1,0,l-1,2*l-2)])
    rev = 0
    while q:
        temp = q.popleft()
        x1,y1,x2,y2,x3,y3 = temp
        visited[x1][y1] = True
        visited[x2][y2] = True
        print(x3,y3)
        visited[x3][y3] = True
        q += Find(sols[rev],visited,x1,y1,x2,y2,x3,y3)
        rev = 0 if rev else 1
        Change(tri, clockwise,x1,y1,x2,y2,x3,y3)
        print(q)
    answer = []
    for line in tri:
        answer.append(''.join(line))  
    print(answer)
    return answer

print(solution(["1","234","56789"],True))
print(solution(["1", "234", "56789", "abcdefg", "hijklmnop"], True))