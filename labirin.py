from collections import deque

# input
n, m = map(int, input().split())

maze = []
visited = []

# temp input pada variabel
for i in range(n):
    maze.append(input().strip())
    visited.append([False] * m)
    
# inisialisasi
startX, startY = None, None
endX, endY = None, None

# cari posisi A dan B
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'A':
            startX, startY = i, j
        elif maze[i][j] == 'B':
            endX, endY = i, j
            
queue = deque()
queue.append((startX, startY, 0, ""))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directions = ['U', 'R', 'D', 'L']

while queue:
    x, y, distance, path = queue.popleft()
    if((x == endX) and (y == endY)):
        print("Ya")
        print(distance)
        print(path)
        break
        
    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        if((nextX < 0) or (nextX >= n) or (nextY < 0) or nextY >= m):
            continue
        if(maze[nextX][nextY] == '#'):
            continue
        if visited[nextX][nextY]:
            continue
        visited[nextX][nextY] = True
        queue.append((nextX, nextY, distance+1, path+directions[i]))
else:
    print("Tidak")