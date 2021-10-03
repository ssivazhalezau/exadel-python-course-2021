tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}

def collect_leaves(t):
    leaves = []

    if isinstance(t, dict):
        for value in t.values():
            for v in collect_leaves(value):
                leaves.append(v)
    else:
        leaves = leaves + t

    return leaves

assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9] and collect_leaves([1, 2, 3]) == [1, 2, 3], 'Wrong function result'

print(collect_leaves(tree))
