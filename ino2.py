from itertools import combinations

MOD = 10 ** 9 + 7


def minCost(n, k):

    subsets = []
    for i in range(1, n + 1):
        if i == k:
            subsets.append(list(range(1, i + 1)))
        else:
            for subset in combinations(range(1, i + 1), k):
                subsets.append(list(subset))
    subsets.sort()

    cost = 0
    for i in range(len(subsets) - 1):
        intersect = set(subsets[i]).intersection(set(subsets[i + 1]))
        cost += len(intersect)

    return cost % MOD
