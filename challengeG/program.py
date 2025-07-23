import sys
from collections import deque

def builder(lines, i):
    n = int(lines[i])
    i += 1
    graph = {}
    for r in range(n):
        row = list(map(int, lines[i].split()))
        graph[r] = []
        for c in range(n):
            if row[c] == 1 and r != c:
                graph[r].append(c)
        i += 1

    return graph, i

def calculate(graph):
    visited = set()
    count = 0

    def dfs(start):
        frontier = deque([start])
        while frontier:
            curr = frontier.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for next in graph[curr]:
                if next not in visited:
                    frontier.append(next)

    for chip in graph:
        if chip not in visited:
            dfs(chip)
            count += 1

    return count

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    i = 0
    s = 1

    while i < len(lines):
        graph, i = builder(lines, i)
        count = calculate(graph)
        print(f"System {s} isolated circuits: {count}")
        s += 1

if __name__ == '__main__':
    main()
