
listArr = [2, 3, 2, 1, 3, 3]


def filterFun(x):
    return x < 2


productss = filter(filterFun, listArr)


print(list(productss))
