def fill_spiral(n):
    # Létrehozunk egy nxn-es táblát, kezdetben minden cella None értékkel
    spiral = [[None for _ in range(n)] for _ in range(n)]
    
    # A csigavonal mintája, amely megismétlődik: -2, -3, -1
    pattern = [2, 3, 1]
    pattern_index = 0
    
    # A csigavonal irányainak meghatározása: jobbra, le, balra, fel
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    
    # Kezdőpont
    x, y = 0, 0
    
    for i in range(n*n):
        # Elhelyezzük a minta jelenlegi számát
        spiral[x][y] = pattern[pattern_index]
        
        # Frissítjük a minta indexét
        pattern_index = (pattern_index + 1) % len(pattern)
        
        # Megpróbáljuk elhelyezni a következő számot
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]
        
        # Ha elérünk a tábla szélére vagy egy már kitöltött cellához, irányt váltunk
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or spiral[next_x][next_y] is not None:
            direction_index = (direction_index + 1) % len(directions)
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]
        
        # Frissítjük a pozíciót a következő lépéshez
        x, y = next_x, next_y
    
    return spiral

# 6x6-os tábla esetén
spiral_board = fill_spiral(6)

# Kiírjuk az eredményt
for row in spiral_board:
    print(row)