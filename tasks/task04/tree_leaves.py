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

leaves = []

def collect_leaves(t):
    global leaves

    assert not isinstance(t, dict) or not isinstance(t, list), 'We accept only tree of dicts'

    if isinstance(t, dict):
        for key, value in t.items():
            print ('k:', key, 'v:', value)
            if isinstance(value, dict):
                collect_leaves(value)
            else:
                leaves = leaves + value
    else:
        leaves = leaves + t

    return leaves

print(collect_leaves(tree))
# print(collect_leaves([1, 2, 3]))
