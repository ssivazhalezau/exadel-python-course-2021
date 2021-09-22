import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

words ={}

for i, sentence in enumerate(texts):
    for w in re.sub(r"[^\w]", " ", str.lower(sentence)).split():
        if w in words:
            words[w] = {'index': words[w]['index'], 'count': words[w]['count'] + 1}
        else:
            words[w] = {'index': i, 'count': 1}

print('word    count   first line')
for n, v in words.items():
    print(n.ljust(7), str(words[n]['count']).ljust(7), words[n]['index'])
