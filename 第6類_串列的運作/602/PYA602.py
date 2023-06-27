'''
602 撲克牌總和
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

提示：J、Q、K以及A分別代表11、12、13以及1。
'''

point = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
poker = [input() for i in range(5)]

total = 0
for i in poker:
  total += point.index(i) + 1

print(total)
