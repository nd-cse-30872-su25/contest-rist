import sys

def checker(word, target):
    if len(word) != len(target):
        return 0

    def pattern(s):
        indexes = {}
        pattern = []
        curr = 0

        for char in s:
            if char not in indexes:
                indexes[char] = curr
                curr += 1
            pattern.append(indexes[char])

        return pattern

    if pattern(word) == pattern(target):
        return 1
    else:
        return 0


def main():
    lines = [num.strip() for num in sys.stdin.readlines()]
    words = [line.split() for line in lines]
    for each in words:
        if (checker(each[0], each[1])) == 1:
            print("Isomorphic")
        elif (checker(each[0], each[1])) == 0:
            print("Not Isomorphic")


if __name__ == '__main__':
    main()
