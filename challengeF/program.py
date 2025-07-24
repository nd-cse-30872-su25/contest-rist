import sys

def read_grid(m):
    grid = []
    for _ in range(m):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append([0] + row)
    return grid


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    i = 0
    while i < len(lines):
        m, n = map(int, lines[i].split())
        grid = read_grid(m)



if __name__ == '__main__':
    main()
