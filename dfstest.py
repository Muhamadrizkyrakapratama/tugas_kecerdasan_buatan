from collections import deque

def print_maze_solution(maze, path):
    """Fungsi untuk mencetak labirin dengan jalur solusinya."""
    
    solution_maze = [list(row) for row in maze]
    if path:
        
        for r, c in path:
            if solution_maze[r][c] == ' ':
                solution_maze[r][c] = '*'
    for row in solution_maze:
        print(" ".join(row))

def solve_maze_bfs(maze, start, end):
    """
    Menemukan solusi JALUR TERPENDEK dalam labirin menggunakan BFS.

    Returns:
        list: Jalur terpendek dari start ke end, atau None jika tidak ada.
    """
    rows, cols = len(maze), len(maze[0])
    
   
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (x, y), path = queue.popleft() # Ambil dari awal antrian

        
        if (x, y) == end:
            return path # Solusi ditemukan, ini pasti yang terpendek

       
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            
            if 0 <= nx < rows and 0 <= ny < cols and \
               maze[nx][ny] != '#' and (nx, ny) not in visited:
                
                visited.add((nx, ny))
                new_path = path + [(nx, ny)]
                queue.append(((nx, ny), new_path)) # Tambahkan ke akhir antrian
    
    return None # Tidak ada solusi yang ditemukan

# --- Program Utama ---
if __name__ == "__main__":
    
    labirin = [
        ['A', ' ', ' ', '#', ' ', ' '],
        ['#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', ' ', 'E']
    ]
    
    
    titik_mulai = (0, 0)
    titik_akhir = (4, 5)

    print("## Labirin Awal ##")
    print_maze_solution(labirin, None)
    print("\n" + "="*20 + "\n")
    
    print("## Mencari Solusi Terpendek (BFS)... ##")
    jalur_terpendek = solve_maze_bfs(labirin, titik_mulai, titik_akhir)
    
    if jalur_terpendek:
        print("✅ Solusi terpendek ditemukan!")
        print_maze_solution(labirin, jalur_terpendek)
    else:
        print("❌ Tidak ada solusi yang ditemukan.")