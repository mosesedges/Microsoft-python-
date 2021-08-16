def decending_order(n: int) -> int:
    if n < 0:
        print('no negative number')
    else:
        n = [int(x) for x in str(n)]
        n.sort()
        n.reverse()

    return n


print(decending_order(81297436))
