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


"""
プライベートメソッド、プロパティには頭にアンダースコアを2つ付ける
クラスの内部からしかアクセスできなくなる
継承先のクラスも利用できない
"""
__show_user_list
__insert_date


"""
プロテクティッドメソッド、プロパティには頭にアンダースコアを1つ付ける
クラスの内部からと、継承先のクラスで利用できる
"""
__show_user_list
_insert_data

"""
tmpは一時的に使うような処理にだけ使用する
数百行もある処理にtmpは使わない
"""

for user in users:
    tmp_user = user
    #処理
    processed_users.append(tmp_user)


"""
単一責任の原則
全てのモジュールとクラスは1つの役割を提供して責任を持つべき
役割が複数ある場合、各クラスが何なのか複雑化してしまう
役割を分けることで、他のクラスから利用しやすくなり拡張性が上がる
"""