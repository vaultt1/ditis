# 3. Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

given_list=['a','b','c','d','e']

for i in range(len(given_list)):
    if given_list[i]=='b':
        given_list.pop(i)
        given_list.insert(i,[1,2,3])
    else:
        continue

print(f"{given_list}")