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

    assert not isinstance(t, dict) or not isinstance(t, list), 'We accept only tree of dicts'

    if isinstance(t, dict):
        for value in t.values():
            if isinstance(value, dict):
                for v in collect_leaves(value):
                    leaves.append(v)
            else:
                leaves = leaves + value
    else:
        leaves = leaves + t

    return leaves

print(collect_leaves(tree))
print(collect_leaves(tree))
print(collect_leaves([1, 2, 3]))
