import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

words =[]

for i, sentence in enumerate(texts):
    index = i
    for w in re.sub("[^\w]", " ", str.lower(sentence)).split():
        dict_index = next((i for i, item in enumerate(words) if item['word'] == w), None)
        if dict_index is None:
            words.append({'word':w, 'count':1, 'index':i})

        else:
            words[dict_index]['count'] = words[dict_index]['count'] + 1

print('word    count   first line')
for i, word in enumerate(words):
    print(words[i]['word'].ljust(7), str(words[i]['count']).ljust(7), words[i]['index'])
