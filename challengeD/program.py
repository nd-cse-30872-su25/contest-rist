import sys

scores = [2, 3, 7]

def counter(num):
    all = []

    def recurse(first, seq, total):
        if total == num:
            all.append(seq)
            return
        elif total > num:
            return
        for i in range(first, len(scores)):
            recurse(i, seq + [scores[i]], total + scores[i])

    recurse(0, [], 0)
    return all


def main():
    lines = [line for line in sys.stdin.readlines()]
    parsed = [int(num.strip()) for num in lines]
    for num in parsed:
        all = counter(num)
        count = len(all)

        if count == 0:
            print(f"There are 0 ways to achieve a score of {num}:")
        elif count == 1:
            print(f"There is 1 way to achieve a score of {num}:")
        else:
            print(f"There are {count} ways to achieve a score of {num}:")

        for seq in all:
            print(" ".join(str(s) for s in seq))


if __name__ == '__main__':
    main()
