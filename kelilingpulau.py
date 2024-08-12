# input
i, j = map(int, input().split())
grid = []
for i in range(i):
    row = list(map(int, input().split()))
    grid.append(row)

def kelilingpulau(grid):
    rows = len(grid)
    cols = len(grid[0])
    keliling = 0
    
    # iterasi setiap sel pada grid
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                keliling += 4               
                # cek sel di atas
                if row > 0 and grid[row-1][col] == 1:
                    keliling -= 2        
                # cek sel di kiri
                if col > 0 and grid[row][col-1] == 1:
                    keliling -= 2
                    
    return keliling

print(kelilingpulau(grid))