temp = X
X = Y
Y = temp

X, Y = Y , X

if x == 'A' and y == 'B':
    pass

if (x, y) == ('A', 'B'):
    pass

idx = 0
while idx < len(my_list):
    print(my_list[idx])
    idx += 1

for value in my_list:
    print(value)

"""
1行でやることは1つにする
"""

"""
ネストは3以下が目安
"""

idx = 0
for x in list_a:
    print(idx, x)
    idx += 1

for idx, x in enumerate(list_a):
    print(idx, x)