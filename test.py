num = [1, 3, 4, 5, 2, 6, 9, 7, 8, 0]

a = 0
b = len(num) - 1


def ALG(number, head, tail):
    s = number[head]
    while head < tail:
        while head < tail and s <= number[tail]:
            tail -= 1
        number[head] = number[tail]
        while head < tail and s >= number[head]:
            head += 1
        number[tail] = number[head]
    number[head] = s
    return head


def quick_sort(number, head, tail):
    if head < tail:
        s = ALG(number, head, tail)
        quick_sort(number, head, s - 1)
        quick_sort(number, s + 1, tail)


if __name__ == '__main__':
    quick_sort(num, a, b)
    print(num)
