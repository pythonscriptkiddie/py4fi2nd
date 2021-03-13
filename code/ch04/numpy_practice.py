from copy import deepcopy

v = [0.5, 0.75, 1.0, 1.5, 2.0]
print('original v ', v)
m = 3*[deepcopy(v)]
print(m)
v[0] = 'python'
print('edited version of v ', v)
print('m remains unchanged', m)