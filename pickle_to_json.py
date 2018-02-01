import pickle, json
print('loading pickle...')

with open('tags_dict.pickle', 'rb') as fp:
    data = pickle.load(fp)

i = 1
for elem in data.keys():
	print('modifying elem ' + str(i) + 'of 9191 ish')
	data[elem] = data[elem].tolist()
	i += 1

print('writting to json...')
with open('wiki_tags.json', 'w') as fp:
    json.dump(data, fp)

