import sys
from collections import defaultdict

def builder(lines, i):
    n = int(lines[i])
    i += 1

    parents = defaultdict(list)
    children = defaultdict(list)

    for _ in range(n):
        parts = lines[i].split(":")
        left = parts[0].split()
        right = parts[1].split()

        for p in left:
            for r in right:
                parents[p].append(r)
        for c in right:
            for l in left:
                children[c].append(l)

        i += 1

    return parents, children, i

def calculate(givers, parents, children):
    spouses = {}
    for p1 in parents:
        for p2 in parents:
            if p1 != p2 and set(parents[p1]) == set(parents[p2]):
                spouses[p1] = p2

    for g in givers:
        siblings = set()

        if g in children:
            for p in children[g]:
                for c in parents[p]:
                    if c != g:
                        siblings.add(c)

        if g in spouses:
            sp = spouses[g]
            if sp in children:
                for p in children[sp]:
                    for c in parents[p]:
                        if c != sp:
                            siblings.add(c)

        final = set()
        for x in siblings:
            for c in parents[x]:
                final.add(c)

        if final:
            print(f"{g} needs to buy gifts for: {', '.join(sorted(final))}")
        else:
            print(f"{g} does not need to buy gifts")

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    i = 0

    while i < len(lines):
        if lines[i] == '0':
            break

        parents, children, i = builder(lines, i)

        j = int(lines[i])
        i += 1

        givers = lines[i:i + j]
        i += j

        calculate(givers, parents, children)

if __name__ == '__main__':
    main()
