import sys

equation = "(((9 ? 8) ? 7) ? 6) ? (5 ? (4 ? (3 ? (2 ? 1))))"
operations = ['+', '-', '*']

def permutations(length=0, curr=[]):
    if length == 8:
        yield curr
        return
    for op in operations:
        yield from permutations(length + 1, curr + [op])

def changer(n):
    for p in permutations():
        x = equation
        for op in p:
            x = x.replace('?', op, 1)
        if x.count('?') == 0:
            result = eval(x)
            if result == n:
                print(f"{x} = {n}")

def main():
    lines = [line for line in sys.stdin.readlines()]
    nums = [int(num) for num in lines]
    for n in nums:
        changer(n)


if __name__ == '__main__':
    main()
