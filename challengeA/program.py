import sys

def counter(seq):
    count = 0
    tallest = -100000000000

    i = len(seq) - 1

    while i >= 0:
        if seq[i] > tallest:
            tallest = seq[i]
            count +=1
        i -= 1

    return count

def main():
    lines = [num.strip() for num in sys.stdin.readlines()]
    parsed = [list(map(int, line.split())) for line in lines]
    for seq in parsed:
        print(counter(seq))

if __name__ == '__main__':
    main()
