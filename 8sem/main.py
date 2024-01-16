l1 = ['1', '123', '123', '12', '1', '123']
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]

d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}


def n1(l1):
    new_l1 = [len(i) for i in l1]
    return new_l1


def n2(l1, x):
    n = sum([1 for i in l1 if len(i) > 2 * x])
    return n


def n3(l2):
    new_l2 = [l2[i] * (i + 1) for i in range(len(l2))]
    return new_l2


def n4(l2):
    new_l2 = [i for i in l2 if i >= 0]
    return new_l2


def n5(l2):
    new_l2 = [l2[i] if l2[i] >= 0 else i + 1 for i in range(len(l2))]
    return new_l2


def n6(st):
    sl = {st[i]: i + 1 for i in range(len(st))}
    return sl


def n7(sp, sl):
    n = sum(1 for i in sp if i in sl.values())
    return n


def n8(evgene_o):
    sl = {i: evgene_o.count(i) for i in
    [evgene_o[j] for j in range(len(evgene_o))
     if evgene_o.count(evgene_o[j]) == 1 or evgene_o[:j].count(evgene_o[j]) == 0 ]}
    return sl


def n9(sl):
    n = sum([sl[i] for i in list(sl.keys()) if 'a' <= i and i <='z'])
    return n


def n10(d4):
    new_d4 = {str(int(i[0]) * i[1]): i[1] for i in list(d4.items())}
    return new_d4


def n11(d6, d5):
    d7 = {i: d6[i] for i in [j for j in list(d6.keys()) if not(j in list(d5.keys()))]}
    return d7


def n12(d5, d6):
    d8 = {str(i[0]): i[1] for i in
    [[j, d5[j]] if j in list(d5.keys()) else [j, d6[j]] for j in
     list(d5.keys()) + [l for l in list(d6.keys()) if not(l in list(d5.keys()))]]}
    return d8


print(n1(l1),
      n2(l1, 1),
      n3(l2),
      n4(l2),
      n5(l2),
      n6('abcd'),
      n7([1, 112, 20, 30, 7], {'a': 20, 'g': 112, 'e': 4, 'j': 30}),
      n8('ddhjhdio_ _'),
      n9({'d': 3, 'h': 2, 'j': 1, 'i': 1, 'o': 1, '_': 2, ' ': 1}),
      n10(d4),
      n11(d6, d5),
      n12(d5, d6),
      sep='\n')