# Vacuum Robot Game

def simulate_robot(grid, commands, orientation, health):
    dirs = ["N", "E", "S", "W"]
    moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

  
    start = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)

    row, col = start
    for cmd in commands:
        if health <= 0:
            break
        if cmd == "L":
            orientation = dirs[(dirs.index(orientation) - 1) % 4]
        elif cmd == "R":
            orientation = dirs[(dirs.index(orientation) + 1) % 4]
        elif cmd == "F":
            dr, dc = moves[orientation]
            new_r, new_c = row + dr, col + dc
            if grid[new_r][new_c] == "#":
                health -= 1
            else:
                row, col = new_r, new_c

    print("Final position:", row + 1, col + 1, orientation, "Health:", max(health, 0))

# Test grid1
grid1 = [
    list("#####"),
    list("#...#"),
    list("#.#S#"),
    list("#...#"),
    list("#####")
]
simulate_robot(grid1, "FFLFFRFFF", "E", 3)

# Test grid2
grid2 = [
    list("#######"),
    list("#..#..#"),
    list("#.#.#S#"),
    list("#.#...#"),
    list("#..####"),
    list("#.....#"),
    list("#######")
]
simulate_robot(grid2, "FLLFFFRFFLFFRFF", "W", 10)
